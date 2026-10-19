%global source0_hash debb0d39e3cdd84626edfd54d6e4a6ba2da9a0ef2e796e691c4e9f8646fda00c
%bcond check 1
%global debug_package %{nil}
%global crate gdk-pixbuf
Name:           rust-gdk-pixbuf0.21
Version:        0.21.5
Release:        1%{?dist}
Summary:        Rust bindings for the GdkPixbuf library
License:        MIT
URL:            https://crates.io/crates/gdk-pixbuf
Source0:        https://static.crates.io/crates/gdk-pixbuf/gdk-pixbuf-%{version}.crate
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
Summary:        Rust bindings for the GdkPixbuf library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+v2_40-devel
Summary:        Rust bindings for the GdkPixbuf library
BuildArch:      noarch
%description -n %{name}+v2_40-devel

This package contains library source intended for building other packages which
use the "v2_40" feature of the "%{crate}" crate.

%package     -n %{name}+v2_42-devel
Summary:        Rust bindings for the GdkPixbuf library
BuildArch:      noarch
%description -n %{name}+v2_42-devel

This package contains library source intended for building other packages which
use the "v2_42" feature of the "%{crate}" crate.

%package     -n %{name}+v2_44-devel
Summary:        Rust bindings for the GdkPixbuf library
BuildArch:      noarch
%description -n %{name}+v2_44-devel

This package contains library source intended for building other packages which
use the "v2_44" feature of the "%{crate}" crate.

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
%files -n rust-gdk-pixbuf0.21-devel -f %{oreon_filedir}/rust-gdk-pixbuf0.21-devel.list

%changelog

%autochangelog
