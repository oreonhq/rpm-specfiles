%global source0_hash 1f7246ed0ac5a223b84a525f675d5242199b549a43a2bd741fe491b2afc21b25

%undefine __cmake_in_source_build
%global commit0 44cb7c6eae4488f921041572908f3af508880547

Name:           glues
Version:        1.5
Release:        16.20200105git44cb7c6%{?dist}
Summary:        GLU port for OpenGL ES

# SGI FREE SOFTWARE LICENSE B (Version 2.0, Sept. 18, 2008)
License:        MIT
URL:            https://github.com/lunixbochs/%{name}
Source0:        %{url}/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz

BuildRequires:  cmake gcc-c++
# TODO check compatibility for SDL 1.2+ currently in rawhide
BuildRequires:  SDL2-devel
BuildRequires:  mesa-libGL-devel

%description
This port is based on original GLU 1.3 and has original libutil, libtess and
nurbs libraries.

%package devel
Summary:        Development files for GLUES
Requires:       %{name}%{?_isa} = %{version}

%description devel
%summary.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n%{name}-%{commit0}
# rename so to avoid conflicts
sed -i 's,GLU ,GLUES ,' CMakeLists.txt
# skip nurbs
find source/libnurbs -type d -print -exec rm -rv '{}/*' \;

%build
# TODO: Please submit an issue to upstream (rhbz#2380618)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build

%install
mkdir -p %{buildroot}%{_libdir}
install -p %{_vpath_builddir}/libGLUES.so* %{buildroot}%{_libdir}
ln -s libGLUES.so.* %{buildroot}%{_libdir}/libGLUES.so
mkdir -p %{buildroot}%{_includedir}/%{name}
cp -pr source/*.h %{buildroot}%{_includedir}/%{name}

%files
%license LICENSE
%doc README docs/*
%{_libdir}/lib*.so.1

%files devel
%license LICENSE
%doc sdltests/
%{_libdir}/libGLUES.so
%{_includedir}/%{name}/

%changelog
%autochangelog
