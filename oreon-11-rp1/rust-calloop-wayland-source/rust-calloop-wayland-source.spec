%global source0_hash 95a66a987056935f7efce4ab5668920b5d0dac4a7c99991a67395f13702ddd20
%bcond check 0
%global debug_package %{nil}
%global crate calloop-wayland-source
Name:           rust-calloop-wayland-source
Version:        0.3.0
Release:        1%{?dist}
Summary:        Wayland-rs client event source for callloop
License:        MIT
URL:            https://crates.io/crates/calloop-wayland-source
Source0:        https://static.crates.io/crates/calloop-wayland-source/calloop-wayland-source-%{version}.crate
Patch:          calloop-wayland-source-fix-metadata.diff
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
Summary:        Wayland-rs client event source for callloop
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Wayland-rs client event source for callloop
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

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
%files -n rust-calloop-wayland-source-devel -f %{oreon_filedir}/rust-calloop-wayland-source-devel.list

%changelog

%autochangelog
