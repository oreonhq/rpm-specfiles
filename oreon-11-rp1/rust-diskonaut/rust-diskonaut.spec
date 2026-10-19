%global source0_hash 03e948901ec04b57e567d7d6d956bf62c4ad89528f42429906449bbe4290a4c7
%bcond check 0
%global crate diskonaut
Name:           rust-diskonaut
Version:        0.11.0
Release:        1%{?dist}
Summary:        Terminal disk space visual navigator
License:        MIT
URL:            https://crates.io/crates/diskonaut
Source0:        https://static.crates.io/crates/diskonaut/diskonaut-%{version}.crate
Patch:          diskonaut-fix-metadata-auto.diff
Patch:          diskonaut-fix-metadata.diff
Patch:          port-dependencies.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Terminal disk space visual navigator
License:        MIT AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT)
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
%files -n diskonaut -f %{oreon_filedir}/diskonaut.list

%changelog

%autochangelog
