%global source0_hash 8e27e276e7b6b8d50f6376ee7769a71133e80d093bdc363bd0af71664228b831
%bcond check 1
%global debug_package %{nil}
%global crate gio
Name:           rust-gio0.20
Version:        0.20.12
Release:        1%{?dist}
Summary:        Rust bindings for the Gio library
License:        MIT
URL:            https://crates.io/crates/gio
Source0:        https://static.crates.io/crates/gio/gio-%{version}.crate
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
Summary:        Rust bindings for the Gio library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+v2_58-devel
Summary:        Rust bindings for the Gio library
BuildArch:      noarch
%description -n %{name}+v2_58-devel

This package contains library source intended for building other packages which
use the "v2_58" feature of the "%{crate}" crate.

%package     -n %{name}+v2_60-devel
Summary:        Rust bindings for the Gio library
BuildArch:      noarch
%description -n %{name}+v2_60-devel

This package contains library source intended for building other packages which
use the "v2_60" feature of the "%{crate}" crate.

%package     -n %{name}+v2_62-devel
Summary:        Rust bindings for the Gio library
BuildArch:      noarch
%description -n %{name}+v2_62-devel

This package contains library source intended for building other packages which
use the "v2_62" feature of the "%{crate}" crate.

%package     -n %{name}+v2_64-devel
Summary:        Rust bindings for the Gio library
BuildArch:      noarch
%description -n %{name}+v2_64-devel

This package contains library source intended for building other packages which
use the "v2_64" feature of the "%{crate}" crate.

%package     -n %{name}+v2_66-devel
Summary:        Rust bindings for the Gio library
BuildArch:      noarch
%description -n %{name}+v2_66-devel

This package contains library source intended for building other packages which
use the "v2_66" feature of the "%{crate}" crate.

%package     -n %{name}+v2_68-devel
Summary:        Rust bindings for the Gio library
BuildArch:      noarch
%description -n %{name}+v2_68-devel

This package contains library source intended for building other packages which
use the "v2_68" feature of the "%{crate}" crate.

%package     -n %{name}+v2_70-devel
Summary:        Rust bindings for the Gio library
BuildArch:      noarch
%description -n %{name}+v2_70-devel

This package contains library source intended for building other packages which
use the "v2_70" feature of the "%{crate}" crate.

%package     -n %{name}+v2_72-devel
Summary:        Rust bindings for the Gio library
BuildArch:      noarch
%description -n %{name}+v2_72-devel

This package contains library source intended for building other packages which
use the "v2_72" feature of the "%{crate}" crate.

%package     -n %{name}+v2_74-devel
Summary:        Rust bindings for the Gio library
BuildArch:      noarch
%description -n %{name}+v2_74-devel

This package contains library source intended for building other packages which
use the "v2_74" feature of the "%{crate}" crate.

%package     -n %{name}+v2_76-devel
Summary:        Rust bindings for the Gio library
BuildArch:      noarch
%description -n %{name}+v2_76-devel

This package contains library source intended for building other packages which
use the "v2_76" feature of the "%{crate}" crate.

%package     -n %{name}+v2_78-devel
Summary:        Rust bindings for the Gio library
BuildArch:      noarch
%description -n %{name}+v2_78-devel

This package contains library source intended for building other packages which
use the "v2_78" feature of the "%{crate}" crate.

%package     -n %{name}+v2_80-devel
Summary:        Rust bindings for the Gio library
BuildArch:      noarch
%description -n %{name}+v2_80-devel

This package contains library source intended for building other packages which
use the "v2_80" feature of the "%{crate}" crate.

%package     -n %{name}+v2_82-devel
Summary:        Rust bindings for the Gio library
BuildArch:      noarch
%description -n %{name}+v2_82-devel

This package contains library source intended for building other packages which
use the "v2_82" feature of the "%{crate}" crate.

%package     -n %{name}+v2_84-devel
Summary:        Rust bindings for the Gio library
BuildArch:      noarch
%description -n %{name}+v2_84-devel

This package contains library source intended for building other packages which
use the "v2_84" feature of the "%{crate}" crate.

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
%files -n rust-gio0.20-devel -f %{oreon_filedir}/rust-gio0.20-devel.list

%changelog

%autochangelog
