%global source0_hash 662d74b3d77e396b8e5beb00b9cad6a9eccf40b2ef68cc858784b14c41d535a3
%bcond check 1
%global debug_package %{nil}
%global crate x11-clipboard
Name:           rust-x11-clipboard
Version:        0.9.3
Release:        1%{?dist}
Summary:        X11 clipboard support for Rust
License:        MIT
URL:            https://crates.io/crates/x11-clipboard
Source0:        https://static.crates.io/crates/x11-clipboard/x11-clipboard-%{version}.crate
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
Summary:        X11 clipboard support for Rust
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
%files -n rust-x11-clipboard-devel -f %{oreon_filedir}/rust-x11-clipboard-devel.list

%changelog

%autochangelog
