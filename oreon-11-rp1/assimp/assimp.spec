# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 9679fe40fce2966a46528f4aff65ed5fedd25a7dbad8c5a067f666f7f9fdf5c6
%global source1_hash 5189a7b617875253eddd7c3faeab6267999b621ea1d6ca51214ec2a332efe9d1
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%define soversion 6

Name:           assimp
Version:        6.0.6
Release:        1%{?dist}
Summary:        Library to import various 3D model formats into applications

License:        BSD-3-Clause AND MIT AND BSL-1.0 AND Unlicense AND Zlib
URL:            https://github.com/assimp/assimp

Source0:        %{name}-%{version}-free.tar.xz
Source1:        assimp_generate_tarball.sh

Patch0:         %{name}-unbundle.patch
Patch1:         %{name}-pythonpath.patch
Patch2:         %{name}-nozlib.patch
Patch3:         %{name}-docs.patch
Patch4:         %{name}-tests.patch
Patch5:        CVE-2026-19967.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  earcut-hpp-devel
BuildRequires:  gtest-devel
BuildRequires:  make
BuildRequires:  pkgconfig(python3)
BuildRequires:  poly2tri-devel
BuildRequires:  pugixml-devel
BuildRequires:  python3-devel
BuildRequires:  zlib-devel
BuildRequires:  rapidjson-devel
BuildRequires:  rapidjson-static
BuildRequires:  stb_image-devel
BuildRequires:  stb_image-static
BuildRequires:  utf8cpp-devel
BuildRequires:  utf8cpp-static

Provides: bundled(polyclipping) = 4.8.8
Provides: bundled(open3dgc)
Provides: bundled(openddl-parser)
Provides: bundled(unzip)
Provides: bundled(minzip)

%description
Assimp, the Open Asset Import Library, is a free library to import
various well-known 3D model formats into applications.  Assimp aims
to provide a full asset conversion pipeline for use in game
engines and real-time rendering systems, but is not limited
to these applications.

%package devel
Summary: Header files and libraries for assimp
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: poly2tri-devel
Requires: pugixml-devel
Requires: zlib-devel

%description devel
This package contains the header files and libraries
for assimp. If you would like to develop programs using assimp,
you will need to install assimp-devel.

%package -n python3-%{name}
Summary: Python 3 bindings for assimp
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description -n python3-%{name}
This package contains the PyAssimp3 python bindings

%package doc
Summary: Assimp documentation
BuildArch: noarch

%description doc
%{summary}.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup -p1 -n %{name}-%{version}
find contrib/ -maxdepth 1 -mindepth 1 \
  | grep -Ev '(clipper|Open3DGC|openddlparser|tinyusdz|unzip|zip)' \
  | xargs rm -r

mv contrib/openddlparser/LICENSE contrib/openddlparser/LICENSE.openddlparser

%build
%cmake \
%ifarch s390x ppc64
 -DAI_BUILD_BIG_ENDIAN=TRUE \
%endif
 -DASSIMP_WARNINGS_AS_ERRORS=OFF \
 -DASSIMP_BUILD_ASSIMP_TOOLS=ON \
 -DASSIMP_BUILD_DOCS=ON \
 -DASSIMP_IGNORE_GIT_HASH=ON \
 -DHAVE_POLY2TRI=ON \
 -DPOLY2TRI_INCLUDE_PATH=%{_includedir}/poly2tri \
 -DPOLY2TRI_LIB=poly2tri \
 -DHTML_OUTPUT=out/html \
 -DCMAKE_INSTALL_DOCDIR=%{_defaultdocdir}/%{name}

%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{python3_sitelib}/pyassimp/
install -m0644 port/PyAssimp/pyassimp/*.py %{buildroot}%{python3_sitelib}/pyassimp/

%check
exclude="utMD5Importer.importBoarMan|utMD5Importer.importBob|utMD2Importer.importDolphin|utMD2Importer.importFlag|utMD2Importer.importHorse|utQ3BSPImportExport.importerTest|utBlenderImporter.importBob|utBlenderImporter.importFleurOptonl|utPMXImporter.importTest|utXImporter.importDwarf|utDXFImporterExporter.importRifle|utX3DImportExport.importX3DChevyTahoe|ut3DSImportExport.importGranate|ut3DSImportExport.importJeep1|ut3DSImportExport.importMp5Sil|ut3DSImportExport.importMarRifle|ut3DSImportExport.importPyramob|ut3DImportExport.importMarRifle|ut3DImportExport.importMarRifleA|ut3DImportExport.importMarRifleD|ut3DSImportExport.importCartWheel"
%ctest --exclude-regex $exclude

%files
%license LICENSE
%license contrib/clipper/License.txt
%license contrib/openddlparser/LICENSE.openddlparser
%license contrib/zip/UNLICENSE
%doc Readme.md CREDITS
%{_bindir}/assimp
%{_libdir}/libassimp.so.6
%{_libdir}/libassimp.so.6.0.6

%files devel
%{_includedir}/assimp/
%{_libdir}/libassimp.so
%{_libdir}/pkgconfig/assimp.pc
%{_libdir}/cmake/assimp-*/

%files doc
%{_docdir}/*

%files -n python3-%{name}
%doc port/PyAssimp/README.md
%{python3_sitelib}/pyassimp/

%changelog
%autochangelog
