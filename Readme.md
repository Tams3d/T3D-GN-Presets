<div align="center">

# T3D GN Presets
##  A Collection of Incredibly useful nodes for Geometry Nodes - Blender 3.6 LTS (Beta)
![T3D GN Presets](https://user-images.githubusercontent.com/106262964/234839626-d88f0ce9-2399-4193-9940-2257bc728351.png)

<br>
</div>

# 💡 Introduction:

* [T3D GN Presets](https://github.com/Tams3d/T3D-GN-Presets/) contains Node groups for Geometry Nodes which include Deformers, Fields, SDF, UV, Utilities and much more for **free!**
* This is an essential component of an artist’s toolkit which enables users to combine multiple nodes with endless possibilities in non-destructive workflows with existing Blender tools.

# 🪄 Release Notes:

- **T3D-GN-Presets (v1.3.0)** to be released on 27.05.2023
- Download stable version for Blender 3.5 & below [here](https://github.com/Tams3d/T3D-GN-Presets/releases)    

# ⚙️ Core:

## Source Files
- Removed unnecessary code comments, empty lines and spaces [(0d4126a)](https://github.com/Tams3d/T3D-GN-Presets/commit/0d4126a9272584c5f80e585ce6ace9d085e8bce2)
- Optimised all icons for Deformers. **Displacer** and **Smooth Geometry** are now assets. Filled necessary informations [(42fdcbc)](https://github.com/Tams3d/T3D-GN-Presets/commit/42fdcbce5ce1547c0f42f93cfab3eb0191b9b14c)
- Removed Exif data from images, solves empty Icon issue

## Nodes
- Fixed implicit issues with nodes [(c7acb1c)](https://github.com/Tams3d/T3D-GN-Presets/commit/c7acb1c97e18864f473bb6a37d39b4d48f8beac3)
  - Fixed jitter in Smooth Geometry
  - Clamp Fields and SDF
  - Fix rotation center in Parent To Object
  - Maintain consistency in input and output names

## 🪅 Performance:
- Nodes with Store Named Attribute are slightly faster and memory efficient [(b54398c16c)](https://projects.blender.org/blender/blender/commit/b54398c16cfee14a054e2c3ec82d091b34c79a34)
- Assets are now loaded faster, saves upto 10 mb [(42fdcbc)](https://github.com/Tams3d/T3D-GN-Presets/commit/42fdcbce5ce1547c0f42f93cfab3eb0191b9b14c)
- Rewritten **UV Project** uses Euler Angles to project and fit mesh islands inside a 1-meter boundary
- Fixed overhead with **UV Project** with high poly mesh

# 🎉 New Nodes, Features & Changes:

## New Nodes:
- **Align Island** - Aligns Mesh Island by axis
- **Geometry Size** - Outputs bound geometry size, bound center and max size
- **Match Topology** - Transforms Mesh by Topology
- **Simple Decimate** - Merge Faces by distance by proximate points

## 🎆 New Features & Changes:

- Nodes are rearranged based on usability with separations. Tooltips are made mandatory for all nodes.
- **Point Honeycomb** inputs Poin Radius
- **Rotate Elements** now supports Edges
- Renamed **Transforms To Position** >>> **Transform Position**
- **Transform Position** is moved to Vector (category) [(c7acb1c)](https://github.com/Tams3d/T3D-GN-Presets/commit/c7acb1c97e18864f473bb6a37d39b4d48f8beac3)
- **Smooth Geometry** does not restore initial size and position to avoid jitter [(c7acb1c)](https://github.com/Tams3d/T3D-GN-Presets/commit/c7acb1c97e18864f473bb6a37d39b4d48f8beac3)
- Easing nodes are rearranged based on easing strength [(ff3cbc9)](https://github.com/Tams3d/T3D-GN-Presets/commit/ff3cbc97200fff4e4262fb747f2c9fe88f19a27b)
- **Vertex Slide** has been ported with new Index of Nearest [(1ab598b)](https://github.com/Tams3d/T3D-GN-Presets/commit/1ab598bb74ef5d80a6cc69caff7a3f897f844815)

## Breaking Changes:
- Removed **Select Index Range** 
- Breaks backwards compatibility in **Vertex Slide**. **Index of Nearest** does not support offsetting, input of Nearest Index is removed.

# 🎯 Development
- Developments are happening locally regularly regarding bug fixes, and support for every upcoming [Blender](https://www.blender.org/) release.
- Check development process [here.](https://github.com/Tams3d/T3D-GN-Presets/issues/16) New tasks might be created depending on the needs. Community Contributions are always welcomed

## 👻 Bug Reports
- Bug reports are always welcomed in the form of reports or suggestions.
- Suggestions can be included with brief explanations of usability.
- Submit Bug reports and feature requests [here](https://github.com/Tams3d/T3D-GN-Presets/issues)

# Licencing & Files:
## 📄 Licence
- The Node groups, including the Addon, are licensed as [GNU GPL](https://github.com/Tams3d/T3D-GN-Presets/blob/Master/LICENSE)
  * You are free for any purpose
  * You are free to distribute unless the license is modified
  * You can distribute changed versions
  * What you create with this Addon is your sole property
  * You are not allowed to change the license or introduce additional terms and conditions

## 📂 Access to Files:
- [ `_init_.py` ](https://github.com/Tams3d/T3D-GN-Presets/blob/Master/__init__.py) defines the addon followed by [geonode_groups.json](https://github.com/Tams3d/T3D-GN-Presets/blob/Master/geonode_groups.json) which contains a list of categories with nodes.
- [geonode_nodes.blend](https://github.com/Tams3d/T3D-GN-Presets/blob/Master/geonode_nodes.blend) contains all the Node-groups which are displayed under `T3D GN Presets`
- **All Files & Assets** follow the same [Licence](https://github.com/Tams3d/T3D-GN-Presets/blob/Master/README.md#licencing--files)

# 🦄 About 
  - Hey! I am **Tamil Selvan**, also known as **tams_3d**. I am a 16-Year-Old Self Taught Blender Artist from **India**
  - My Vision is to create *Free* for the Blender, which requires complex setups provided in a simplified and effective way.
  - Currently developing Presets for Geometry Nodes which are similar to tools and features of other 3D Packages and some add-ons.
  - I believe that my work contributes to a better world for 3D Artists, Game Developers and other artists who create incredible works.
  
  # 🥂 Socials
  - Catch up with me here:
    * [Behance](https://www.behance.net/tamilselvan3d)
    * [Discord](https://discord.gg/TNgzbZCdnY)
    * [GitHub](https://github.com/Tams3d)
    * [Twitter](https://twitter.com/Tams_3d)
