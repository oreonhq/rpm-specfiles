%global source0_hash 81763af0ceec26ef18970166aa61f59df0358a294ddd7162fea0e1d52584917c
%bcond check 1
%global crate sevctl
Name:           rust-sevctl
Version:        0.6.2
Release:        1%{?dist}
Summary:        Administrative utility for AMD SEV
License:        Apache-2.0
URL:            https://crates.io/crates/sevctl
Source0:        https://static.crates.io/crates/%{crate}/%{crate}-%{version}.crate
Patch:        sevctl-fix-metadata.diff
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Administrative utility for AMD SEV
License:        Apache-2.0 AND MIT
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n sevctl -f %{oreon_filedir}/sevctl.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.2-1
- Import
