%global source0_hash 19b17cddbe7ec3f8bc800887bab5e717348c95ea2ca0b1bf0837fb964dc67099
%bcond check 0
%global debug_package %{nil}
%global crate peeking_take_while
Name:           rust-peeking_take_while
Version:        0.1.2
Release:        1%{?dist}
Summary:        Like `Iterator::take_while`, but calls the predicate on a peeked valu...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/peeking_take_while
Source0:        https://static.crates.io/crates/peeking_take_while/peeking_take_while-%{version}.crate
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
Summary:        Like `Iterator::take_while`, but calls the predicate on a peeked valu...
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
%files -n rust-peeking_take_while-devel -f %{oreon_filedir}/rust-peeking_take_while-devel.list

%changelog

%autochangelog
