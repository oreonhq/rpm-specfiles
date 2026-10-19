%global source0_hash 8bb5cdbecf0ea5c99a50412afc0a18a7343b432513dd806f3aab0a808bb2c3c5
%bcond check 1
%global debug_package %{nil}
%global crate below-ethtool
%global unsupported_arches %{ix86}
Name:           rust-below-ethtool
Version:        0.9.0
Release:        1%{?dist}
Summary:        Ethtool crate for below
License:        Apache-2.0
URL:            https://crates.io/crates/below-ethtool
Source0:        https://static.crates.io/crates/below-ethtool/below-ethtool-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Ethtool crate for below
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%ifnarch %{unsupported_arches}
%cargo_build
%endif
%install
%cargo_install
%if %{with check}
%ifnarch %{unsupported_arches}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%cargo_test
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-below-ethtool-devel -f %{oreon_filedir}/rust-below-ethtool-devel.list

%changelog

%autochangelog
