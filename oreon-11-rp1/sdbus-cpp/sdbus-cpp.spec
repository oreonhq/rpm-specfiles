%global source0_hash 3a289eded586c26d06c1387de72c7bf7c809527a70d51ba6401fe61059b19626
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: sdbus-cpp
Version: 2.3.1
Release: 1%{?dist}
Summary: High-level C++ D-Bus library
License: LGPL-2.1-or-later WITH Sdbus-C++ exception
URL: https://github.com/Kistler-Group/sdbus-cpp
Source0: https://github.com/Kistler-Group/sdbus-cpp/archive/v%{version}/sdbus-cpp-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: gcc-c++
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: patchelf
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: systemd-devel
BuildRequires: pkgconf
%endif

%description
sdbus-c++ is a high-level C++ D-Bus library built on sd-bus.

%package devel
Summary: Development files for sdbus-cpp
Requires: sdbus-cpp%{?_isa} = %{version}-%{release}
Provides: pkgconfig(sdbus-c++)
Provides: cmake(sdbus-c++)

%description devel
Headers and libraries for developing against sdbus-cpp.

%prep
%oreon_sha256
%autosetup -n sdbus-cpp-%{version} -p1

%build
%oreon_cmake -DSDBUSCPP_BUILD_DOCS=OFF -DSDBUSCPP_BUILD_TESTS=OFF -DSDBUSCPP_BUILD_CODEGEN=OFF -DSDBUSCPP_BUILD_EXAMPLES=OFF
%oreon_cmake_build

%install
%oreon_cmake_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f" 2>/dev/null || true)
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
