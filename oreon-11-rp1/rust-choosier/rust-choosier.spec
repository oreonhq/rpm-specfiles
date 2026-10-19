%global source0_hash 36016284fc35d2549f806f5f4c4409877fecd3b56f3ae30e6c6f81a2324a6411
%bcond check 0
%global crate choosier
Name:           rust-choosier
Version:        0.1.0
Release:        1%{?dist}
Summary:        Choose your browser based on the URL given
License:        MPL-2.0
URL:            https://crates.io/crates/choosier
Source0:        https://static.crates.io/crates/choosier/choosier-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Choose your browser based on the URL given
License:        MPL-2.0 AND (MIT OR Apache-2.0)
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
install -Dpm0644 -t %{buildroot}/%{_datadir}/applications assets/choosier.desktop
mkdir -p %{buildroot}/%{_sysconfdir}/choosier
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
desktop-file-validate %{buildroot}/%{_datadir}/applications/choosier.desktop
%endif
%files -f %{oreon_filedir}/main.list
%files -n choosier -f %{oreon_filedir}/choosier.list

%changelog

%autochangelog
