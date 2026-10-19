%global source0_hash 38735924fedd5314a6e548792904ed8c6de6636285cb9fec04d5b1db85c1516f
%bcond check 0
%global debug_package %{nil}
%global crate x11-dl
Name:           rust-x11-dl
Version:        2.21.0
Release:        1%{?dist}
Summary:        X11 library bindings for Rust
License:        MIT
URL:            https://crates.io/crates/x11-dl
Source0:        https://static.crates.io/crates/x11-dl/x11-dl-%{version}.crate
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
Summary:        X11 library bindings for Rust
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
%files -n rust-x11-dl-devel -f %{oreon_filedir}/rust-x11-dl-devel.list

%changelog

%autochangelog
