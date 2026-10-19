%global source0_hash 4a9fd2d1f9ba37e767283228fef33d53c136e81a570800f0531da1986e595079
%bcond check 0
%global crate clang-tidy-sarif
Name:           rust-clang-tidy-sarif
Version:        0.8.0
Release:        1%{?dist}
Summary:        Convert clang-tidy output to SARIF
License:        MIT
URL:            https://crates.io/crates/clang-tidy-sarif
Source0:        https://static.crates.io/crates/clang-tidy-sarif/clang-tidy-sarif-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Convert clang-tidy output to SARIF
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
%files -n clang-tidy-sarif -f %{oreon_filedir}/clang-tidy-sarif.list

%changelog

%autochangelog
