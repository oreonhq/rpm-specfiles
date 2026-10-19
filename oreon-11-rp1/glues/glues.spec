%global source0_hash 1f7246ed0ac5a223b84a525f675d5242199b549a43a2bd741fe491b2afc21b25
%undefine __cmake_in_source_build
%global commit0 44cb7c6eae4488f921041572908f3af508880547
Name:           glues
Version:        1.5
Release:        1%{?dist}
Summary:        GLU port for OpenGL ES
License:        MIT
URL:            https://github.com/lunixbochs/%{name}
Source0:        https://github.com/lunixbochs/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  mesa-libGL-devel
# /oreon:deps
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

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build
%install
mkdir -p %{buildroot}%{_libdir}
install -p %{_vpath_builddir}/libGLUES.so* %{buildroot}%{_libdir}
ln -s libGLUES.so.* %{buildroot}%{_libdir}/libGLUES.so
mkdir -p %{buildroot}%{_includedir}/%{name}
cp -pr source/*.h %{buildroot}%{_includedir}/%{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n glues-devel -f %{oreon_filedir}/glues-devel.list

%changelog

%autochangelog
