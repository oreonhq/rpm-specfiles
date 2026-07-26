%global source0_hash 2b432ccc6b9c924feb32e8adf0c115d83a2f8017df8e5d4cc238cc4d77d77fec

Name:           libnitrokey
Version:        3.7
Release:        10%{?dist}
Summary:        Communicate with Nitrokey stick devices in a clean and easy manner

License:        LGPL-3.0-or-later
URL:            https://github.com/Nitrokey/libnitrokey
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(hidapi-libusb)
BuildRequires:  pkgconfig(udev)

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

%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%post	
%udev_rules_update

%postun
%udev_rules_update

%files
%license LICENSE
%doc README.md
%{_libdir}/libnitrokey.so.*
%{_udevrulesdir}/*-nitrokey.rules

%files devel
%{_libdir}/libnitrokey.so
%{_libdir}/pkgconfig/libnitrokey-1.pc
%{_includedir}/libnitrokey/

%changelog
%autochangelog
