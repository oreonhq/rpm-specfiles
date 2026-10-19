%global source0_hash 596c5b6c39c8395a7cc71e77ad8e89c48f4f6fa1e65a509c10bc79eaa03c7191
%bcond check 0
%global crate clippy-sarif
Name:           rust-clippy-sarif
Version:        0.8.0
Release:        1%{?dist}
Summary:        Convert clippy output to SARIF
License:        MIT
URL:            https://crates.io/crates/clippy-sarif
Source0:        https://static.crates.io/crates/clippy-sarif/clippy-sarif-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Convert clippy output to SARIF
License:        MIT AND Unicode-DFS-2016 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT)
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
%files -n clippy-sarif -f %{oreon_filedir}/clippy-sarif.list

%changelog

%autochangelog
