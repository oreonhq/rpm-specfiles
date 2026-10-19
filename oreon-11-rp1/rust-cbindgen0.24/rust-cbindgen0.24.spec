%global source0_hash 4b922faaf31122819ec80c4047cc684c6979a087366c069611e33649bf98e18d
%bcond check 0
%global debug_package %{nil}
%global crate cbindgen
Name:           rust-cbindgen0.24
Version:        0.24.5
Release:        1%{?dist}
Summary:        A tool for generating C bindings to Rust code.
License:        MPL-2.0
URL:            https://crates.io/crates/cbindgen
Source0:        https://static.crates.io/crates/cbindgen/cbindgen-%{version}.crate
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
Summary:        A tool for generating C bindings to Rust code.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+clap-devel
Summary:        A tool for generating C bindings to Rust code.
BuildArch:      noarch
%description -n %{name}+clap-devel

This package contains library source intended for building other packages which
use the "clap" feature of the "%{crate}" crate.

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
%files -n rust-cbindgen0.24-devel -f %{oreon_filedir}/rust-cbindgen0.24-devel.list

%changelog

%autochangelog
