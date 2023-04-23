<div align="center">

# T3D GN Presets
##  A Collection of Incredibly useful nodes for Geometry Nodes - 3.5
![T3D GN Presets](https://user-images.githubusercontent.com/106262964/233781475-2a48c999-f843-476a-a9bb-75e61e0781f4.png)

<br>
</div>

# 💡 Introduction:
* [T3D GN Presets](https://github.com/Tams3d/T3D-GN-Presets/) contains Node Groups for Geometry Nodes which include Deformers, Fields, SDF, UV, Utilities and much more for **free!**
* This is an essential component of an artist’s toolkit which enables users to combine multiple nodes with endless possibilities in non-destructive workflows with existing Blender tools.

# 🪄 Release Notes:
- **T3D-GN-Presets (v1.2.0)** released on 24.04.2023
- Download older versions for Blender 3.4 & below [here](https://github.com/Tams3d/T3D-GN-Presets/releases)    
- [Corrective Release](https://github.com/Tams3d/T3D-GN-Presets/tree/Master#-corrective-releases) has been introduced for [LTS](https://github.com/Tams3d/T3D-GN-Presets/releases/tag/LTS)

# ⚙️ Core:
## Source Files
- Execute code when it runs as script, prevents running as imported module.
- Added disabled buttons for Separation and Visual Improvement, **`^ `** as prefix makes disabled button
- Tooltips are now more specific on functions 
- `Deformers` which work in all types of geometry are now converted to **Assets**
- Added [Icons](https://github.com/Tams3d/T3D-GN-Presets/tree/Master/Icons) for `Deformers` which now supports **Asset Browser**

## Nodes
- Fixed Tooltips
- Changed Appropriate input sub-type.
- Replaced appropriate **[Mix node](https://archive.blender.org/developer/D13749)** for Data Types: float, vector & color.
- Files saved with the new node are not compatible with older versions of Blender. Files saved with older versions of addons are still compatible.
- `Coordinates` have been moved to `Vector` (Catergory)
- Renamed **Smooth >>> Smooth Geometry**, provided support for Mesh & Curves
- Fixed `Cartesian to Cylindrical` **(r, θ, z)**
- Fixed `Fields` scale evaluation
- *Field Inputs* are now hidden by default
- Removed **Modify Field** as functions of it can be created with basic setups
- Removed **Smooth Curve** as a replacement for  **Smooth Geometry**

## 🪅 Performance:
- `Smooth Geometry` evaluates much faster, ignores Point Clouds and Instances
- `UV To Mesh` to calculate UV at initial position avoids flicker and more stable and 1.5x faster because of [Spilt Edges mesh operator and multi-threading](https://projects.blender.org/blender/blender/commit/e83f46ea7630)
- `Geometry To Spline` does not remap index, removal of *Trim* 
- *Boolean inputs* to be made constant to avoid field computation in `Align To Spline` `Set Geometry Visibility` `Lathe Curve`


# 🎉 New Nodes, Features & Changes:
## New Nodes:
- **Delete Island** - Deletes Mesh Island by size
- **Extend Curve** - Extrudes the endpoints of the curve along *Curve Tangent*
- **Vertex Slide** - Move vertices based on index
- **Rename Named Attribute** - Rename Stored Named Attribute (only Float & Vector are supported)

### Input:
- **Component Selection** - Select Individual Components
- **Edge Path Selection** - Select shortest edge path
- **Select Similar Vertices** - Select Similar Vertices by property type
- **Select Similar Edges** - Select Similar Edges by property type
- **Select Similar Faces** - Select Similar Faces by property type
- **Select Index Range** - Select Index ranging from min & max value

### UV:
- **UV Deform** - Sets sampled position based on UV from Sample Mesh on Deform Mesh
- **Flip UV** - Flips U & V of  UV Map
- **UV Displace** - Displace UV using vector
- **UV Project** - Generate UV Map based on Axis

## 🎆 New Features & Changes:
- Added `Deformers` as **Assets** now supports Drag & Drop with Asset Browser for appended nodes.
- Added *Disabled Buttons* as inter-catergory Separators
- Added Per Axis Strength as default `Displacer`
- Added *Position* input for **SDF**
- `Smooth Geometry` can now input **Stiffness** works with Mesh
- `Phyllotaxis`  outputs **Normal** of the points from Mesh
- `Smooth Geometry` to work with [Blur Attribute](https://projects.blender.org/blender/blender/commit/d68c47ff347bbb3824)
- `Mesh To SDF` `Mesh To Field` are now evaluated using Raycast method.
- **Deformers** now support *Instances* as realised geometry.

## 👻 Bug Reports
- Bug reports are always welcomed in the form as reports or suggestions.
- Suggestions can be included with brief explanations of usability.
- Submit Bug reports and feature requests [here](https://github.com/Tams3d/T3D-GN-Presets/issues)

# 🎯 Development
- Developments are happening locally on regular basis regarding bug fixes, and support for every upcoming [Blender](https://www.blender.org/) release.
- [Simulation Nodes](https://builder.blender.org/download/experimental/geometry-nodes-simulation/)  will get eventually be supported when packed with Stable Blender releases. 
- Support for Hair Curves has been provided by default. 
- Dev conversations may get started in future on My [Discord Server](https://discord.gg/TNgzbZCdnY)
- Closed [GitHub Projects](https://github.com/users/Tams3d/projects/2/views/1) for maintinance reasons.
- Closed & Removed *Experimental Branch*
- Removed `v1.0.0` release as a replacement for [`Corrective Release (v1.0.1)`](https://github.com/Tams3d/T3D-GN-Presets/releases/tag/v1.0.1)

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
  - My Vision is to create *Free* for the Blender Community, which requires complex setups provided in a simplified, effective way.
  - Currently developing Presets for Geometry Nodes which are similar to tools and features of other 3D Packages and some add-ons.
  - I believe that my work contributes to a better world for 3D Artists, Game Developers and other artists who create incredible works.
  
  # 🥂 Socials
  - Catch up with me here:
    * [Behance](https://www.behance.net/tamilselvan3d)
    * [Discord](https://discord.gg/TNgzbZCdnY)
    * [GitHub](https://github.com/Tams3d)
    * [Twitter](https://twitter.com/Tams_3d)
