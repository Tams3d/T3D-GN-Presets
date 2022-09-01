from bpy.utils import *
from bpy.props import StringProperty
from bpy.types import Operator, Menu
import os
import bpy
import json
bl_info = {
    "name": "Tams 3d's GN Presets",
    "description": "A Collection of Incredibly useful nodes for Geometry Nodes",
    "author": "Tamil Selvan",
    "version": (1, 0, 0),
    "blender": (3, 3, 0),
    "location": "Geometry Node Editor > Add > T3D Presets",
    "doc_url":  "https://github.com/Tams3d/T3D-GN-Presets",
    "tracker_url": "https://github.com/Tams3d/T3D-GN-Presets/issues",
    "support": "COMMUNITY",
    "category": "Node",
}

addon_keymaps = {}
_icons = None


def load_preview_icon(path):
    global _icons
    if not path in _icons:
        if os.path.exists(path):
            _icons.load(path, path, "IMAGE")
        else:
            return 0
    return _icons[path].icon_id


def add_t3d_button(self, context):
    if context.area.ui_type == "GeometryNodeTree":
        self.layout.menu("NODE_MT_t3d_menu", text="T3D Presets", icon_value=load_preview_icon(
            os.path.join(os.path.dirname(__file__), 'assets', 'T3D.png')))


t3d_group_cache = {}
geonode_cat_list = []
draw_menu_functions = []

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
                entry = group_name.split("~")
                props = layout.operator(
                    NODE_OT_group_add.bl_idname,
                    text=entry[0].replace("3D", ""),
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
            draw_menu = generate_menu_draw(
                menu_type.bl_idname, menu_type.bl_label)
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


class NODE_OT_group_add(Operator):
    """Add a node group"""

    bl_idname = "tams3d.group_add"
    bl_label = "Add node group"
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
        old_groups = set(bpy.data.node_groups)

        for file in os.listdir(dir_path):
            if file.endswith(".blend"):
                filepath = os.path.join(dir_path, file)
                break
        else:
            raise FileNotFoundError("No .blend File in directory " + dir_path)

        with bpy.data.libraries.load(filepath, link=False) as (data_from, data_to):
            if self.group_name not in bpy.data.node_groups:
                data_to.node_groups.append(self.group_name)

        bpy.ops.node.add_node(type="GeometryNodeGroup")

        node = context.selected_nodes[0]
        node.node_tree = bpy.data.node_groups[self.group_name]

        node.location = context.space_data.cursor_location
        bpy.ops.transform.translate("INVOKE_DEFAULT")
        return {"FINISHED"}

    def invoke(self, context, event):
        self.store_mouse_cursor(context, event)
        return self.execute(context)


def t3d_add_to_node_ht_header_T3D(self, context):
    if not (False):
        layout = self.layout
        if bpy.context.area.ui_type == 'GeometryNodeTree':
            row_T3D = layout.row(heading='', align=True)
            row_T3D.alert = False
            row_T3D.enabled = True
            row_T3D.use_property_split = False
            row_T3D.use_property_decorate = False
            row_T3D.scale_x = 1.0
            row_T3D.scale_y = 1.0
            row_T3D.alignment = 'Expand'.upper()
            row_T3D.label(text='', icon_value=load_preview_icon(
                os.path.join(os.path.dirname(__file__), 'assets', 'T3D.png')))
            row_T3D.popover('T3D_PT_T3D_PRESET__UPDATES_T3D',
                            text='', icon_value=0)
        else:
            pass


class T3D_PT_T3D_PRESET__UPDATES_T3D(bpy.types.Panel):
    bl_label = 'T3D Preset  Updates'
    bl_idname = 'T3D_PT_T3D_PRESET__UPDATES_T3D'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'WINDOW'
    bl_context = ''
    bl_order = 0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        column_T3D = layout.column(heading='', align=True)
        column_T3D.alert = False
        column_T3D.enabled = True
        column_T3D.use_property_split = False
        column_T3D.use_property_decorate = False
        column_T3D.scale_x = 0.0
        column_T3D.scale_y = 1.25
        column_T3D.alignment = 'Expand'.upper()
        op = column_T3D.operator(
            'wm.url_open', text='Changelogs', icon_value=93, emboss=True, depress=False)
        op.url = 'https://github.com/Tams3d/T3D-GN-Presets/edit/Development/README.md#magic_wand-changelogs--release-notes'
        op = column_T3D.operator(
            'wm.url_open', text='Example Files', icon_value=695, emboss=True, depress=False)
        op.url = 'https://discord.gg/eKdswfAS'
        op = column_T3D.operator(
            'wm.url_open', text='Report A Bug', icon_value=68, emboss=True, depress=False)
        op.url = 'https://github.com/Tams3d/T3D-GN-Presets/issues/'


def draw(self, context):   
        layout = self.layout
        addon_updater_ops.update_settings_ui(self, context)

def register():
    global t3d_group_cache
    with open(os.path.join(os.path.dirname(__file__), "geonode_nodes.json"), "r") as f:
        t3d_group_cache = json.loads(f.read())

    if not hasattr(bpy.types, "NODE_MT_t3d_menu"):
        bpy.utils.register_class(NODE_MT_t3d_menu)
        bpy.types.NODE_MT_add.append(add_t3d_button)
    bpy.utils.register_class(NODE_OT_group_add)
    geonode_cat_generator()
    global _icons
    _icons = bpy.utils.previews.new()

    bpy.types.NODE_HT_header.append(t3d_add_to_node_ht_header_T3D)
    bpy.utils.register_class(T3D_PT_T3D_PRESET__UPDATES_T3D)


def unregister():
    for func in draw_menu_functions:
        bpy.types.NODE_MT_t3d_menu.remove(func)
    if hasattr(bpy.types, "NODE_MT_t3d_menu"):
        bpy.types.NODE_MT_add.remove(add_t3d_button)
        bpy.utils.unregister_class(NODE_MT_t3d_menu)
    bpy.utils.unregister_class(NODE_OT_group_add)
    global _icons
    bpy.utils.previews.remove(_icons)
    bpy.types.NODE_HT_header.remove(t3d_add_to_node_ht_header_T3D)
    bpy.utils.unregister_class(T3D_PT_T3D_PRESET__UPDATES_T3D)
