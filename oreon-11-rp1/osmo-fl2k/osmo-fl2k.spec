%global source0_hash d8f5ebf6b4e15b181b34c16cccb8d6e56ca657c940e8aa9513b06cc908deb91a
Name:             osmo-fl2k
URL:              https://osmocom.org/projects/osmo-fl2k/wiki
Version:          0.2.1
Release:        1%{?dist}
License:          GPL-2.0-or-later AND GPL-3.0-or-later
Requires:         systemd-udev
Summary:        Turns FL2000-based USB 3.0 to VGA adapters into low cost DACs
Source0:        https://github.com/osmocom/osmo-fl2k/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libusbx-devel
# /oreon:deps
%description
Turns FL2000-based USB 3.0 to VGA adapters into low cost DACs.

%package libs
Summary:          Libraries for osmo-fl2k
%description libs
Libraries for osmo-fl2k.

%package devel
Summary:          Development files for osmo-fl2k
Requires:         %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
Development files for osmo-fl2k.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{_libdir}/libosmo-fl2k.a
sed -i 's/MODE:="0666"/MODE:="0660", ENV{ID_SOFTWARE_RADIO}="1"/' ./osmo-fl2k.rules
install -Dpm 644 ./osmo-fl2k.rules %{buildroot}%{_prefix}/lib/udev/rules.d/10-osmo-fl2k.rules
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n osmo-fl2k-libs -f %{oreon_filedir}/osmo-fl2k-libs.list
%files -n osmo-fl2k-devel -f %{oreon_filedir}/osmo-fl2k-devel.list

%changelog

%autochangelog
