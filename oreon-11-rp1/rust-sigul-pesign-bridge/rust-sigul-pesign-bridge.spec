%global source0_hash f1f35a2f0ab258fa2e0b7352705081d0d6af7bcdc6fa2cb79fca0d026ba1bcc1
%bcond check 1
%global cargo_install_lib 0
%global crate sigul-pesign-bridge
Name:           rust-sigul-pesign-bridge
Version:        0.10.1
Release:        1%{?dist}
Summary:        Bridge pesign-client requests to a Sigul signing server
License:        MIT
URL:            https://crates.io/crates/sigul-pesign-bridge
Source0:        https://static.crates.io/crates/sigul-pesign-bridge/sigul-pesign-bridge-%{version}.crate
ExcludeArch:    %{ix86}
Patch:          0001-sigul-pesign-bridge-switch-to-using-the-standard-tem.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description

%package     -n sigul-pesign-bridge
Summary:        Bridge pesign-client requests to a Sigul signing server
License:        Unicode-DFS-2016 AND (MIT OR Apache-2.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND MIT AND (Unlicense OR MIT)
Recommends:     sbsigntools
Requires:       pesign
%post -n sigul-pesign-bridge

%systemd_post sigul-pesign-bridge.service
%preun -n sigul-pesign-bridge

%systemd_preun sigul-pesign-bridge.service
%postun -n sigul-pesign-bridge

%systemd_postun_with_restart sigul-pesign-bridge.service
%description -n sigul-pesign-bridge

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
install -D -p -m 0644 sigul-pesign-bridge.service %{buildroot}%{_unitdir}/sigul-pesign-bridge.service
install -D -p -m 0644 docs/sigul-pesign-bridge.1 %{buildroot}%{_mandir}/man1/sigul-pesign-bridge.1
install -D -p -m 0644 config.toml.example %{buildroot}%{_sysconfdir}/sigul-pesign-bridge/config.toml
%oreon_autofiles sigul-pesign-bridge usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test -- --lib
%cargo_test -- --doc
%cargo_test -- --bins
%endif
%files -f %{oreon_filedir}/main.list
%files -n sigul-pesign-bridge -f %{oreon_filedir}/sigul-pesign-bridge.list

%changelog

%autochangelog
