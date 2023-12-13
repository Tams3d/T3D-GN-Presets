"""
    Copyright (C) 2023  Tamil Selvan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# Importing Modules
import bpy
import json
import os
from bpy.utils import *
from bpy.props import StringProperty
from bpy.types import Operator, Menu

# Addon Info
bl_info = {
    "name": "T3D GN Presets",
    "author": "Tamil Selvan",
    "description": "T3D GN Presets contains Node groups for Geometry Nodes for a non-destructive workflow of proceduralism",
    "location": "Geometry Node Editor > Add > T3D GN Presets",
    "blender": (4, 0, 0),
    "version": (1, 4, 0),
    "doc_url": "https://github.com/Tams3d/T3D-GN-Presets",
    "tracker_url": "https://github.com/Tams3d/T3D-GN-Presets/issues/new/",
    "category": "Node",
}

# Load Icons
_icons = None


def load_preview_icon(path):
    global _icons
    if not path in _icons:
        if os.path.exists(path):
            _icons.load(path, path, "IMAGE")
        else:
            return 0
    return _icons[path].icon_id


# T3D Node Header at Geometry Node Editor
def t3d_ht_header(self, context):
    if not (False):
        layout = self.layout
        if bpy.context.area.ui_type == "GeometryNodeTree":
            layout.label(
                icon_value=load_preview_icon(
                    os.path.join(os.path.dirname(__file__), "Icons", "T3D.png")
                )
            )


# T3D GN Presets Menu + Icon at Geometry Node Editor > Add > T3D GN Presets
def add_t3d_button(self, context):
    if context.area.ui_type == "GeometryNodeTree":
        self.layout.menu(
            "NODE_MT_t3d_menu",
            text="T3D GN Presets",
            icon_value=load_preview_icon(
                os.path.join(os.path.dirname(__file__), "Icons", "T3D.png")
            ),
        )


t3d_group_cache = {}
geonode_cat_list = []
draw_menu_functions = []

# File Path
dir_path = os.path.dirname(__file__)


def geonode_cat_generator():
    global geonode_cat_list
    global draw_menu_functions

    geonode_cat_list = []
    draw_menu_functions = []

    for item in t3d_group_cache.items():

        def custom_draw(self, context):
            layout = self.layout
            for group_name in t3d_group_cache[self.bl_label]:
                if group_name == "_":
                    layout.separator(factor=1.0)
                    continue

                # Use group name starts with "^ " as disabled button
                if group_name.startswith("^ "):
                    layout.label(text=group_name.split("^ ")[1])
                    continue

                # Set group name after " ~ " as tooltip
                entry = group_name.split(" ~ ")
                props = layout.operator(
                    NODE_OT_group_add.bl_idname,
                    text=entry[0],
                )
                props.group_name = entry[0]

                if len(entry) > 1:
                    props.tooltip = entry[1]

        itemid = item[0].split("_")[0]

        menu_type = type(
            "NODE_MT_category_" + itemid,
            (bpy.types.Menu,),
            {
                "bl_idname": "NODE_MT_category_" + itemid.replace(" ", "_"),
                "bl_space_type": "NODE_EDITOR",
                "bl_label": item[0],
                "draw": custom_draw,
            },
        )
        if menu_type not in geonode_cat_list:

            def generate_menu_draw(name, label):
                def draw_menu(self, context):
                    self.layout.menu(name, text=label.split("_")[0])

                return draw_menu

            bpy.utils.register_class(menu_type)
            draw_menu = generate_menu_draw(menu_type.bl_idname, menu_type.bl_label)
            bpy.types.NODE_MT_t3d_menu.append(draw_menu)

            draw_menu_functions.append(draw_menu)
            geonode_cat_list.append(menu_type)


class NODE_MT_t3d_menu(Menu):
    bl_label = "T3D"
    bl_idname = "NODE_MT_t3d_menu"

    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == "GeometryNodeTree"

    def draw(self, context):
        pass


# Append Operator
class NODE_OT_group_add(Operator):
    """Add a node group"""

    bl_idname = "tams3d.group_add"
    bl_label = "Add a node group"
    bl_description = "Append Node Group"
    bl_options = {"REGISTER", "UNDO"}

    group_name: StringProperty()
    tooltip: StringProperty()

    @staticmethod
    def store_mouse_cursor(context, event):
        space = context.space_data
        tree = space.edit_tree

        if context.region.type == "WINDOW":
            space.cursor_location_from_region(
                event.mouse_region_x, event.mouse_region_y
            )
        else:
            space.cursor_location = tree.view_center

    @classmethod
    def poll(cls, context):
        return context.space_data.node_tree

    @classmethod
    def description(self, context, props):
        return props.tooltip

    def execute(self, context):
        for file in os.listdir(dir_path):
            if file.endswith(".blend"):
                filepath = os.path.join(dir_path, file)
                break
        else:
            raise FileNotFoundError(
                f"No .blend file found in the directory: {dir_path}"
            )

        with bpy.data.libraries.load(filepath, link=False) as (data_from, data_to):
            if self.group_name not in bpy.data.node_groups:
                data_to.node_groups.append(self.group_name)

        bpy.ops.node.add_node(type="GeometryNodeGroup")
        node = context.selected_nodes[0]
        node.node_tree = bpy.data.node_groups[self.group_name]

        # Place Node Group at Mouse Cursor Location
        node.location = context.space_data.cursor_location
        bpy.ops.transform.translate("INVOKE_DEFAULT")
        return {"FINISHED"}

    def invoke(self, context, event):
        self.store_mouse_cursor(context, event)
        return self.execute(context)


# Functions to Register
def register():
    global t3d_group_cache
    with open(os.path.join(os.path.dirname(__file__), "t3d_nodegroups.json"), "r") as v:
        t3d_group_cache = json.loads(v.read())

    if not hasattr(bpy.types, "NODE_MT_t3d_menu"):
        bpy.utils.register_class(NODE_MT_t3d_menu)
        bpy.types.NODE_MT_add.append(add_t3d_button)
    bpy.utils.register_class(NODE_OT_group_add)
    geonode_cat_generator()
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.types.NODE_HT_header.append(t3d_ht_header)


# Functions to Unregister
def unregister():
    for func in draw_menu_functions:
        bpy.types.NODE_MT_t3d_menu.remove(func)
    if hasattr(bpy.types, "NODE_MT_t3d_menu"):
        bpy.types.NODE_MT_add.remove(add_t3d_button)
        bpy.utils.unregister_class(NODE_MT_t3d_menu)
    bpy.utils.unregister_class(NODE_OT_group_add)
    global _icons
    bpy.utils.previews.remove(_icons)
    bpy.types.NODE_HT_header.remove(t3d_ht_header)


if __name__ == "__main__":
    register()
