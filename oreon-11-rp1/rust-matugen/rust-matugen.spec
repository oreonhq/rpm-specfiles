%global source0_hash 297e0e07ed011bc661e4e4a83847e2d546b5db44963d035b3b6df4762312c040
%bcond check 1
%global cargo_install_lib 0
%global crate matugen
Name:           rust-matugen
Version:        3.1.0
Release:        1%{?dist}
Summary:        Material you color generation tool with templates
License:        GPL-2.0-only
URL:            https://crates.io/crates/matugen
Source0:        https://static.crates.io/crates/matugen/matugen-%{version}.crate
Patch:          matugen-fix-metadata-auto.diff
Patch:          matugen-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Material you color generation tool with templates
License:        %{shrink:
    GPL-2.0-only
    AND Apache-2.0
    AND Apache-2.0 WITH LLVM-exception
    AND BSD-2-Clause
    AND BSD-3-Clause
    AND MIT
    AND MPL-2.0
    AND Unicode-DFS-2016
    AND Zlib
    AND (0BSD OR MIT OR Apache-2.0)
    AND (Apache-2.0 OR BSL-1.0)
    AND (Apache-2.0 OR MIT)
    AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
    AND (BSD-2-Clause OR Apache-2.0 OR MIT)
    AND (MIT OR Apache-2.0 OR NCSA)
    AND (MIT OR Apache-2.0 OR Zlib)
    AND (Unlicense OR MIT)
}
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}
%install
%cargo_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n matugen -f %{oreon_filedir}/matugen.list

%changelog

%autochangelog
