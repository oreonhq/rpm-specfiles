%global source0_hash daae2a0a6df41ab9565d788f19775b2fcfb14f7ab0f6cd44290cf9a01680a4cc
%bcond check 1
%global crate monitord-exporter
Name:           rust-monitord-exporter
Version:        0.26.2
Release:        1%{?dist}
Summary:        Let Prometheus know how happy your systemd is
License:        GPL-2.0-or-later
URL:            https://crates.io/crates/monitord-exporter
Source0:        https://static.crates.io/crates/monitord-exporter/monitord-exporter-%{version}.crate
Patch:          monitord-exporter-fix-metadata.diff
Patch:          0001-Add-missing-type-annotation-for-prometheus-0.14-comp.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Let Prometheus know how happy your systemd is
License:        ((MIT OR Apache-2.0) AND Unicode-3.0) AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND GPL-2.0-or-later AND MIT AND (MIT OR Apache-2.0) AND (MIT OR LGPL-3.0-or-later) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT)
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Let Prometheus know how happy your systemd is
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
install -Dpm0644 -t %{buildroot}%{_unitdir} monitord-exporter.service
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%systemd_post monitord-exporter.service
%preun

%systemd_preun monitord-exporter.service
%postun

%systemd_postun_with_restart monitord-exporter.service
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n monitord-exporter -f %{oreon_filedir}/monitord-exporter.list
%files -n rust-monitord-exporter-devel -f %{oreon_filedir}/rust-monitord-exporter-devel.list

%changelog

%autochangelog
