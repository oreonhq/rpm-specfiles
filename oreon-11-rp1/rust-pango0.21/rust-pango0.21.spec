%global source0_hash 52d1d85e2078077a065bb7fc072783d5bcd4e51b379f22d67107d0a16937eb69
%bcond check 1
%global debug_package %{nil}
%global crate pango
Name:           rust-pango0.21
Version:        0.21.5
Release:        1%{?dist}
Summary:        Rust bindings for the Pango library
License:        MIT
URL:            https://crates.io/crates/pango
Source0:        https://static.crates.io/crates/pango/pango-%{version}.crate
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
Summary:        Rust bindings for the Pango library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+v1_42-devel
Summary:        Rust bindings for the Pango library
BuildArch:      noarch
%description -n %{name}+v1_42-devel

This package contains library source intended for building other packages which
use the "v1_42" feature of the "%{crate}" crate.

%package     -n %{name}+v1_44-devel
Summary:        Rust bindings for the Pango library
BuildArch:      noarch
%description -n %{name}+v1_44-devel

This package contains library source intended for building other packages which
use the "v1_44" feature of the "%{crate}" crate.

%package     -n %{name}+v1_46-devel
Summary:        Rust bindings for the Pango library
BuildArch:      noarch
%description -n %{name}+v1_46-devel

This package contains library source intended for building other packages which
use the "v1_46" feature of the "%{crate}" crate.

%package     -n %{name}+v1_48-devel
Summary:        Rust bindings for the Pango library
BuildArch:      noarch
%description -n %{name}+v1_48-devel

This package contains library source intended for building other packages which
use the "v1_48" feature of the "%{crate}" crate.

%package     -n %{name}+v1_50-devel
Summary:        Rust bindings for the Pango library
BuildArch:      noarch
%description -n %{name}+v1_50-devel

This package contains library source intended for building other packages which
use the "v1_50" feature of the "%{crate}" crate.

%package     -n %{name}+v1_52-devel
Summary:        Rust bindings for the Pango library
BuildArch:      noarch
%description -n %{name}+v1_52-devel

This package contains library source intended for building other packages which
use the "v1_52" feature of the "%{crate}" crate.

%package     -n %{name}+v1_54-devel
Summary:        Rust bindings for the Pango library
BuildArch:      noarch
%description -n %{name}+v1_54-devel

This package contains library source intended for building other packages which
use the "v1_54" feature of the "%{crate}" crate.

%package     -n %{name}+v1_56-devel
Summary:        Rust bindings for the Pango library
BuildArch:      noarch
%description -n %{name}+v1_56-devel

This package contains library source intended for building other packages which
use the "v1_56" feature of the "%{crate}" crate.

%package     -n %{name}+v1_57-devel
Summary:        Rust bindings for the Pango library
BuildArch:      noarch
%description -n %{name}+v1_57-devel

This package contains library source intended for building other packages which
use the "v1_57" feature of the "%{crate}" crate.

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
%files -n rust-pango0.21-devel -f %{oreon_filedir}/rust-pango0.21-devel.list

%changelog

%autochangelog
