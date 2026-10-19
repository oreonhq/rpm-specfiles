%global source0_hash 38e9f87936bc2fa6beb9519855fe343fa6e002b457b5e8b6e6e82ca68bc0ea61
%bcond check 1
%global crate below
%global forgeurl https://github.com/facebookincubator/below
Name:           rust-below
Version:        0.9.0
Release:        1%{?dist}
Summary:        Interactive tool to view and record historical system data
License:        Apache-2.0
URL:            https://crates.io/crates/below
Source0:        https://static.crates.io/crates/below/below-%{version}.crate
Source1:        %{forgeurl}/raw/v%{version}/etc/below.service
Source2:        %{forgeurl}/raw/v%{version}/etc/logrotate.conf
Patch:          below-fix-metadata.diff
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Interactive tool to view and record historical system data
License:        %{shrink:
                Apache-2.0
                AND (MIT OR Apache-2.0) AND Unicode-DFS-2016
                AND 0BSD
                AND (Apache-2.0 OR BSL-1.0)
                AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
                AND BSD-2-Clause
                AND (BSD-2-Clause OR Apache-2.0 OR MIT)
                AND (LGPL-2.1-only OR BSD-2-Clause)
                AND MIT
                AND (MPL-2.0 OR MIT OR Apache-2.0)
                AND (Unlicense OR MIT)
                }
Recommends:     logrotate
%description -n %{crate}

%post        -n %{crate}

%systemd_post %{crate}.service
%preun       -n %{crate}

%systemd_preun %{crate}.service
%postun      -n %{crate}

%systemd_postun_with_restart %{crate}.service
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
install -D -p -m0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{crate}.service
install -D -p -m0644 %{SOURCE2} \
  %{buildroot}%{_sysconfdir}/logrotate.d/%{crate}.conf
install -d -m1777 %{buildroot}%{_localstatedir}/log/%{crate}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test -- -- --exact --skip test::record_replay_integration
%endif
%files -f %{oreon_filedir}/main.list
%files -n below -f %{oreon_filedir}/below.list

%changelog

%autochangelog
