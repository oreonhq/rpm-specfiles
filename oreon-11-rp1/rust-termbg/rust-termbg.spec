%global source0_hash 8bf44577a1adf3dfd7fec3b8763074467e27b2ad35ff9157bc3f0a51bb0a3dd4
%bcond check 1
%global crate termbg
Name:           rust-termbg
Version:        0.6.2
Release:        1%{?dist}
Summary:        Terminal background color detection
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/termbg
Source0:        https://static.crates.io/crates/termbg/termbg-%{version}.crate
Patch:          termbg-fix-metadata-auto.diff
Patch:          termbg-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Terminal background color detection
License:        Apache-2.0 AND MIT AND Unicode-DFS-2016 AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Unlicense OR MIT)
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Terminal background color detection
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n termbg -f %{oreon_filedir}/termbg.list
%files -n rust-termbg-devel -f %{oreon_filedir}/rust-termbg-devel.list

%changelog

%autochangelog
