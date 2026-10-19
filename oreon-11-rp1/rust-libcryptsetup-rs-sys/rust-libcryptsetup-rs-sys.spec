%global source0_hash 376e4a1f481c5f0b8354d370cfaf9f1322d56e628e2954c6b59c9729e6f4d5ee
%bcond check 1
%global debug_package %{nil}
%global crate libcryptsetup-rs-sys
Name:           rust-libcryptsetup-rs-sys
Version:        0.6.1
Release:        1%{?dist}
Summary:        Low level bindings for libcryptsetup
License:        MPL-2.0
URL:            https://crates.io/crates/libcryptsetup-rs-sys
Source0:        https://static.crates.io/crates/libcryptsetup-rs-sys/libcryptsetup-rs-sys-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(libcryptsetup)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libcryptsetup)
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Low level bindings for libcryptsetup
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+static-devel
Summary:        Low level bindings for libcryptsetup
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
%files -n rust-libcryptsetup-rs-sys-devel -f %{oreon_filedir}/rust-libcryptsetup-rs-sys-devel.list

%changelog

%autochangelog
