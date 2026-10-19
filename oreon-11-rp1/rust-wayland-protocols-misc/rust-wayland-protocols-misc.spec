%global source2_hash a9bdde5616ecdd1e980b44f360600ee8783b1f99b8cc83a2beb163a0a390e861
%global source0_hash 6e9567599ef23e09b8dad6e429e5738d4509dfc46b3b21f32841a304d16b29c8
%bcond check 1
%global debug_package %{nil}
%global crate wayland-protocols-misc
Name:           rust-wayland-protocols-misc
Version:        0.3.12
Release:        1%{?dist}
Summary:        Generated API for misc and deprecated wayland protocol extensions
License:        MIT
URL:            https://crates.io/crates/wayland-protocols-misc
Source0:        https://static.crates.io/crates/wayland-protocols-misc/wayland-protocols-misc-%{version}.crate
Source2:        https://invent.kde.org/libraries/plasma-wayland-protocols/-/raw/master/COPYING.LIB
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
Summary:        Generated API for misc and deprecated wayland protocol extensions
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+client-devel
Summary:        Generated API for misc and deprecated wayland protocol extensions
BuildArch:      noarch
%description -n %{name}+client-devel

This package contains library source intended for building other packages which
use the "client" feature of the "%{crate}" crate.

%package     -n %{name}+server-devel
Summary:        Generated API for misc and deprecated wayland protocol extensions
BuildArch:      noarch
%description -n %{name}+server-devel

This package contains library source intended for building other packages which
use the "server" feature of the "%{crate}" crate.

%package     -n %{name}+wayland-client-devel
Summary:        Generated API for misc and deprecated wayland protocol extensions
BuildArch:      noarch
%description -n %{name}+wayland-client-devel

This package contains library source intended for building other packages which
use the "wayland-client" feature of the "%{crate}" crate.

%package     -n %{name}+wayland-server-devel
Summary:        Generated API for misc and deprecated wayland protocol extensions
BuildArch:      noarch
%description -n %{name}+wayland-server-devel

This package contains library source intended for building other packages which
use the "wayland-server" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp %{SOURCE2} LICENSE-LGPL-2.1.txt
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
%files -n rust-wayland-protocols-misc-devel -f %{oreon_filedir}/rust-wayland-protocols-misc-devel.list

%changelog

%autochangelog
