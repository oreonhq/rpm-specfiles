%global source0_hash f6eee640d2d3e939915ef2576b4d0d6aa4d40d96b37cfbcec38c3c1ff7d4f221
%bcond check 1
%global debug_package %{nil}
%global crate libblkid-rs
Name:           rust-libblkid-rs
Version:        0.4.2
Release:        1%{?dist}
Summary:        High level bindings for libblkid
License:        MPL-2.0
URL:            https://crates.io/crates/libblkid-rs
Source0:        https://static.crates.io/crates/libblkid-rs/libblkid-rs-%{version}.crate
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
Summary:        High level bindings for libblkid
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+deprecated-devel
Summary:        High level bindings for libblkid
BuildArch:      noarch
%description -n %{name}+deprecated-devel

This package contains library source intended for building other packages which
use the "deprecated" feature of the "%{crate}" crate.

%package     -n %{name}+static-devel
Summary:        High level bindings for libblkid
BuildArch:      noarch
%description -n %{name}+static-devel

This package contains library source intended for building other packages which
use the "static" feature of the "%{crate}" crate.

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
%files -n rust-libblkid-rs-devel -f %{oreon_filedir}/rust-libblkid-rs-devel.list

%changelog

%autochangelog
