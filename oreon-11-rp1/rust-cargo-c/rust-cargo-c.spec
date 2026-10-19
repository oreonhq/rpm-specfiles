%global source0_hash 6b2ddde58a8a773ccce4b6384acacd3ce01373f52717dd2424633ed46755c627
%bcond check 1
%ifarch %{ix86}
%global rustflags_debuginfo 1
%endif
%global crate cargo-c
%global crate_version 0.10.25+cargo-0.99.0
%global crate_instdir %{cargo_registry}/%{crate}-%{crate_version}
Name:           rust-cargo-c
Version:        0.10.25
Release:        1%{?dist}
Summary:        Helper program to build and install c-like libraries
License:        MIT
URL:            https://crates.io/crates/cargo-c
Source0:        https://static.crates.io/crates/%{crate}/%{crate}-%{crate_version}.crate
Source1:        macros.cargo-c
Patch:          cargo-c-fix-metadata-auto.diff
Patch:          cargo-c-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Helper program to build and install c-like libraries
License:        %{shrink:
    MIT AND
    AND Apache-2.0
    AND BSD-2-Clause
    AND BSD-3-Clause
    AND ISC
    AND MPL-2.0
    AND Unicode-3.0
    AND Unicode-DFS-2016
    AND Zlib
    AND (Apache-2.0 OR MIT)
    AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception)
    AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
    AND (BSD-2-Clause OR Apache-2.0 OR MIT)
    AND (MIT OR Apache-2.0 OR BSD-1-Clause)
    AND (MIT OR Apache-2.0 OR Zlib)
    AND (MIT-0 OR Apache-2.0)
    AND (Unlicense OR MIT)
}
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Helper program to build and install c-like libraries
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{crate_version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
install -D -p -m 0644 -t %{buildroot}/%{_rpmmacrodir} %{SOURCE1}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n cargo-c -f %{oreon_filedir}/cargo-c.list
%files -n rust-cargo-c-devel -f %{oreon_filedir}/rust-cargo-c-devel.list

%changelog

%autochangelog
