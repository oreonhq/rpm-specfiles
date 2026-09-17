%global source0_hash 52506935f70e247ed2777e3c65f20e86f79208c2a2d0e180ae7475daf11c96ef

# CGAL is a header-only library, with dependencies.
%global debug_package %{nil}

# Min dependencies
%global boost_version 1.74
%global qt_version 6.4
%global cmake_version 3.22

%global fullversion %{version}
#global fullversion 6.1

Name:           CGAL
Version:        6.2.1
Release:        1%{?dist}
Summary:        Computational Geometry Algorithms Library

# Automatically converted from old format: LGPLv3+ and GPLv3+ and Boost - review is highly recommended.
License:        LGPL-3.0-or-later AND GPL-3.0-or-later AND BSL-1.0
URL:            http://www.cgal.org/
Source0:        https://github.com/CGAL/cgal/releases/download/v%{fullversion}/%{name}-%{fullversion}.tar.xz

# Required devel packages.
BuildRequires: cmake >= %{cmake_version}
BuildRequires: gcc-c++
BuildRequires: gmp-devel
BuildRequires: boost-devel >= %{boost_version}
BuildRequires: mpfr-devel
BuildRequires: qt6-qtbase-devel >= %{qt_version}
BuildRequires: qt6-qtsvg-devel >= %{qt_version}
BuildRequires: qt6-qtdeclarative-devel >= %{qt_version}
BuildRequires: qt6-qttools-devel >= %{qt_version}
BuildRequires: make

%description
Libraries for CGAL applications.
CGAL is a collaborative effort of several sites in Europe and
Israel. The goal is to make the most important of the solutions and
methods developed in computational geometry available to users in
industry and academia in a C++ library. The goal is to provide easy
access to useful, reliable geometric algorithms.

%package devel
Summary:        Development files and tools for CGAL applications
Provides:       CGAL-static = %{version}-%{release}
Requires:       cmake
Requires:       boost-devel%{?_isa} >= %{boost_version}
Requires:       gmp-devel%{?_isa}
Requires:       mpfr-devel%{?_isa}
Recommends:     zlib-devel%{?_isa}
Recommends:     eigen3-devel
%description devel
Libraries for CGAL applications.
CGAL is a collaborative effort of several sites in Europe and
Israel. The goal is to make the most important of the solutions and
methods developed in computational geometry available to users in
industry and academia in a C++ library. The goal is to provide easy
access to useful, reliable geometric algorithms.
The %{name}-devel package provides the headers files and tools you may need to
develop applications using CGAL.

%package qt6-devel
Summary:        Development files and tools for CGAL applications using CGAL_qt6
Requires:       %{name}-devel = %{version}-%{release}
Requires:       qt6-qtbase-devel%{?_isa} >= %{qt_version}
Requires:       qt6-qtsvg-devel%{?_isa} >= %{qt_version}
Requires:       qt6-qtdeclarative-devel%{?_isa} >= %{qt_version}
Requires:       qt6-qttools-devel%{?_isa} >= %{qt_version}
%description qt6-devel
The %{name}-qt6-devel package provides the headers files and tools you
may need to develop applications using the CGAL_qt6 component of CGAL.

%package demos-source
BuildArch:      noarch
Summary:        Examples and demos of CGAL algorithms
Requires:       %{name}-devel = %{version}-%{release}
%description demos-source
The %{name}-demos-source package provides the sources of examples and demos of
CGAL algorithms.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{fullversion}

# Fix some file permissions
#chmod a-x include/CGAL/export/ImageIO.h

# Install README.Fedora here, to include it in %%doc
cat << 'EOF' > ./README.Fedora
Header-only
-----------
CGAL is a header-only library since version 5.0.

Packages
--------
In Fedora, the CGAL tarball is separated in several packages:
  - CGAL is empty since CGAL-5.0
  - CGAL-devel contains header files, and several files and tools needed to
  develop CGAL applications,
  - CGAL-demos-source contains the source of examples and demos of CGAL.

Documentation
-------------
Note that the CGAL documentation cannot be packaged for Fedora due to unclear
license conditions. The complete documentation in PDF and HTML is
available at http://www.cgal.org/Manual/index.html
EOF

%build

%cmake -DCGAL_DO_NOT_WARN_ABOUT_CMAKE_BUILD_TYPE=ON -DCGAL_INSTALL_LIB_DIR=%{_datadir} -DCGAL_INSTALL_DOC_DIR=
%cmake_build

%install
rm -rf %{buildroot}

%cmake_install

# Install demos and examples
mkdir -p %{buildroot}%{_datadir}/CGAL
touch -r demo %{buildroot}%{_datadir}/CGAL/
cp -a demo %{buildroot}%{_datadir}/CGAL/demo
cp -a examples %{buildroot}%{_datadir}/CGAL/examples

