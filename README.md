# T3D-Geo-Node-Presets
## A Collection of Incredibly useful nodes for Geometry Nodes - Blender 3.2 & above

![T3D GN Presets](https://user-images.githubusercontent.com/106262964/173188615-21216a7b-6e8b-4319-bf33-954b940ac4b5.png)

## :bulb: Introduction

- **T3D GN Presets** is designed to solve basic operations which require much more complex node trees and time-consuming processes with a simple **easy-to-use solution**. We assure to provide constant updates, bug fixes and support for every newest Blender Stable Releases. This Addon Will evolve many new changes over time with performance, customizability, and user requests as the main key. 
- Tams 3d's Geo-Node Presets Add-on is located at `Geometry Node Editor > Add > T3D's Presets` - with separate categories based on uses. Requested Users to read [Licence & Files](https://github.com/Tams3d/T3D-GN-Presets/edit/Development/README.md#licencing--files) before sharing files and intend to modify. 
- The Addon Stability & Releases are being defined by the [Changelogs](https://github.com/Tams3d/T3D-GN-Presets/edit/Master/README.md#magic_wand-changelogs) Version.
  - For example, 
    - Version 1.0.0 - New Release (Stable/ LTS)
    - Version 1.1.0/ 1.2.0 - Bug Fixes, Potential changes & Performances Improvements In Node-groups (may update frequently)
    - Version 0.0.1-E / 0.1.0-E - Beta/Alpha Releases (experimental purposes in [Experimental Branch ](https://github.com/Tams3d/T3D-GN-Presets/tree/Experimental) )
    -  :green_circle: - Stable
    -  :large_blue_circle: - Release Candidate/Older Version
    -  :yellow_circle: - Beta
    -  :red_circle: - Alpha


## :magic_wand: Changelogs & Release Notes

  ### Version 1.0.0 :green_circle:

  - **T3D GN Presets** Turns into Addon with Node-groups for quick navigation and abolished Append Fake-user Method from Pre-Alpha Release
  - Added Popover at Geometry Node Editor - Header which contains:
     * [Changelogs](https://github.com/Tams3d/T3D-GN-Presets/edit/Master/README.md#magic_wand-changelogs)
     * [Example Files](https://discord.gg/eKdswfAS)
     * [Report A Bug](https://github.com/Tams3d/T3D-GN-Presets/issues)

  - Added Support for Splines, Meshes, Instances, Points to `Deformers`
  - Added Additional Support for Splines, Meshes, Points as Outputs for `Primitives`
  - Added Adaptive Point Radius based on Geometry Resolution & Count for `Points` Outputs

## :infinity: Github Repository Changes

  - Added `Experimental` Branch
  - Added `Development` Branch
  - Branches are allocated based on usability and developments.
    * [Master](https://github.com/Tams3d/T3D-GN-Presets/tree/Master) - New Releases with major changes and added Support.
    * [LTS]() - Long Term Support Based on Blender LTS Releases and production-ready. (:warning: Work-In-Process)
    * [Experimental](https://github.com/Tams3d/T3D-GN-Presets/tree/Experimental) - Most Frequent Updates, have the latest features and while there might be bug fixes too, they are unstable.
    * [Developement](https://github.com/Tams3d/T3D-GN-Presets/tree/Development) - Contains Incomplete codes, To-do works, preview checks. (Not Intended For Public Use, Strictly Only for Developers)
   - Commits with completed changes will be moved from the `Development` Branch to the `Experimental` Branch after Verification.
   - `Experimental` Branch has upcoming developments which are expected to come in the `Master`
   - Commits for `LTS` should be labelled and tested intensively to avoid conflicts. These Commits are allowed to be Developed in `LTS` Branch via Pull requests.

## :link: Updates & Restrictions

- Our Presets are made only to run on Latest Stable Blender Release as of date - Blender 3.2 & Above are supported.
- Due to the Introduction of [Named Attributes System](https://developer.blender.org/T91742) most of the Node-groups contain Named Attributes for faster computation and simplicity, older versions of Blender will not be supported and will not get supported.
- Special `LTS` branches can be added on the release of Blender 3.3 & Blender 3.7 which will require much faster, error-free, most customizable options and need separate attention.
- Experimental Branch Content usages are AT YOUR OWN RISK! MAY CAUSE SIGNIFICANT LOSS AND INCOMPATIBILITY!
- Older Addon versions Will be discontinued after Alpha versions of the addons are released.
- Updates will be provided frequently as-soon-as-possible for free 


# Licencing & Files
 ## :page_facing_up: Licence

  The Node-groups and the addon are licensed as GNU GPL - the same license as Blender uses.
  * The node groups including the addon are licensed as GNU GPL - the same license as Blender uses.
  * You are free for any purpose.
  * You are free to distribute.
  * You can distribute changed versions.
  * What you create with This Addon is your sole property.
  * You are not allowed to change the license or introduce additional terms and conditions.

## :open_file_folder: Files & Source Code
  
  - [init.py]() Contains the python code for the Addon. (Not made for readability, May get updated soon)
  - The [geonode_nodes.blend]() Contains All the Node-groups as Fake-User :shield: which is being appended by the Addon. Requested not to edit any name, `tams3d` -    GeometryNodeTree is the only supported Node-tree for the Addon as of the version, changes may bring errors.
  - The [geonode_nodes.json]() Contains the actual work of the menus and submenus with names of the Node-groups. 
  - All these files follow the same [Licence](https://github.com/Tams3d/T3D-GN-Presets/edit/Development/README.md#licence).


# Bug Reports & Fixes
  ## :ghost: Bug Reports
  - Bug reports can be done with [here](https://github.com/Tams3d/T3D-GN-Presets/issues/new).
  - It can be viewed at [Issuses](https://github.com/Tams3d/T3D-GN-Presets/issues/).
  
  ## :bug: Bug Fixes
  - Create a [Pull Request](https://github.com/Tams3d/T3D-GN-Presets/pulls) with changes and details about changes.
  - Labels will be added based on the Type of Bug.

  ## :mag: Known Issues
  - **Set Geometry Size** does not Support Instances.
  - **UV To Mesh** only works with Uv-ed Meshes without any transformations before it.
  - `Deformers` works different when Geometry is Transformed before it.
  - **Displacer** strength is based on-axis and normal, Custom normals aren't supported yet.
 
 
 # :unicorn: About 
  - Hey! I am **Tamil Selvan** also known as **tams_3d**. I am a 15-Year-Old Self Taught Blender Artist from India.
  - My Vision is to create *Free & Paid Resources* for the Blender Community which does complex task or require complex setups in a simplified effective way. Have 7 Months of Experience with Blender. I mainly focus on making procedural stuff with Geometry Nodes which can also be edited procedurally and which require minimum manual tweaks. 
  - Catch up with me here: 
    * [Behance](https://www.behance.net/tamilselvan3d)
    * [Discord](https://discord.gg/TNgzbZCdnY)
    * [Twitter](https://twitter.com/Tams_3d)
