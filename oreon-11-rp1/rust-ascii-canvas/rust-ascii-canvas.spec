%global source0_hash ef1e3e699d84ab1b0911a1010c5c106aa34ae89aeac103be5ce0c3859db1e891
%bcond check 0
%global debug_package %{nil}
%global crate ascii-canvas
Name:           rust-ascii-canvas
Version:        4.0.0
Release:        1%{?dist}
Summary:        simple canvas for drawing lines and styled text and emitting to the t...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/ascii-canvas
Source0:        https://static.crates.io/crates/ascii-canvas/ascii-canvas-%{version}.crate
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
Summary:        simple canvas for drawing lines and styled text and emitting to the t...
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
%files -n rust-ascii-canvas-devel -f %{oreon_filedir}/rust-ascii-canvas-devel.list

%changelog

%autochangelog
