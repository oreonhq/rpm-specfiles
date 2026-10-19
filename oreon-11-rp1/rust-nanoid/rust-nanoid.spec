%global source0_hash 8628de41fe064cc3f0cf07f3d299ee3e73521adaff72278731d5c8cae3797873
%bcond check 1
%global debug_package %{nil}
%global crate nanoid
Name:           rust-nanoid
Version:        0.5.0
Release:        1%{?dist}
Summary:        Tiny, secure, URL-friendly, unique string ID generator for Rust
License:        MIT
URL:            https://crates.io/crates/nanoid
Source0:        https://static.crates.io/crates/nanoid/nanoid-%{version}.crate
Patch:          nanoid-fix-metadata.diff
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
Summary:        Tiny, secure, URL-friendly, unique string ID generator for Rust
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
%files -n rust-nanoid-devel -f %{oreon_filedir}/rust-nanoid-devel.list

%changelog

%autochangelog
