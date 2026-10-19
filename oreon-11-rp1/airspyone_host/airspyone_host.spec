%global source0_hash fcca23911c9a9da71cebeffeba708c59d1d6401eec6eb2dd73cae35b8ea3c613
Name:           airspyone_host
Version:        1.0.10
Release:        1%{?dist}
Summary:        AirSpy host tools and library
License:        GPL-2.0-or-later AND MIT AND BSD-3-Clause AND LGPL-2.1-or-later
URL:            http://airspy.com/
Source0:        https://github.com/airspy/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          airspyone_host-1.0.10-c23-fix.patch
Patch:          100.patch
Requires:       systemd-udev
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libusbx-devel
BuildRequires:  systemd
# /oreon:deps
%description
Software for AirSpy, a project to produce a low cost, open
source software radio platform.

%package devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
License:        MIT AND BSD-3-Clause
Summary:        Development files for %{name}
%description devel
Files needed to develop software against libairspy.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Remove win stuff
rm -rf libairspy/vc

# Fix udev rule
sed -i -e 's/GROUP="plugdev"/ENV{ID_SOFTWARE_RADIO}="1"/g' airspy-tools/52-airspy.rules

%build

%cmake -DINSTALL_UDEV_RULES=on
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{_libdir}/libairspy.a
mkdir -p %{buildroot}%{_udevrulesdir}
mv %{buildroot}%{_sysconfdir}/udev/rules.d/52-airspy.rules %{buildroot}%{_udevrulesdir}
%oreon_autofiles airspyone_host-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%?ldconfig
%udev_rules_update
%postun

%?ldconfig
%udev_rules_update
%files -f %{oreon_filedir}/main.list
%files -n airspyone_host-devel -f %{oreon_filedir}/airspyone_host-devel.list

%changelog

%autochangelog
