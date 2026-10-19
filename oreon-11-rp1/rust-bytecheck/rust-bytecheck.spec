%global source0_hash 0caa33a2c0edca0419d15ac723dff03f1956f7978329b1e3b5fdaaaed9d3ca8b
%bcond check 0
%global debug_package %{nil}
%global crate bytecheck
Name:           rust-bytecheck
Version:        0.8.2
Release:        1%{?dist}
Summary:        Memory validation framework for Rust
License:        MIT
URL:            https://crates.io/crates/bytecheck
Source0:        https://static.crates.io/crates/bytecheck/bytecheck-%{version}.crate
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
Summary:        Memory validation framework for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+simdutf8-devel
Summary:        Memory validation framework for Rust
BuildArch:      noarch
%description -n %{name}+simdutf8-devel

This package contains library source intended for building other packages which
use the "simdutf8" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-1-devel
Summary:        Memory validation framework for Rust
BuildArch:      noarch
%description -n %{name}+uuid-1-devel

This package contains library source intended for building other packages which
use the "uuid-1" feature of the "%{crate}" crate.

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
%files -n rust-bytecheck-devel -f %{oreon_filedir}/rust-bytecheck-devel.list

%changelog

%autochangelog
