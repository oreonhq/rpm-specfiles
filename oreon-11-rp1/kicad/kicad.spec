%global source5_hash def2208ec7e4693642c172d525652d95d7b706f3631930b7c754c559c0ad190a
%global source4_hash 17827af73192ae17b479d4c502b6f569d03ed855b9d3c0b9b133b8cf1b8d3e22
%global source3_hash 5587f5cb4a779d287e49c4ba069a6b42c27b55cbe4c5b6241e39d91878abe571
%global source2_hash 18b4e3f2ed781383179c1b15a82c94e5176dc825e1c646f84e89ed50e835063b
%global source1_hash 4ff8e568a754c6618cae907b0efdaa6eb88a4b1878c09841b88f5bc8af2ac794
%global source0_hash 528788c342461536bee3331998a8aa609975723f07b816287146ab8d4d9af3cb
Name:           kicad
Version:        10.0.6
Release:        1%{?dist}
Epoch:          1
Summary:        EDA software suite for creation of schematic diagrams and PCBs
License:        GPL-3.0-or-later
URL:            https://www.kicad.org
Source0:        https://gitlab.com/kicad/code/kicad/-/archive/%{version}/kicad-%{version}.tar.gz
Source1:        https://gitlab.com/kicad/services/kicad-doc/-/archive/%{version}/kicad-doc-%{version}.tar.gz
Source2:        https://gitlab.com/kicad/libraries/kicad-templates/-/archive/%{version}/kicad-templates-%{version}.tar.gz
Source3:        https://gitlab.com/kicad/libraries/kicad-symbols/-/archive/%{version}/kicad-symbols-%{version}.tar.gz
Source4:        https://gitlab.com/kicad/libraries/kicad-footprints/-/archive/%{version}/kicad-footprints-%{version}.tar.gz
Source5:        https://gitlab.com/kicad/libraries/kicad-packages3D/-/archive/%{version}/kicad-packages3D-%{version}.tar.gz
ExclusiveArch:  x86_64 aarch64 ppc64le
Provides:       bundled(fmt) = 9.0.0
Provides:       bundled(libdxflib) = 3.26.4
Provides:       bundled(polyclipping) = 6.4.2
Provides:       bundled(potrace) = 1.15
%if %{undefined flatpak}
Requires:       electronics-menu
%endif
Requires:       libgit2
Requires:       libngspice
Requires:       libsecret
Requires:       libspnav
Requires:       ngspice-codemodel
Requires:       protobuf
Requires:       python3-wxpython4
Requires:       unixODBC
Suggests:       kicad
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  glew-devel
BuildRequires:  glm-devel
BuildRequires:  gtk3-devel
BuildRequires:  libappstream-glib
BuildRequires:  libcurl-devel
BuildRequires:  libgit2-devel
BuildRequires:  libngspice-devel
BuildRequires:  libsecret-devel
BuildRequires:  libspnav-devel
BuildRequires:  libzstd-devel
BuildRequires:  make
BuildRequires:  nng-devel
BuildRequires:  opencascade-devel
BuildRequires:  po4a
BuildRequires:  poppler-glib-devel
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  python3-devel
BuildRequires:  python3-wxpython4
BuildRequires:  rubygem-asciidoctor
BuildRequires:  shared-mime-info
BuildRequires:  swig
BuildRequires:  unixODBC-devel
BuildRequires:  wxGTK-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
KiCad is EDA software to design electronic schematic
diagrams and printed circuit board artwork of up to
32 layers.

%package        packages3d
Summary:        3D Models for KiCad
License:        CC-BY-SA-4.0
BuildArch:      noarch
Requires:       kicad >= 10.0.6
%description    packages3d
3D Models for KiCad.

%package        doc
Summary:        Documentation for KiCad
License:        GPL-3.0-or-later or CC-BY-3.0
BuildArch:      noarch
%description    doc
Documentation for KiCad.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a 1 -a 2 -a 3 -a 4 -a 5

%build

%cmake \
    -DKICAD_IPC_API=ON \
    -DKICAD_SCRIPTING_WXPYTHON=ON \
    -DKICAD_INSTALL_DEMOS=ON \
    -DKICAD_BUILD_QA_TESTS=OFF \
    -DKICAD_BUILD_I18N=ON \
    -DKICAD_I18N_UNIX_STRICT_PATH=ON \
    -DKICAD_USE_CMAKE_FINDPROTOBUF=ON \
    -DKICAD_VERSION_EXTRA=%{release} \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DOCC_INCLUDE_DIR=%{_includedir}/opencascade \
    -DOCC_LIBRARY_DIR=%{_libdir} \
    -DPYTHON_SITE_PACKAGE_PATH=%{python3_sitearch}
%cmake_build
pushd %{name}-templates-%{version}/
%cmake
%cmake_build
popd
pushd %{name}-symbols-%{version}/
%cmake \
    -DKICAD_PACK_SYM_LIBRARIES=ON
%cmake_build
popd
pushd %{name}-footprints-%{version}/
%cmake
%cmake_build
popd
pushd %{name}-packages3D-%{version}/
%cmake
%cmake_build
popd
pushd %{name}-doc-%{version}/
%cmake \
    -DPDF_GENERATOR=none \
    -DBUILD_FORMATS=html
%cmake_build -j1
popd
%install
%cmake_install
for desktopfile in %{buildroot}%{_datadir}/applications/*.desktop ; do
  desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  --delete-original                          \
  ${desktopfile}
done
pushd %{name}-templates-%{version}/
%cmake_install
cp -p LICENSE.md ../LICENSE-templates.md
popd
pushd %{name}-symbols-%{version}/
%cmake_install
cp -p LICENSE.md ../LICENSE-symbols.md
popd
pushd %{name}-footprints-%{version}/
%cmake_install
cp -p LICENSE.md ../LICENSE-footprints.md
popd
pushd %{name}-packages3D-%{version}/
%cmake_install
popd
pushd %{name}-doc-%{version}/
%cmake_install
popd
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n kicad-packages3d -f %{oreon_filedir}/kicad-packages3d.list
%files -n kicad-doc -f %{oreon_filedir}/kicad-doc.list

%changelog

%autochangelog
