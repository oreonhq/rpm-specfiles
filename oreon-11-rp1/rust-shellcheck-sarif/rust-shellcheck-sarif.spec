%global source0_hash 9398cb52d62b73d3a0837c6cb197a439d8a14334c778a174cb258c7c09ce4cf2
%bcond check 0
%global crate shellcheck-sarif
Name:           rust-shellcheck-sarif
Version:        0.5.0
Release:        1%{?dist}
Summary:        Convert shellcheck output to SARIF
License:        MIT
URL:            https://crates.io/crates/shellcheck-sarif
Source0:        https://static.crates.io/crates/shellcheck-sarif/shellcheck-sarif-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Convert shellcheck output to SARIF
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
%files -n shellcheck-sarif -f %{oreon_filedir}/shellcheck-sarif.list

%changelog

%autochangelog
