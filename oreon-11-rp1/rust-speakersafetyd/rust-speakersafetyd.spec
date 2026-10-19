%global source0_hash 7f817422aaab29ae2583771858445eacaed8eccd3fce6687ea593c0db17f9d80
%bcond check 1
%global crate speakersafetyd
Name:           rust-speakersafetyd
Version:        1.0.2
Release:        1%{?dist}
Summary:        Speaker protection daemon for embedded Linux systems
License:        MIT
URL:            https://crates.io/crates/speakersafetyd
Source0:        https://static.crates.io/crates/speakersafetyd/speakersafetyd-%{version}.crate
Patch:          speakersafetyd-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Speaker protection daemon for embedded Linux systems
License:        (Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0) AND (MIT OR LGPL-3.0-or-later) AND MPL-2.0
Requires:       systemd-udev
%description -n %{crate}

%post -n %{crate}

%systemd_post speakersafetyd.service
%preun -n %{crate}

%systemd_preun speakersafetyd.service
%postun -n %{crate}

%systemd_postun_with_restart speakersafetyd.service
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
install -p -m 0644 -D speakersafetyd.service %{buildroot}%{_unitdir}/speakersafetyd.service
install -p -m 0644 -D 95-speakersafetyd.rules %{buildroot}%{_udevrulesdir}/95-speakersafetyd.rules
install -d -m 0755 %{buildroot}%{_datadir}/speakersafetyd/apple
install -p -m 0644 -t %{buildroot}%{_datadir}/speakersafetyd/apple conf/apple/*
install -d -m 0755 %{buildroot}%{_sharedstatedir}/speakersafetyd/blackbox
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n speakersafetyd -f %{oreon_filedir}/speakersafetyd.list

%changelog

%autochangelog
