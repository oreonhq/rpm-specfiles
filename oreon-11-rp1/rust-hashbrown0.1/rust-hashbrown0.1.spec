%global source0_hash 3bae29b6653b3412c2e71e9d486db9f9df5d701941d86683005efb9f2d28e3da
%bcond check 0
%global debug_package %{nil}
%global crate hashbrown
Name:           rust-hashbrown0.1
Version:        0.1.8
Release:        1%{?dist}
Summary:        A Rust port of Google's SwissTable hash map
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/hashbrown
Source0:        https://static.crates.io/crates/hashbrown/hashbrown-%{version}.crate
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

%package     -n %{name}+nightly-devel
Summary:        A Rust port of Google's SwissTable hash map
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        A Rust port of Google's SwissTable hash map
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A Rust port of Google's SwissTable hash map
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-hashbrown0.1-devel -f %{oreon_filedir}/rust-hashbrown0.1-devel.list

%changelog

%autochangelog
