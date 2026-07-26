%global source0_hash d22b66eb13b92513c7736cc5e867fed40b25a0e398a70aa059711fc4f4769363

%undefine __cmake_in_source_build
%global commit dfbe3d2cd21d3d88d7ba9de39cfc8aa901a6041b
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           wiiuse
Version:        0.15.5
Release:        17%{?dist}
Summary:        The wiiuse library is used to access and control multiple Nintendo Wiimotes
License:        GPL-3.0-or-later
URL:            https://github.com/rpavlik/wiiuse
Source0:        https://github.com/rpavlik/wiiuse/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  bluez-libs-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  freeglut-devel
BuildRequires:  SDL-devel
BuildRequires:  dos2unix
BuildRequires:  cmake
BuildRequires:  /usr/bin/chrpath

%description
A library that implements access to wiiremote controllers via bluetooth.

%package devel
Summary: Developer tools for the wiiuse library
Requires: bluez-libs-devel
Requires: wiiuse = %{version}-%{release}

%description devel
Header files needed to develop programs that link against the wiiuse library.

%package examples
Summary: Example programs for the wiiuse library
Requires: wiiuse = %{version}-%{release}

%description examples
Example programs to test accessing wiiremote controllers

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0

#Convert all relevant files to unix charset
for i in CHANGELOG.mkd README.mkd; do dos2unix $i; done
for i in example*/*; do dos2unix $i; done
for i in src/*; do dos2unix $i; done

%build
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install
# Can't use make install as it is a pathetic copy into fixed paths and won't
# work on x86_64
install -Dpm 0755 %{_vpath_builddir}/src/libwiiuse.so %{buildroot}%{_libdir}/libwiiuse.so.0
ln -s libwiiuse.so.0 %{buildroot}%{_libdir}/libwiiuse.so
install -Dpm 0644 src/wiiuse.h %{buildroot}%{_includedir}/wiiuse.h
install -Dpm 0755 %{_vpath_builddir}/example/wiiuseexample %{buildroot}%{_bindir}/wiiuseexample
install -Dpm 0755 %{_vpath_builddir}/example-sdl/wiiuseexample-sdl %{buildroot}%{_bindir}/wiiuseexample-sdl
chrpath -d %{buildroot}%{_bindir}/wiiuseexample*

%files
%{_libdir}/libwiiuse.so.0
%license LICENSE
%doc CHANGELOG.mkd README.mkd

%files devel
%{_includedir}/wiiuse.h
%{_libdir}/libwiiuse.so

%files examples
%doc example/example.c example-sdl/sdl.c
%{_bindir}/wiiuseexample
%{_bindir}/wiiuseexample-sdl

%ldconfig_scriptlets

%changelog
%autochangelog
