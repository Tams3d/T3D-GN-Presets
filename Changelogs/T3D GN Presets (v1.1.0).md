<div align="center">

# Tams 3d's GN Presets
##  A Collection of Incredibly useful nodes for Geometry Nodes - 3.4 & Above
![T3D GN Presets](https://user-images.githubusercontent.com/106262964/173188615-21216a7b-6e8b-4319-bf33-954b940ac4b5.png)

<br>
</div>

# 💡 Introduction:
* [T3D GN Presets](https://github.com/Tams3d/T3D-GN-Presets/) are Custom made Node Groups for Geometry Nodes which include Primitive Geometry, Deformers, Fields, SDF, Utilities and much more for **free!** only for [Blender](https://www.blender.org). 
* This is an essential component of an artist’s toolkit which enables users to combine multiple nodes with endless possibilities in non-destructive workflows with existing Blender tools.
* *T3D GN Presets* is a user-friendly addon that helps artists generate faster recursions of ideas by unlocking proceduralism. 

# 🪄 Release Notes:
- **T3D-GN-Presets (v1.1.0)** is now Active and Stable
- Find older version release notes [here](https://github.com/Tams3d/T3D-GN-Presets/tree/Master/Changelogs).     
- [Corrective Release](https://github.com/Tams3d/T3D-GN-Presets/tree/Master#-corrective-releases) has been introduced for minor fixes.

# ⚙️ Core:
- Complete Restructuring of [ `_init_.py` ](https://github.com/Tams3d/T3D-GN-Presets/blob/Master/__init__.py) which packs more information to developers such as Licence, Previous updates and further improvements.
- Removed unfinished/ unreleased features.
- Maintained lowercase and relative paths.
- Cleared Popover & with only Icon.

## 🪅 Performance:
- Rewritten `Parent To Object` to work more stable
- Rewritten `Displacer` gains 5-10% speed and stability with a 1 Million vertex grid
- Rewritten `UV To Mesh` is now 2-5% faster
- Rewritten `Align To Spline` to work with all types of splines
- Rewritten all Fields nodes to improve stability. Fixed inverted direction while transforming with empties
- Removal of UV feature in `Sweep Curve` gains 85% increase. Supports non-cyclic curves
- Renamed & Rewritten `Reset Position` to `Center Elements` is 15% faster with Mesh, Curves, Points, Instances, Volume Combined
- Rewritten `Inset Faces` work without internal dependencies to reduce attribute-storing computations  

## 🎉 New Nodes & Categories:
### Nodes
- **Smooth Curve** - Curve to Bezier with smoothing
- **Prism Field** - Prism Falloff
- **Torus Field** - Torus Falloff
- **Modify Field** - Field Modifier with direct controls of the Input Field
- **Smooth** - Smooths a mesh by averaging Face angles

### Category: SDF (Signed Distance Function)
- SDF Box
- SDF Cylinder
- SDF Ngon
- SDF Torus
- SDF Boolean
- SDF Displacement

## 🎆 New Features & Changes:
### Features

- Added *Tooltips*
- Added *Separators*
- Added per Mesh island control and Selection to `Center Elements`
- Added strength with separate Axis Controls for `Displacer` now Supports Geometry without Generic Normal Attribute
- Added Invert in `Transforms To Position` and `Vector Mapping`
- Added Offset Output in `Center Elements` & `Rotate Elements` Now outputs change in Position
- Added Support for *Geometry Type: Volume* in `Instancers`

### Changes & Fixes
- Renamed Inputs and Outputs to make uniform across the category
- Removed _Bound Center_ & Added _Mesh Island_ in `Center Elements` to calculate per mesh island. Defaulted to Bound Center for faster computations
- Renamed `Manifold Edge Selection` to `Non-Manifold Edge Selection` with Non-Manifold Edge Selection Output
- Made _Center at Origin_ as default in Curve Primitives, Point Primitives and Instancers
- Replaced _String_ to _Vector_ input in `UV To Mesh`
- `Poke Faces` now outputs New Vertices Selection
- Fixed `Spherify` to preserve Face Area
- Corrected inverted scale in `Transforms to Position`

## 🚨 Breaking Changes
- Removed UV from `Sweep Curve`
- Reset Position renamed to `Center Elements`
- Removed *Offset* in `Rotate Elements` `Set Geometry Size` `Center Elements` 
- Removed category `Generators` which includes _Distribute Points in Volume_
- Fields are optimised to use with empty which may behave oddly in different Viewport Perspectives and are made Scale-based instead of size-based


# 🎯 Development
- Developments are happening regularly in [Experimental Branch](https://github.com/Tams3d/T3D-GN-Presets/tree/Master) regarding bug fixes, and support for every upcoming [Blender](https://www.blender.org/) release.
- Support for [Blender 3.5 Alpha](https://wiki.blender.org/wiki/Reference/Release_Notes) is not yet started as of now. [Simulation Nodes](https://builder.blender.org/download/experimental/geometry-nodes-simulation/)  will get supported eventually. 
- Dev talks may start in future on My [Discord Server](https://discord.gg/TNgzbZCdnY)
- Introduction of [GitHub Projects](https://github.com/users/Tams3d/projects/2/views/1) for productivity

#### ✅ Corrective Releases:
- As of now, there are no major issues or bugs.
- Minor fixes will be directly committed from `Experimental` → `Master` apart from [Release](https://github.com/Tams3d/T3D-GN-Presets/releases/)
- Substantial fixes will be released directly replacing the Main Release as Corrective Release.

## ♾️ GitHub Repository Changes
### Issues 
- 🚀 [Release (v1.1.0): Recorrecting, Regression, Removing, Renaming, Restructuring](https://github.com/Tams3d/T3D-GN-Presets/issues/12)
- ✅ [Support: Need Built in Reset Position node in Deformers](https://github.com/Tams3d/T3D-GN-Presets/issues/5)
- ✅ [Support: Geometry Type - Instance, Volume](https://github.com/Tams3d/T3D-GN-Presets/issues/6)
- ✅ [Node: UV To Mesh - Needs Support For Mesh Without default Uv](https://github.com/Tams3d/T3D-GN-Presets/issues/7)
- ⭕ [Documentation: Installing, Usage, Restrictions](https://github.com/Tams3d/T3D-GN-Presets/issues/10)

## 👻 Bug Reports & Fixes
- Submit Bug reports and feature requests [here](https://github.com/Tams3d/T3D-GN-Presets/issues)
- Review file changes [here](https://github.com/Tams3d/T3D-GN-Presets/pulls)
- Fixes will be provided periodically as assured

## 🔗 Updates & Restrictions:
- Our Presets are made only to run on Latest Stable Blender Release as of date - **Blender 3.4 & Above**
- Due to the Introduction of [Named Attributes System](https://developer.blender.org/T91742) - nodes contain some **Internal Dependencies** which may conflict with existing attributes
- The `Transfer Attribute` node has been removed and split into multiple more specific nodes - [Sample Index, Sample Nearest, Sample Nearest Surface ](https://developer.blender.org/D15909)
- Older versions will be discontinued, and the User Needs to manually upgrade to [New Version](https://github.com/Tams3d/T3D-GN-Presets/releases)
- `Tams 3d's GN Presets` have been used as `T3D GN Presets` to conserve string length

# Licencing & Files:
## 📄 Licence
- The Node groups, including the Addon, are licensed as [GNU GPL](https://github.com/Tams3d/T3D-GN-Presets/blob/Master/LICENSE) - the same license as Blender uses
  * You are free for any purpose
  * You are free to distribute unless the license is modified
  * You can distribute changed versions
  * What you create with This Addon is your sole property
  * You are not allowed to change the license or introduce additional terms and conditions
  
## 📂 Access to Files:
- [ `_init_.py` ](https://github.com/Tams3d/T3D-GN-Presets/blob/Master/__init__.py) defines the addon followed by [geonode_groups.json](https://github.com/Tams3d/T3D-GN-Presets/blob/Master/geonode_groups.json) which contains a list of categories with nodes.
- [geonode_nodes.blend](https://github.com/Tams3d/T3D-GN-Presets/blob/Master/geonode_nodes.blend) contains all the Node-groups which are displayed under `T3D GN Presets` 
- All these files follow the same [Licence](https://github.com/Tams3d/T3D-GN-Presets/blob/Master/README.md#licencing--files)

# 🦄 About 
  - Hey! I am **Tamil Selvan**, also known as **tams_3d**. I am a 15-Year-Old Self Taught Blender Artist from **India**.
  - My Vision is to create *Free & Paid Resources* for the Blender Community, which requires complex setups provided in a simplified, effective way.
  - Currently developing Presets for Geometry Nodes which are similar to tools and features of other 3D Packages and some add-ons.
  - I believe that my work contributes to a better world for 3D Artists, Game Developers and other artists who create incredible works.
  
  ### 🥂 Socials
  - Catch up with me here:
    * [Behance](https://www.behance.net/tamilselvan3d)
    * [Discord](https://discord.gg/TNgzbZCdnY)
    * [GitHub](https://github.com/Tams3d)
    * [Twitter](https://twitter.com/Tams_3d)
