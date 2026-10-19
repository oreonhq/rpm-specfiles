%global source0_hash 4ebdbbd670373442a12fe9ef7aeb53aec4147a5a27a00bbc3ab639f08f48191a
%bcond check 0
%global debug_package %{nil}
%global crate udev
Name:           rust-udev0.7
Version:        0.7.0
Release:        1%{?dist}
Summary:        Libudev bindings for Rust
License:        MIT
URL:            https://crates.io/crates/udev
Source0:        https://static.crates.io/crates/udev/udev-%{version}.crate
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
Summary:        Libudev bindings for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+hwdb-devel
Summary:        Libudev bindings for Rust
BuildArch:      noarch
%description -n %{name}+hwdb-devel

This package contains library source intended for building other packages which
use the "hwdb" feature of the "%{crate}" crate.

%package     -n %{name}+mio-devel
Summary:        Libudev bindings for Rust
BuildArch:      noarch
%description -n %{name}+mio-devel

This package contains library source intended for building other packages which
use the "mio" feature of the "%{crate}" crate.

%package     -n %{name}+mio08-devel
Summary:        Libudev bindings for Rust
BuildArch:      noarch
%description -n %{name}+mio08-devel

This package contains library source intended for building other packages which
use the "mio08" feature of the "%{crate}" crate.

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
%files -n rust-udev0.7-devel -f %{oreon_filedir}/rust-udev0.7-devel.list

%changelog

%autochangelog
