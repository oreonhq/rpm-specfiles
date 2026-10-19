%global source0_hash 9c82cd3db386e82fba2adfe01c3d09436c9e9cfe3ca8bb341d7eb882768c58af
%bcond vendor 0
Name:           zram-generator
Version:        1.2.1
Release:        1%{?dist}
Summary:        Systemd unit generator for zram devices
License:        MIT AND (MIT OR Apache-2.0)
URL:            https://github.com/systemd/zram-generator
Source0:        https://github.com/systemd/zram-generator/archive/v%{version}/zram-generator-%{version}.tar.gz
Source1:        zram-generator.conf
Patch0:         https://github.com/systemd/zram-generator/pull/238.patch
Recommends:     %{_sbindir}/zramctl
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  /usr/bin/ronn
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(systemd)
BuildRequires:  rustc
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
This is a systemd unit generator that enables swap on zram.

To activate, install the zram-generator-defaults subpackage.

%package        defaults
Summary:        Default configuration for zram-generator
Requires:       zram-generator = %{version}-%{release}
Obsoletes:      zram < 0.4-2
BuildArch:      noarch
%description    defaults
Default zram-generator config for Oreon.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n zram-generator-%{version} -p1
cp -a %{SOURCE1} .
%oreon_vendor_cargo
%build

export SYSTEMD_UTIL_DIR=%{_systemd_util_dir}
export LC_ALL=C.UTF-8
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%make_build SYSTEMD_SYSTEM_UNIT_DIR=%{_unitdir} SYSTEMD_SYSTEM_GENERATOR_DIR=%{_systemdgeneratordir} systemd-service man
%install
export SYSTEMD_UTIL_DIR=%{_systemd_util_dir}
%make_install SYSTEMD_SYSTEM_UNIT_DIR=%{_unitdir} SYSTEMD_SYSTEM_GENERATOR_DIR=%{_systemdgeneratordir} NOBUILD=1
install -Dpm0644 -t %{buildroot}%{_prefix}/lib/systemd %{SOURCE1}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export SYSTEMD_UTIL_DIR=%{_systemd_util_dir}
%cargo_test
%{buildroot}%{_systemdgeneratordir}/zram-generator --help
%{buildroot}%{_systemdgeneratordir}/zram-generator --help | grep -q %{_systemd_util_dir}/systemd-makefs
%files -f %{oreon_filedir}/main.list
%files -n zram-generator-defaults -f %{oreon_filedir}/zram-generator-defaults.list

%changelog

* Wed Jun 10 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.1-1
- import for oreon 11 iso
