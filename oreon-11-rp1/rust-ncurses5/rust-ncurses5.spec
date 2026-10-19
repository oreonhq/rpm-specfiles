%global source0_hash 5e2c5d34d72657dc4b638a1c25d40aae81e4f1c699062f72f467237920752032
%bcond check 1
%global debug_package %{nil}
%global crate ncurses
Name:           rust-ncurses5
Version:        5.101.0
Release:        1%{?dist}
Summary:        Very thin wrapper around the ncurses TUI library
License:        MIT
URL:            https://crates.io/crates/ncurses
Source0:        https://static.crates.io/crates/ncurses/ncurses-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  ncurses-devel
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       ncurses-devel
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Very thin wrapper around the ncurses TUI library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+extended_colors-devel
Summary:        Very thin wrapper around the ncurses TUI library
BuildArch:      noarch
%description -n %{name}+extended_colors-devel

This package contains library source intended for building other packages which
use the "extended_colors" feature of the "%{crate}" crate.

%package     -n %{name}+menu-devel
Summary:        Very thin wrapper around the ncurses TUI library
BuildArch:      noarch
%description -n %{name}+menu-devel

This package contains library source intended for building other packages which
use the "menu" feature of the "%{crate}" crate.

%package     -n %{name}+mouse_v1-devel
Summary:        Very thin wrapper around the ncurses TUI library
BuildArch:      noarch
%description -n %{name}+mouse_v1-devel

This package contains library source intended for building other packages which
use the "mouse_v1" feature of the "%{crate}" crate.

%package     -n %{name}+panel-devel
Summary:        Very thin wrapper around the ncurses TUI library
BuildArch:      noarch
%description -n %{name}+panel-devel

This package contains library source intended for building other packages which
use the "panel" feature of the "%{crate}" crate.

%package     -n %{name}+wide-devel
Summary:        Very thin wrapper around the ncurses TUI library
BuildArch:      noarch
%description -n %{name}+wide-devel

This package contains library source intended for building other packages which
use the "wide" feature of the "%{crate}" crate.

%package     -n %{name}+wide_chtype-devel
Summary:        Very thin wrapper around the ncurses TUI library
BuildArch:      noarch
%description -n %{name}+wide_chtype-devel

This package contains library source intended for building other packages which
use the "wide_chtype" feature of the "%{crate}" crate.

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
%files -n rust-ncurses5-devel -f %{oreon_filedir}/rust-ncurses5-devel.list

%changelog

%autochangelog
