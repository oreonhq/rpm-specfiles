%global source0_hash 9d22e65bdd6a125ac2043350a019ec4346ea83922cafdf47e125a03c16f6fa07
%global major_version 11
%global minor_version 0
%global patch_version 0
%global pkg_version %{major_version}.%{minor_version}.%{patch_version}
%global short_version %{major_version}.%{minor_version}
Name:           OpenMesh
Version:        %{pkg_version}
Release:        1%{?dist}
Summary:        A generic and efficient polygon mesh data structure
License:        BSD-3-Clause
URL:            http://www.openmesh.org/
Source0:        https://www.graphics.rwth-aachen.de/media/openmesh_static/Releases/%{short_version}/%{name}-%{version}.tar.bz2
Source1:        README.Fedora
Patch0:         OpenMesh-11.0.0-gtest.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  eigen3-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  gtest-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  rdfind
BuildRequires:  symlinks
BuildRequires:  texlive-dvips-bin
BuildRequires:  texlive-latex-bin
BuildRequires:  texlive-makeindex-bin
BuildRequires:  texlive-newunicodechar
# /oreon:deps
%description
OpenMesh is a generic and efficient data structure for representing
and manipulating polygonal meshes.

%package devel
Summary:        Development headers and libraries for OpenMesh
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains development headers and libraries necessary to
compile programs against OpenMesh.

%package doc
Summary:        Doxygen documentation for OpenMesh
BuildArch:      noarch
%description doc
This package contains the Doxygen documentation for OpenMesh.

%package tools
Summary:        OpenMesh tools
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description tools
This package contains the applications that ship with OpenMesh.

%global OpenMesh_apps Analyzer commandlineAdaptiveSubdivider commandlineDecimater commandlineSubdivider DecimaterGui Dualizer mconvert mkbalancedpm ProgViewer QtViewer Smoothing SubdividerGui Synthesizer

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch 0 -p1 -b .gtest
cp -p %{SOURCE1} .

# Generate desktop files
for xb in %{OpenMesh_apps}; do
    cat > om_${xb}.desktop <<EOF
[Desktop Entry]
Name=OpenMesh $xb
Exec=%{_libdir}/%{name}/$xb
Terminal=false
Type=Application
StartupNotify=true
Categories=Utility;Science
EOF
done

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%{cmake} -DCMAKE_BUILD_TYPE=RELEASE -DQT_VERSION=6 -DOPENMESH_BUILD_UNIT_TESTS=ON \
%if "%{?_lib}" == "lib64"
    %{?_cmake_lib_suffix64} \
%endif
%{cmake_build}
%{cmake_build} -t doc
rdfind -makesymlinks true %{_vpath_builddir}/Build/share/OpenMesh/Doc/html
symlinks -rc %{_vpath_builddir}/Build/share/OpenMesh/Doc/html
%check

%ifnarch s390x
%ctest -j1 # Run tests sequentially to avoid I/O conflicts
%endif
%install
%cmake_install
rm %{buildroot}%{_libdir}/*.a
rm %{buildroot}%{_bindir}/unittests*
mkdir -p %{buildroot}%{_libdir}/pkgconfig
mv %{buildroot}/*/*/pkgconfig/openmesh.pc %{buildroot}%{_libdir}/pkgconfig/openmesh.pc
mkdir -p %{buildroot}%{_libdir}/cmake/OpenMesh
mv %{buildroot}/%{_datadir}/OpenMesh/cmake/OpenMeshConfig*cmake %{buildroot}%{_libdir}/cmake/OpenMesh/
mkdir -p %{buildroot}%{_libdir}/%{name}
mv %{buildroot}%{_bindir}/* %{buildroot}%{_libdir}/%{name}/
pushd %{buildroot}%{_libdir}/%{name}/
for b in *; do
    ln -s ../%{_lib}/%{name}/$b %{buildroot}%{_bindir}/om_$b
done
popd
touch tools-files.txt
for xb in %{OpenMesh_apps}; do
    desktop-file-install --dir=%{buildroot}%{_datadir}/applications om_${xb}.desktop
    echo "%{_libdir}/%{name}/$xb" >> tools-files.txt
    echo "%{_bindir}/om_$xb" >> tools-files.txt
    echo "%{_datadir}/applications/om_${xb}.desktop" >> tools-files.txt
done
%ldconfig_scriptlets
%oreon_autofiles OpenMesh-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles OpenMesh-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles OpenMesh-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n OpenMesh-devel -f %{oreon_filedir}/OpenMesh-devel.list
%files -n OpenMesh-doc -f %{oreon_filedir}/OpenMesh-doc.list
%files -n OpenMesh-tools -f %{oreon_filedir}/OpenMesh-tools.list

%changelog

%autochangelog
