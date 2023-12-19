<div align="center">

# T3D GN Presets
##  A Collection of Incredibly useful nodes for Geometry Nodes - Blender 4.0
![T3D GN Presets](https://user-images.githubusercontent.com/106262964/234839626-d88f0ce9-2399-4193-9940-2257bc728351.png)

<br>
</div>

# 💡 Introduction:

* [T3D GN Presets](https://github.com/Tams3d/T3D-GN-Presets/#t3d-gn-presets) contains Node groups for Geometry Nodes which include Deformers, Fields, SDF, UV, Utilities and much more for **free!**
* This is an essential component of an artist’s toolkit which enables users to combine multiple nodes with endless possibilities in non-destructive workflows with existing Blender tools.

# 🪄 Release Notes:

- **T3D-GN-Presets (v1.4.0)** to be released on 11.03.2024
- For Blender 4.0 & below, checkout lastest releases [here](https://github.com/Tams3d/T3D-GN-Presets/releases).

# Planned Changes:
## Aim
- Our current goals for T3D GN Presets include ensuring smooth compatibility with Blender 4.1, introducing new features for the Grease Pencil, Volumes, and utilizing the latest Blender nodes. We're making the nodes faster, optimizing it for a better user experience.
- Clear documentation and video tutorials are a priority, making it easy for users to understand and use T3D GN Presets.
- We're also keen on building a friendly and supportive community where users can share experiences and learn from each other.

## Core
- [ ] Preferences Panel
- [ ] Node Tools

## Support
- [ ] Support Rotation Socket Type
- [ ] Support for Subpanels and Gizmos
- [ ] Support Volume & SDF nodes
- [ ] Support for Matrix Inputs
- [ ] Implicitly use "Normal" and "Position" directly from Input
- [ ] Tooltip for all nodes

## New Nodes
- [ ] Nodes for Grease Pencil
- [ ] Curve Deform
- [ ] Loft Curve

## Depreciations
- [x] Depreciate Segmental Extrude
- [x] Depreciate Shade Auto Smooth
- [ ] Depreciate SDF nodes

## Documentations & Tutorials
- Still yet to be planned. A full form doucmentation will be written and included along with the addon which also includes links to tutorial.

# ⚙️ Core:
## Source Files
- Follow **Black** code style [(6ca7f8b)](https://github.com/Tams3d/T3D-GN-Presets/commit/6ca7f8b)
- Renamed **geonode_groups.json** >>> [**t3d_nodegroups.json**](https://github.com/Tams3d/T3D-GN-Presets/blob/Master/t3d_nodegroups.json)
- Renamed **geonode_nodes.blend** >>> [**t3d_nodes.blend**](https://github.com/Tams3d/T3D-GN-Presets/blob/Master/t3d_nodes.blend)

# 🎉 New Nodes, Features & Changes:

## 🎆 New Features & Changes:
- **Geometry To Spline** inputs selection. Supports Mesh,Curve and instances. Adapted new Points to Curve node. [(0a2f609)](https://github.com/Tams3d/T3D-GN-Presets/commit/0a2f609)

### Deformer
- `Deformers` can only be used in Geometry Node Modifier.

## Depreciationed Features:
- Removed **Shade Auto Smooth** as a future replacement for built-in [node](https://projects.blender.org/blender/blender/pulls/108014)
- `Deformers` are no longer **Assets**. [(074b970)](https://github.com/Tams3d/T3D-GN-Presets/commit/074b970)

# 🎯 Development
- Developments are happening regularly regarding bug fixes, and support for every upcoming [Blender Release](https://www.blender.org/download/releases/)
- Contributing are always welcomed!

## 👻 Bug Reports
- Bug reports are always welcomed in the form of reports or suggestions.
- Suggestions can be included with brief explanations of usability.
- Submit Bug reports and feature requests [here](https://github.com/Tams3d/T3D-GN-Presets/issues)

# Licencing & Files:
## 📄 Licence
- The Node groups, including the Addon, are licensed as [GNU GPL](https://github.com/Tams3d/T3D-GN-Presets/blob/Master/LICENSE.txt)
  * You are free for any purpose
  * You are free to distribute unless the license is modified
  * You can distribute changed versions
  * What you create with this Addon is your sole property
  * You are not allowed to change the license or introduce additional terms and conditions

## 📂 Access to Files:
- [ `_init_.py` ](https://github.com/Tams3d/T3D-GN-Presets/blob/Master/__init__.py) defines the addon followed by [t3d_nodegroups.json](https://github.com/Tams3d/T3D-GN-Presets/blob/Master/t3d_nodegroups.json) which contains a list of categories with nodes.
- [t3d_nodes.blend](https://github.com/Tams3d/T3D-GN-Presets/blob/Master/t3d_nodes.blend) contains all the Node-groups which are displayed under `T3D GN Presets`
- **All Files & Assets** follow the same [Licence](https://github.com/Tams3d/T3D-GN-Presets/blob/Master/LICENSE.txt)

# 🦄 About 
  - Hey! I am **Tamil Selvan**, also known as **tams_3d**. I am a 16-Year-Old Self Taught Blender Artist from **India**
  - My Vision is to create *Free* for the Blender, which requires complex setups provided in a simplified and effective way.
  - Currently developing Presets for Geometry Nodes which are similar to tools and features of other 3D Packages and some add-ons.
  - I believe that my work contributes to a better world for 3D Artists, Game Developers and other artists who create incredible works.
  
  # 🥂 Socials
  - Catch up with me here:
    * [Behance](https://www.behance.net/tamilselvan3d)
    * [GitHub](https://github.com/Tams3d)
    * [X (Twitter)](https://twitter.com/Tams_3d)
