%global source0_hash 1ac7773f335b40367e963cfb3c86a2b711b1ad056eabf5c82e4516821621f402
%global gitdate 20260107
%global commit 30e0422ab5eae0fecd429b29e89c6e8699bb5cd6
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           airspyhf
Version:        1.6.8^%{gitdate}git%{shortcommit}
Release:        1%{?dist}
Summary:        AirSpy HF+ SDR host software for HF and VHF bands
License:        BSD-3-Clause AND GPL-2.0-or-later
URL:            http://airspy.com/
Source0:        https://github.com/airspy/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Requires:       systemd-udev
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libusbx-devel
BuildRequires:  systemd
# /oreon:deps
%description
Software for AirSpy HF+, a high performance software defined
radio for the HF and VHF bands.

%package devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
License:        BSD-3-Clause AND GPL-2.0-or-later
Summary:        Development files for %{name}
%description devel
Files needed to develop software against libairspy.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}
# Fix udev rule
sed -i -e 's/MODE="660", GROUP="plugdev"/TAG+="uaccess"/g' tools/52-airspyhf.rules
rm -rf tools/getopt

%build

%cmake -DINSTALL_UDEV_RULES=on
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{_libdir}/libairspyhf.a
mkdir -p %{buildroot}%{_udevrulesdir}
mv %{buildroot}%{_sysconfdir}/udev/rules.d/52-airspyhf.rules %{buildroot}%{_udevrulesdir}
%oreon_autofiles airspyhf-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%?ldconfig
%udev_rules_update
%postun

%?ldconfig
%udev_rules_update
%check

export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%{buildroot}%{_bindir}/airspyhf_lib_version
%files -f %{oreon_filedir}/main.list
%files -n airspyhf-devel -f %{oreon_filedir}/airspyhf-devel.list

%changelog

%autochangelog
