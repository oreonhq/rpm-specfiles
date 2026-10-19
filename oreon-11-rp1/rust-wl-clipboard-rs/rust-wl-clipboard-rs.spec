%global source0_hash e9651471a32e87d96ef3a127715382b2d11cc7c8bb9822ded8a7cc94072eb0a3
%bcond check 1
%global debug_package %{nil}
%global crate wl-clipboard-rs
Name:           rust-wl-clipboard-rs
Version:        0.9.3
Release:        1%{?dist}
Summary:        Access to the Wayland clipboard for terminal and other window-less applications
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/wl-clipboard-rs
Source0:        https://static.crates.io/crates/wl-clipboard-rs/wl-clipboard-rs-%{version}.crate
Patch:          wl-clipboard-rs-fix-metadata.diff
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
Summary:        Access to the Wayland clipboard for terminal and other window-less applications
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+dlopen-devel
Summary:        Access to the Wayland clipboard for terminal and other window-less applications
BuildArch:      noarch
%description -n %{name}+dlopen-devel

This package contains library source intended for building other packages which
use the "dlopen" feature of the "%{crate}" crate.

%package     -n %{name}+native_lib-devel
Summary:        Access to the Wayland clipboard for terminal and other window-less applications
BuildArch:      noarch
%description -n %{name}+native_lib-devel

This package contains library source intended for building other packages which
use the "native_lib" feature of the "%{crate}" crate.

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

%cargo_test -- --doc
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-wl-clipboard-rs-devel -f %{oreon_filedir}/rust-wl-clipboard-rs-devel.list

%changelog

%autochangelog
