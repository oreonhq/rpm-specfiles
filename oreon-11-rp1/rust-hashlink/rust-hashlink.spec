%global source0_hash a596f1b20ed2cc5ecac41a164aaebc7258057060f06c0cf7a2ba3991ee7990fb
%bcond check 0
%global debug_package %{nil}
%global crate hashlink
Name:           rust-hashlink
Version:        0.12.2
Release:        1%{?dist}
Summary:        HashMap-like containers that hold their key-value pairs in a user con...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hashlink
Source0:        https://static.crates.io/crates/hashlink/hashlink-%{version}.crate
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

%package     -n %{name}+serde-devel
Summary:        HashMap-like containers that hold their key-value pairs in a user con...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_impl-devel
Summary:        HashMap-like containers that hold their key-value pairs in a user con...
BuildArch:      noarch
%description -n %{name}+serde_impl-devel

This package contains library source intended for building other packages which
use the "serde_impl" feature of the "%{crate}" crate.

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
%files -n rust-hashlink-devel -f %{oreon_filedir}/rust-hashlink-devel.list

%changelog

%autochangelog
