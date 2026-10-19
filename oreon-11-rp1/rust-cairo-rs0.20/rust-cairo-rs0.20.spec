%global source0_hash 91e3bd0f4e25afa9cabc157908d14eeef9067d6448c49414d17b3fb55f0eadd0
%bcond check 0
%global debug_package %{nil}
%global crate cairo-rs
Name:           rust-cairo-rs0.20
Version:        0.20.12
Release:        1%{?dist}
Summary:        Rust bindings for the Cairo library
License:        MIT
URL:            https://crates.io/crates/cairo-rs
Source0:        https://static.crates.io/crates/cairo-rs/cairo-rs-%{version}.crate
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
Summary:        Rust bindings for the Cairo library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+freetype-devel
Summary:        Rust bindings for the Cairo library
BuildArch:      noarch
%description -n %{name}+freetype-devel

This package contains library source intended for building other packages which
use the "freetype" feature of the "%{crate}" crate.

%package     -n %{name}+freetype-rs-devel
Summary:        Rust bindings for the Cairo library
BuildArch:      noarch
%description -n %{name}+freetype-rs-devel

This package contains library source intended for building other packages which
use the "freetype-rs" feature of the "%{crate}" crate.

%package     -n %{name}+glib-devel
Summary:        Rust bindings for the Cairo library
BuildArch:      noarch
%description -n %{name}+glib-devel

This package contains library source intended for building other packages which
use the "glib" feature of the "%{crate}" crate.

%package     -n %{name}+pdf-devel
Summary:        Rust bindings for the Cairo library
BuildArch:      noarch
%description -n %{name}+pdf-devel

This package contains library source intended for building other packages which
use the "pdf" feature of the "%{crate}" crate.

%package     -n %{name}+png-devel
Summary:        Rust bindings for the Cairo library
BuildArch:      noarch
%description -n %{name}+png-devel

This package contains library source intended for building other packages which
use the "png" feature of the "%{crate}" crate.

%package     -n %{name}+ps-devel
Summary:        Rust bindings for the Cairo library
BuildArch:      noarch
%description -n %{name}+ps-devel

This package contains library source intended for building other packages which
use the "ps" feature of the "%{crate}" crate.

%package     -n %{name}+script-devel
Summary:        Rust bindings for the Cairo library
BuildArch:      noarch
%description -n %{name}+script-devel

This package contains library source intended for building other packages which
use the "script" feature of the "%{crate}" crate.

%package     -n %{name}+svg-devel
Summary:        Rust bindings for the Cairo library
BuildArch:      noarch
%description -n %{name}+svg-devel

This package contains library source intended for building other packages which
use the "svg" feature of the "%{crate}" crate.

%package     -n %{name}+use_glib-devel
Summary:        Rust bindings for the Cairo library
BuildArch:      noarch
%description -n %{name}+use_glib-devel

This package contains library source intended for building other packages which
use the "use_glib" feature of the "%{crate}" crate.

%package     -n %{name}+v1_16-devel
Summary:        Rust bindings for the Cairo library
BuildArch:      noarch
%description -n %{name}+v1_16-devel

This package contains library source intended for building other packages which
use the "v1_16" feature of the "%{crate}" crate.

%package     -n %{name}+v1_18-devel
Summary:        Rust bindings for the Cairo library
BuildArch:      noarch
%description -n %{name}+v1_18-devel

This package contains library source intended for building other packages which
use the "v1_18" feature of the "%{crate}" crate.

%package     -n %{name}+xcb-devel
Summary:        Rust bindings for the Cairo library
BuildArch:      noarch
%description -n %{name}+xcb-devel

This package contains library source intended for building other packages which
use the "xcb" feature of the "%{crate}" crate.

%package     -n %{name}+xlib-devel
Summary:        Rust bindings for the Cairo library
BuildArch:      noarch
%description -n %{name}+xlib-devel

This package contains library source intended for building other packages which
use the "xlib" feature of the "%{crate}" crate.

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
%files -n rust-cairo-rs0.20-devel -f %{oreon_filedir}/rust-cairo-rs0.20-devel.list

%changelog

%autochangelog
