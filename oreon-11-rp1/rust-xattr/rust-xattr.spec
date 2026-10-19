%global source0_hash 32e45ad4206f6d2479085147f02bc2ef834ac85886624a23575ae137c8aa8156
%bcond check 0
%global debug_package %{nil}
%global crate xattr
Name:           rust-xattr
Version:        1.6.1
Release:        1%{?dist}
Summary:        unix extended filesystem attributes
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/xattr
Source0:        https://static.crates.io/crates/xattr/xattr-%{version}.crate
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
Summary:        unix extended filesystem attributes
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+unsupported-devel
Summary:        unix extended filesystem attributes
BuildArch:      noarch
%description -n %{name}+unsupported-devel

This package contains library source intended for building other packages which
use the "unsupported" feature of the "%{crate}" crate.

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
%files -n rust-xattr-devel -f %{oreon_filedir}/rust-xattr-devel.list

%changelog

%autochangelog
