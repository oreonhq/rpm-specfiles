%global source0_hash 338565ce70d26731783e8e5933549fc19ac44acdc4fced59ca85aad5f8d25a5c
%bcond check 1
%global crate zeitfetch
Name:           rust-zeitfetch
Version:        0.1.16
Release:        1%{?dist}
Summary:        Instantaneous snapshots of cross-platform system information
License:        MIT
URL:            https://crates.io/crates/zeitfetch
Source0:        https://static.crates.io/crates/zeitfetch/zeitfetch-%{version}.crate
Patch:          zeitfetch-fix-metadata-auto.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Instantaneous snapshots of cross-platform system information
License:        %{shrink:
    MIT AND
    Unicode-DFS-2016 AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (MIT OR Apache-2.0) AND
    (Unlicense OR MIT)
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
%install
%cargo_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n zeitfetch -f %{oreon_filedir}/zeitfetch.list

%changelog

%autochangelog
