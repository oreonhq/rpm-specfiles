%global source0_hash 0352975c36cbacb9ee99bfb709b9db818bed43af57751797f8633649759d13db
%bcond check 0
%global debug_package %{nil}
%global crate pancurses
Name:           rust-pancurses
Version:        0.17.0
Release:        1%{?dist}
Summary:        Curses library for Rust that supports both Unix and Windows
License:        MIT
URL:            https://crates.io/crates/pancurses
Source0:        https://static.crates.io/crates/pancurses/pancurses-%{version}.crate
Patch:          pancurses-fix-metadata-auto.diff
Patch:          pancurses-fix-metadata.diff
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
Summary:        Curses library for Rust that supports both Unix and Windows
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+disable_resize-devel
Summary:        Curses library for Rust that supports both Unix and Windows
BuildArch:      noarch
%description -n %{name}+disable_resize-devel

This package contains library source intended for building other packages which
use the "disable_resize" feature of the "%{crate}" crate.

%package     -n %{name}+show_menu-devel
Summary:        Curses library for Rust that supports both Unix and Windows
BuildArch:      noarch
%description -n %{name}+show_menu-devel

This package contains library source intended for building other packages which
use the "show_menu" feature of the "%{crate}" crate.

%package     -n %{name}+wide-devel
Summary:        Curses library for Rust that supports both Unix and Windows
BuildArch:      noarch
%description -n %{name}+wide-devel

This package contains library source intended for building other packages which
use the "wide" feature of the "%{crate}" crate.

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
%files -n rust-pancurses-devel -f %{oreon_filedir}/rust-pancurses-devel.list

%changelog

%autochangelog
