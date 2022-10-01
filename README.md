<div align="center">
  <img src="https://user-images.githubusercontent.com/106262964/191753865-f69ae775-f7cf-4075-8ac9-0d1861b9fef1.png"
       width="100">
  <!--T3D Icon with Head er-->
  <h1>Tams 3d's GN Presets</h1>
  <h3>A Collection of Incredibly useful nodes for Geometry Nodes</h3>

[Introduction]() | [Installation]() | [Release Notes]() |  [Development]() | [Licence]() |  [About]() 
  <!--Center Sub-header-->

***<<<<< Work-In-Process >>>>>***
</div>
<br>

# Introduction:
* [T3D GN Presets](https://github.com/Tams3d/T3D-GN-Presets/) are Custom made Node Groups for Geometry Nodes which include Primitive Geometries, Deformers, Fields, Generators, Utilities and much more for **free!** only for [Blender](https://www.blender.org). 
* This is an essential component of an artist’s toolkit which enables users to combine multiple nodes with endless possibilities in non-destructive workflows with existing Blender tools.
* *T3D GN Presets* is a user-friendly addon that helps artists generate faster recursions of ideas by unlocking proceduralism. 

# Installation:
<div align="center">
<<<< Video Place Holder - Installation T3D GN Presets >>>>
  <!-- A Video about How to install T3D GN Presets-->
  </div>
<br>
  <!-- A short description -->
- Lorem ipsum dolor sit amet consectetur adipisicing elit. Veniam eos fugit excepturi nulla distinctio quasi dolorum sed voluptatem temporibus id eligendi quaerat, quibusdam fuga minus iure magni ut neque cupiditate blanditiis natus repellendus ab dolorem? Blanditiis quisquam, error porro omnis ad reprehenderit explicabo incidunt. Nesciunt, at rerum? Officiis, quibusdam nesciunt quas placeat debitis ratione delectus voluptatibus eaque ullam, doloribus nisi beatae doloremque iure cupiditate, minima tenetur adipisci? Sint consectetur temporibus sit beatae cumque nam distinctio!
<div align="center">

<<<< Video Place Holder - Updating T3D GN Presets >>>>
  <!-- A Video about How to update T3D GN Presets-->
  </div>
<br>
  <!-- A short desciption -->
- Lorem ipsum, dolor sit amet consectetur adipisicing elit. Ea facilis maiores dolor vel dolore! Dolorum praesentium harum perferendis atque doloremque quam rerum sapiente officiis. Labore quia repudiandae obcaecati dignissimos. Laboriosam ipsa omnis quidem quasi, maiores fuga dolor magni ad ratione? Facilis pariatur facere quaerat aspernatur deleniti dolorem, corporis nemo eveniet!

# Release Notes:
- T3D-GN-Presets (v1.0.1) is currently in Alpha. Find older version release notes [here]().     
- [Hyperlinks]() are set to `Experimental` Branch contents. 
- [Corrective Release]() has been introduced for minor fixes.

# Core:
- Complete Restructuring of [ `_init_.py` ]() which packs more information to developers such as Licence, Previous updates and further improvements.
- Removed unfinished/ unreleased features.
- Maintained lowercase and relative paths 
- Replaced Popover with only Icon `<img src="https://user-images.githubusercontent.com/106262964/191753865-f69ae775-f7cf-4075-8ac9-0d1861b9fef1.png"
width="10">`

## Performance
- Rewritten `Displacer` gains 5-10% speed and stability with a 1 Million vertex grid.
- Rewritten `UV To Mesh` is now 2-5% faster. 
- Rewritten `Align To Spline` to work with all types of splines
- Rewritten all Fields nodes to improve stability. Fixed inverted direction while transforming with empties.
- Removal of UV feature in `Sweep Curve` gains 85% increase. Supports non-cyclic curves
- Renamed & Rewritten `Reset Position` to `Center Elements` is 15% faster with Mesh, Curves, Points, Instances, Volume Combined
- Rewritten `Inset Faces` works without internal dependencies to reduce attribute storing computations  

## New Nodes & Categories :
### Nodes
- **Smooth Curve** - Curve to Bezier with smoothing
- **Prism Field** - Prism Falloff
- **Torus Field** - Torus Falloff
- **Modify Field** - Field Modifier with direct controls of the Input Field
- **Atom Array** - Generate Atom Array with Vertex and Edge Instances

### Category: SDF (Signed Distance Function)
#### Primitives:
- SDF Box
- SDF Cylinder
- SDF Ngon
- SDF Torus

#### Modifiers:
- SDF Boolean
- SDF Displacement

## New Features & Changes :
- Added *Tooltips*
- Added *Separators*
- Renamed Inputs and Outputs to make uniform across the category
- Added per Mesh island control and Selection to `Center Elements`
- Added Bound Center in `Center Elements` for faster computation
- Renamed `Manifold Edge Selection` to `Non-Manifold Edge Selection` with Non-Manifold Edge Selection Output
- Added Global strength with Axis Controls for `Displacer` Now Supports Geometry without Generic Normal Attribute
- Made _Center at Origin_ as default in Point and Curve Primitives
- Added Invert in `Transforms To Position and Vector Mapping` 
- Added and corrected Offset Output in `Center Elements` & `Rotate Elements`
- Added Support for *Geometry Type: Volume* in `Instancers`
- `Poke Faces` now outputs New Vertices Selection
- Fixed `Spherify` to maintain Face Area
- Corrected inverted scale in `Transforms to Position`

##  Breaking Changes:
- Removed UV from `Sweep Curve`
- Reset Position renamed to `Center Elements`
- Fields are made Scale-based instead of size-based

</details>

#### Corrective Releases:
- As of now, there are no updates regarding corrective Releases, bug reports will be viewed and resolved as soon as possible.
- Minor fixes will be directly committed from `Experimental` → `Master` apart from [Release]()
- Substantial fixes will be released directly replacing the Main Release as Corrective Release.

# Development:
- Developments are happening on daily basis in [Experimental]() Branch regarding bug fixes, and support for every upcoming [Blender](https://www.blender.org/) release.
- Support for [Blender 3.4 Alpha]() is not yet started as of now. There will be a huge improvement in UI like *[Mix RGB]() , [Transfer Attribute]()*
- We will have discussions regarding the *Removal/ Renaming/ Restructuring* of nodes like `Distribute Points in Volume` , and  `Sweep Curve`.
- Plans for [Corrective Releases]()
- Plans for adding nodes as [Assets](https://developer.blender.org/rBbdb57541475f20)
- Devtalks are held on My [Discord Server]()

## :ghost: Bug Reports & Fixes
- Submit Bug reports and feature requests [here](https://github.com/Tams3d/T3D-GN-Presets/issues).
- Review file changes [here](https://github.com/Tams3d/T3D-GN-Presets/pulls).
- Fixes will be provided periodically as assured.

## Fixes

- [x] [Deformers](https://github.com/Tams3d/T3D-GN-Presets/issues/5) to work properly with `Center Elements`
- [x] [Instancers](https://github.com/Tams3d/T3D-GN-Presets/issues/6) support Geometry type: *Volume*
- [x] [UV To Mesh](https://github.com/Tams3d/T3D-GN-Presets/issues/7) gets *Generate UV* option

## Access to Source Code:

- [ `_init_.py` ]() defines the addon followed by [geonode_groups.json]() which contains a list of categories with nodes.
- [geonode_nodes.blend]() contains all the Node-groups which are displayed under `T3D GN Presets` 

# Licence:

- The node groups, including the Addon, are licensed as [GNU GPL]() - the same license as Blender uses
  * You are free for any purpose.
  * You are free to distribute unless the license is modified.
  * You can distribute changed versions.
  * What you create with This Addon is your sole property.
  * You are not allowed to change the license or introduce additional terms and conditions.

# :unicorn: About 
  - Hey! I am **Tamil Selvan**, also known as **tams_3d**. I am a 15-Year-Old Self Taught Blender Artist from **India**.
  - My Vision is to create *Free & Paid Resources* for the Blender Community, which requires complex setups provided in a simplified, effective way. I  Have 8 Months of Experience with Blender, mainly focusing on making procedural stuff with Geometry Nodes.
  
  ### 🚀 Experience
  - I have been Investing time into 2D and 3D learning and developing my skillset. I primarily use **Blender** for 3D stuff learning through Youtube Tutorials and from the awesome Blender Community.

  ### :clinking_glasses: Socials
  - Catch up with me here:
    * [Behance](https://www.behance.net/tamilselvan3d)
    * [Discord](https://discord.gg/TNgzbZCdnY)
    * [GitHub](https://github.com/Tams3d)
    * [Twitter](https://twitter.com/Tams_3d)