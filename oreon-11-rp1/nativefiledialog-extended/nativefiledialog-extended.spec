%global source0_hash 38116050495cd7de77a91d6d8d59c1aa0a0848c56daa60029bd5b59f3c897229
Name:           nativefiledialog-extended
Version:        1.4.0
Release:        1%{?dist}
Summary:        Native file dialog library with C and C++ bindings
License:        Zlib
URL:            https://github.com/btzy/nativefiledialog-extended
Source0:        https://github.com/btzy/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel
# /oreon:deps
%description
A small C library with that portably invokes native file open, folder
select and file save dialogs. Write dialog code once and have it pop up
native dialogs on all supported platforms. Avoid linking large
dependencies like wxWidgets and Qt.

This library is based on Michael Labbe's Native File Dialog (
mlabbe/nativefiledialog).

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
A small C library with that portably invokes native file open, folder
select and file save dialogs. Write dialog code once and have it pop up
native dialogs on all supported platforms. Avoid linking large
dependencies like wxWidgets and Qt.

This library is based on Michael Labbe's Native File Dialog (
mlabbe/nativefiledialog).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
  -D NFD_BUILD_TESTS=OFF \
  -D BUILD_SHARED_LIBRARY=ON
%cmake_build
%check

%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n nativefiledialog-extended-devel -f %{oreon_filedir}/nativefiledialog-extended-devel.list

%changelog

%autochangelog
