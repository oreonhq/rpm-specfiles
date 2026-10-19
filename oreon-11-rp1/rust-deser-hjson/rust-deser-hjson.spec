%global source0_hash a0d49a923edd92dc1ca5819822f540ea83f094ab5ac6940e4044e03c1d8e6576
%bcond check 0
%global debug_package %{nil}
%global crate deser-hjson
Name:           rust-deser-hjson
Version:        2.2.6
Release:        1%{?dist}
Summary:        Hjson deserializer for Serde
License:        MIT
URL:            https://crates.io/crates/deser-hjson
Source0:        https://static.crates.io/crates/deser-hjson/deser-hjson-%{version}.crate
Patch:          deser-hjson-fix-metadata.diff
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
Summary:        Hjson deserializer for Serde
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
%files -n rust-deser-hjson-devel -f %{oreon_filedir}/rust-deser-hjson-devel.list

%changelog

%autochangelog
