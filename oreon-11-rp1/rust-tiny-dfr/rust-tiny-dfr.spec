%global source0_hash 5ca2d7d41e627c2f66908a0cdb5f817b8457a2c24014ad5841f3090aa7bb67db
%bcond check 1
%global crate tiny-dfr
Name:           rust-tiny-dfr
Version:        0.3.7
Release:        1%{?dist}
Summary:        Most basic dynamic function row daemon possible
License:        MIT AND Apache-2.0
URL:            https://crates.io/crates/tiny-dfr
Source0:        https://static.crates.io/crates/tiny-dfr/tiny-dfr-%{version}.crate
Patch:          tiny-dfr-fix-metadata.diff
Patch2:         https://github.com/AsahiLinux/tiny-dfr/pull/81.patch
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Most basic dynamic function row daemon possible
License:        (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND ISC AND MIT AND (MIT AND Apache-2.0) AND (MIT OR Apache-2.0) AND MPL-2.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
%description -n %{crate}

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
install -Dpm0644 -t %{buildroot}%{_datadir}/%{crate} share/%{crate}/*.svg share/%{crate}/config.toml
install -Ddpm0755 %{buildroot}%{_sysconfdir}/%{crate}
touch %{buildroot}%{_sysconfdir}/%{crate}/config.toml
install -Dpm0644 -t %{buildroot}%{_udevrulesdir} etc/udev/rules.d/*.rules
install -Dpm0644 -t %{buildroot}%{_unitdir} etc/systemd/system/%{crate}.service
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post -n %{crate}

%systemd_post %{crate}.service
%preun -n %{crate}

%systemd_preun %{crate}.service
%postun -n %{crate}

%systemd_postun_with_restart %{crate}.service
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n tiny-dfr -f %{oreon_filedir}/tiny-dfr.list

%changelog

%autochangelog
