%global source0_hash 4fc4729dd0ba21e9ef1c960c582aeb272d2ba26e9ebb3e4473069bda4d3247f0
%bcond check 0
%global crate hadolint-sarif
Name:           rust-hadolint-sarif
Version:        0.8.0
Release:        1%{?dist}
Summary:        Convert hadolint output to SARIF
License:        MIT
URL:            https://crates.io/crates/hadolint-sarif
Source0:        https://static.crates.io/crates/hadolint-sarif/hadolint-sarif-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Convert hadolint output to SARIF
License:        MIT AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT)
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n hadolint-sarif -f %{oreon_filedir}/hadolint-sarif.list

%changelog

%autochangelog
