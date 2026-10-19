%global source0_hash 97e3d90edb6a3053b6b346ed9fbff13a03f7c1bfc9f872b8d48167d87a3632c0
%bcond check 1
%global debug_package %{nil}
%global crate usbredirparser-sys
Name:           rust-usbredirparser-sys
Version:        0.4.0
Release:        1%{?dist}
Summary:        FFI bindings for usbredirparser
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/usbredirparser-sys
Source0:        https://static.crates.io/crates/usbredirparser-sys/usbredirparser-sys-%{version}.crate
ExcludeArch:    i686
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(libusbredirparser-0.5)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libusbredirparser-0.5) >= 0.13
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        FFI bindings for usbredirparser
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
%files -n rust-usbredirparser-sys-devel -f %{oreon_filedir}/rust-usbredirparser-sys-devel.list

%changelog

%autochangelog
