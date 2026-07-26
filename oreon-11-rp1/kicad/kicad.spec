%global source0_hash 3d188b0c1cda84dfa11ef9e6bbf4cb5b509ba68555bd6e4d8d7224ddd1112880

Name:           kicad
Version:        10.0.0
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

# https://gitlab.com/kicad/code/kicad/-/issues/237
ExclusiveArch:  x86_64 aarch64 ppc64le

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
BuildRequires:  poppler-glib-devel
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  python3-devel
BuildRequires:  python3-wxpython4
BuildRequires:  shared-mime-info
BuildRequires:  swig
BuildRequires:  unixODBC-devel
BuildRequires:  wxGTK-devel
BuildRequires:  zlib-devel

# Documentation
BuildRequires:  po4a
BuildRequires:  rubygem-asciidoctor

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

%description
KiCad is EDA software to design electronic schematic
diagrams and printed circuit board artwork of up to
32 layers.

%package        packages3d
Summary:        3D Models for KiCad
License:        CC-BY-SA-4.0
BuildArch:      noarch
Requires:       kicad >= 10.0.0

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

# KiCad application
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

# Templates
pushd %{name}-templates-%{version}/
%cmake
%cmake_build
popd

# Symbol libraries
pushd %{name}-symbols-%{version}/
%cmake \
    -DKICAD_PACK_SYM_LIBRARIES=ON
%cmake_build
popd

# Footprint libraries
pushd %{name}-footprints-%{version}/
%cmake
%cmake_build
popd

# 3D models
pushd %{name}-packages3D-%{version}/
%cmake
%cmake_build
popd

# Documentation (HTML only)
pushd %{name}-doc-%{version}/
%cmake \
    -DPDF_GENERATOR=none \
    -DBUILD_FORMATS=html
%cmake_build -j1
popd

%install

# KiCad application
%cmake_install

# Install desktop
for desktopfile in %{buildroot}%{_datadir}/applications/*.desktop ; do
  desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  --delete-original                          \
  ${desktopfile}
done

# Templates
pushd %{name}-templates-%{version}/
%cmake_install
cp -p LICENSE.md ../LICENSE-templates.md
popd

# Symbol libraries
pushd %{name}-symbols-%{version}/
%cmake_install
cp -p LICENSE.md ../LICENSE-symbols.md
popd

# Footprint libraries
pushd %{name}-footprints-%{version}/
%cmake_install
cp -p LICENSE.md ../LICENSE-footprints.md
popd

# 3D models
pushd %{name}-packages3D-%{version}/
%cmake_install
popd

# Documentation
pushd %{name}-doc-%{version}/
%cmake_install
popd

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files -f %{name}.lang
%doc AUTHORS.txt
%attr(0755, root, root) %{_bindir}/*
%{_libdir}/%{name}/
%{_libdir}/libkiapi.so*
%{_libdir}/libkicad_3dsg.so*
%{_libdir}/libkigal.so*
%{_libdir}/libkicommon.so*
%{python3_sitearch}/_pcbnew.so
%pycached %{python3_sitearch}/pcbnew.py
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/bash-completion/completions/*
%{_datadir}/icons/hicolor/*/apps/*.*
%{_datadir}/icons/hicolor/*/mimetypes/application-x-*.*
%{_datadir}/mime/packages/*.xml
%{_datadir}/zsh/site-functions/*
%{_metainfodir}/*.metainfo.xml
%license LICENSE*
%exclude %{_datadir}/%{name}/3dmodels/*

%files packages3d
%{_datadir}/%{name}/3dmodels/*.3dshapes
%license %{name}-packages3D-%{version}/LICENSE*

%files doc
%{_docdir}/%{name}/help/
%exclude %{_docdir}/%{name}/AUTHORS.txt
%license %{name}-doc-%{version}/LICENSE*

%changelog
%autochangelog
