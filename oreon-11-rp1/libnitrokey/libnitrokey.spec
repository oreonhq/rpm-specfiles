%global source0_hash ef8239a4ec651339064a505e195f810596a007b84a12445c5ddf86aa1ecea633
Name:           libnitrokey
Version:        3.8
Release:        1%{?dist}
Summary:        Communicate with Nitrokey stick devices in a clean and easy manner
License:        LGPL-3.0-or-later
URL:            https://github.com/Nitrokey/libnitrokey
Source0:        https://github.com/Nitrokey/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(hidapi-libusb)
BuildRequires:  pkgconfig(udev)
# /oreon:deps
%description
Libnitrokey is a project to communicate with Nitrokey Pro and Storage devices
in a clean and easy manner.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
This package contains development libraries and header files are needed
to develop using libnitrokey.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post	

%udev_rules_update
%postun

%udev_rules_update
%files -f %{oreon_filedir}/main.list
%files -n libnitrokey-devel -f %{oreon_filedir}/libnitrokey-devel.list

%changelog

%autochangelog
