%global source0_hash 7eec5d1121208364f6793f7d2e222bf75a915c19557537745b195b253dd64217
%bcond check 0
%global debug_package %{nil}
%global crate unicode-bom
Name:           rust-unicode-bom
Version:        2.0.3
Release:        2%{?dist}
Summary:        Unicode byte-order mark detection for files and byte arrays.
License:        Apache-2.0
URL:            https://crates.io/crates/unicode-bom
Source0:        https://static.crates.io/crates/unicode-bom/unicode-bom-%{version}.crate
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
Summary:        Unicode byte-order mark detection for files and byte arrays.
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
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-unicode-bom-devel -f %{oreon_filedir}/rust-unicode-bom-devel.list

%changelog

%autochangelog