%check
rm -rf include/
mkdir build-example
cd build-example
cmake -L "-DCMAKE_PREFIX_PATH=%{buildroot}/usr" %{buildroot}%{_datadir}/CGAL/examples/Triangulation_2
make constrained_plus
ldd ./constrained_plus
./constrained_plus

%files devel
%license AUTHORS LICENSE LICENSE.BSL LICENSE.RFL LICENSE.LGPL LICENSE.GPL
%doc CHANGES.md README.Fedora
%{_includedir}/CGAL
%exclude %{_includedir}/CGAL/Qt
%dir %{_datadir}/CGAL
%{_datadir}/cmake/CGAL
%exclude %{_datadir}/cmake/CGAL/demo
%{_bindir}/*
%{_mandir}/man1/cgal_create_cmake_script.1.gz
%{_datadir}/CGAL/AABB_tree/
%{_datadir}/CGAL/Advancing_front_surface_reconstruction/
%{_datadir}/CGAL/Algebraic_kernel_d/
%{_datadir}/CGAL/Algebraic_kernel_for_circles/
%{_datadir}/CGAL/Algebraic_kernel_for_spheres/
%{_datadir}/CGAL/Alpha_shapes_2/
%{_datadir}/CGAL/Alpha_shapes_3/
%{_datadir}/CGAL/Alpha_wrap_2/
%{_datadir}/CGAL/Alpha_wrap_3/
%{_datadir}/CGAL/Apollonius_graph_2/
%{_datadir}/CGAL/Approximate_min_ellipsoid_d/
%{_datadir}/CGAL/Arithmetic_kernel/
%{_datadir}/CGAL/Arr_geometry_traits/
%{_datadir}/CGAL/Arr_point_location/
%{_datadir}/CGAL/Arr_rat_arc/
%{_datadir}/CGAL/Arr_spherical_gaussian_map_3/
%{_datadir}/CGAL/Arr_topology_traits/
%{_datadir}/CGAL/Arrangement_2/
%{_datadir}/CGAL/Barycentric_coordinates_2/
%{_datadir}/CGAL/Barycentric_coordinates_3/
%{_datadir}/CGAL/Boolean_set_operations_2/
%{_datadir}/CGAL/Box_intersection_d/
%{_datadir}/CGAL/CORE/
%{_datadir}/CGAL/Cartesian/
%{_datadir}/CGAL/Circular_kernel_2/
%{_datadir}/CGAL/Circular_kernel_3/
%{_datadir}/CGAL/Circulator/
%{_datadir}/CGAL/Classification/
%{_datadir}/CGAL/Combinatorial_map/
%{_datadir}/CGAL/Cone_spanners_2/
%{_datadir}/CGAL/Constrained_triangulation_3/
%{_datadir}/CGAL/Convex_decomposition_3/
%{_datadir}/CGAL/Convex_hull_2/
%{_datadir}/CGAL/Convex_hull_3/
%{_datadir}/CGAL/Curved_kernel_via_analysis_2/
%{_datadir}/CGAL/Distance_2/
%{_datadir}/CGAL/Distance_3/
%{_datadir}/CGAL/Draw_aos/
%{_datadir}/CGAL/Envelope_2/
%{_datadir}/CGAL/Envelope_3/
%{_datadir}/CGAL/Filtered_bbox_circular_kernel_2/
%{_datadir}/CGAL/Filtered_kernel/
%{_datadir}/CGAL/Frechet_distance/
%{_datadir}/CGAL/GMP/
%{_datadir}/CGAL/Generalized_map/
%{_datadir}/CGAL/Generator/
%{_datadir}/CGAL/Hash_map/
%{_datadir}/CGAL/Heat_method_3/
%{_datadir}/CGAL/Homogeneous/
%{_datadir}/CGAL/Hyperbolic_triangulation_2/
%{_datadir}/CGAL/IO/
%{_datadir}/CGAL/ImageIO/
%{_datadir}/CGAL/Installation/
%{_datadir}/CGAL/Interpolation/
%{_datadir}/CGAL/Intersections_2/
%{_datadir}/CGAL/Intersections_3/
%{_datadir}/CGAL/Isosurfacing_3/
%{_datadir}/CGAL/KSP/
%{_datadir}/CGAL/KSP_3/
%{_datadir}/CGAL/KSR_3/
%{_datadir}/CGAL/Kernel/
%{_datadir}/CGAL/Kernel_23/
%{_datadir}/CGAL/Kernel_d/
%{_datadir}/CGAL/Linear_cell_complex/
%{_datadir}/CGAL/Mesh_2/
%{_datadir}/CGAL/Mesh_3/
%{_datadir}/CGAL/Meshes/
%{_datadir}/CGAL/Min_circle_2/
%{_datadir}/CGAL/Min_ellipse_2/
%{_datadir}/CGAL/Min_sphere_d/
%{_datadir}/CGAL/Min_sphere_of_spheres_d/
%{_datadir}/CGAL/Minkowski_sum_2/
%{_datadir}/CGAL/Minkowski_sum_3/
%{_datadir}/CGAL/Modular_arithmetic/
%{_datadir}/CGAL/Nef_2/
%{_datadir}/CGAL/Nef_3/
%{_datadir}/CGAL/Nef_S2/
%{_datadir}/CGAL/NewKernel_d/
%{_datadir}/CGAL/Number_types/
%{_datadir}/CGAL/OTR_2/
%{_datadir}/CGAL/OpenGR/
%{_datadir}/CGAL/Optimal_bounding_box/
%{_datadir}/CGAL/Optimisation/
%{_datadir}/CGAL/Orthtree/
%{_datadir}/CGAL/Partition_2/
%{_datadir}/CGAL/Periodic_2_triangulation_2/
%{_datadir}/CGAL/Periodic_3_mesh_3/
%{_datadir}/CGAL/Periodic_3_triangulation_3/
%{_datadir}/CGAL/Periodic_4_hyperbolic_triangulation_2/
%{_datadir}/CGAL/Point_set_3/
%{_datadir}/CGAL/Point_set_processing_3/
%{_datadir}/CGAL/Poisson_surface_reconstruction_3/
%{_datadir}/CGAL/Polygon_2/
%{_datadir}/CGAL/Polygon_mesh_processing/
%{_datadir}/CGAL/Polygon_repair/
%{_datadir}/CGAL/Polygonal_surface_reconstruction/
%{_datadir}/CGAL/Polyline_simplification_2/
%{_datadir}/CGAL/Polynomial/
%{_datadir}/CGAL/QP_solver/
%{_datadir}/CGAL/Qt/
%{_datadir}/CGAL/SMDS_3/
%{_datadir}/CGAL/STL_Extension/
%{_datadir}/CGAL/Scale_space_reconstruction_3/
%{_datadir}/CGAL/Segment_Delaunay_graph_2/
%{_datadir}/CGAL/Segment_Delaunay_graph_Linf_2/
%{_datadir}/CGAL/Set_movable_separability_2/
%{_datadir}/CGAL/Shape_detection/
%{_datadir}/CGAL/Shape_regularization/
%{_datadir}/CGAL/Spatial_searching/
%{_datadir}/CGAL/Spatial_sorting/
%{_datadir}/CGAL/Sqrt_extension/
%{_datadir}/CGAL/Straight_skeleton_2/
%{_datadir}/CGAL/Stream_support/
%{_datadir}/CGAL/Subdivision_method_3/
%{_datadir}/CGAL/Surface_mesh/
%{_datadir}/CGAL/Surface_mesh_approximation/
%{_datadir}/CGAL/Surface_mesh_parameterization/
%{_datadir}/CGAL/Surface_mesh_segmentation/
%{_datadir}/CGAL/Surface_mesh_shortest_path/
%{_datadir}/CGAL/Surface_mesh_simplification/
%{_datadir}/CGAL/Surface_mesh_skeletonization/
%{_datadir}/CGAL/Surface_mesh_topology/
%{_datadir}/CGAL/Surface_mesher/
%{_datadir}/CGAL/Surface_sweep_2/
%{_datadir}/CGAL/TDS_2/
%{_datadir}/CGAL/TDS_3/
%{_datadir}/CGAL/Tetrahedral_remeshing/
%{_datadir}/CGAL/Three/
%{_datadir}/CGAL/Triangulation/
%{_datadir}/CGAL/Triangulation_2/
%{_datadir}/CGAL/Triangulation_3/
%{_datadir}/CGAL/Triangulation_on_sphere_2/
%{_datadir}/CGAL/Visibility_2/
%{_datadir}/CGAL/Voronoi_diagram_2/
%{_datadir}/CGAL/Weights/
%{_datadir}/CGAL/auto_link/
%{_datadir}/CGAL/boost/
%{_datadir}/CGAL/constructions/
%{_datadir}/CGAL/export/
%{_datadir}/CGAL/internal/
%{_datadir}/CGAL/license/
%{_datadir}/CGAL/pointmatcher/
%{_datadir}/CGAL/predicates/
%{_datadir}/CGAL/type_traits/
%files qt6-devel
%{_includedir}/CGAL/Qt
%{_datadir}/cmake/CGAL/demo

%files demos-source
%{_datadir}/CGAL/demo
%{_datadir}/CGAL/examples
%exclude %{_datadir}/CGAL/*/*/skip_vcproj_auto_generation

%changelog
%autochangelog
