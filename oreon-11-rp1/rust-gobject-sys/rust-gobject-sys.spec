%global source0_hash 07595c9ba696bd9819cb6a8df39f08078f3dd679508fe052dd558492c2053834
%bcond check 1
%global debug_package %{nil}
%global crate gobject-sys
Name:           rust-gobject-sys
Version:        0.22.9
Release:        1%{?dist}
Summary:        FFI bindings to libgobject-2.0
License:        MIT
URL:            https://crates.io/crates/gobject-sys
Source0:        https://static.crates.io/crates/gobject-sys/gobject-sys-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gobject-2.0) >= 2.56
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        FFI bindings to libgobject-2.0
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+v2_58-devel
Summary:        FFI bindings to libgobject-2.0
BuildArch:      noarch
Requires:       pkgconfig(gobject-2.0) >= 2.58
%description -n %{name}+v2_58-devel

This package contains library source intended for building other packages which
use the "v2_58" feature of the "%{crate}" crate.

%package     -n %{name}+v2_62-devel
Summary:        FFI bindings to libgobject-2.0
BuildArch:      noarch
Requires:       pkgconfig(gobject-2.0) >= 2.62
%description -n %{name}+v2_62-devel

This package contains library source intended for building other packages which
use the "v2_62" feature of the "%{crate}" crate.

%package     -n %{name}+v2_66-devel
Summary:        FFI bindings to libgobject-2.0
BuildArch:      noarch
Requires:       pkgconfig(gobject-2.0) >= 2.66
%description -n %{name}+v2_66-devel

This package contains library source intended for building other packages which
use the "v2_66" feature of the "%{crate}" crate.

%package     -n %{name}+v2_68-devel
Summary:        FFI bindings to libgobject-2.0
BuildArch:      noarch
Requires:       pkgconfig(gobject-2.0) >= 2.68
%description -n %{name}+v2_68-devel

This package contains library source intended for building other packages which
use the "v2_68" feature of the "%{crate}" crate.

%package     -n %{name}+v2_70-devel
Summary:        FFI bindings to libgobject-2.0
BuildArch:      noarch
Requires:       pkgconfig(gobject-2.0) >= 2.70
%description -n %{name}+v2_70-devel

This package contains library source intended for building other packages which
use the "v2_70" feature of the "%{crate}" crate.

%package     -n %{name}+v2_72-devel
Summary:        FFI bindings to libgobject-2.0
BuildArch:      noarch
Requires:       pkgconfig(gobject-2.0) >= 2.72
%description -n %{name}+v2_72-devel

This package contains library source intended for building other packages which
use the "v2_72" feature of the "%{crate}" crate.

%package     -n %{name}+v2_74-devel
Summary:        FFI bindings to libgobject-2.0
BuildArch:      noarch
Requires:       pkgconfig(gobject-2.0) >= 2.74
%description -n %{name}+v2_74-devel

This package contains library source intended for building other packages which
use the "v2_74" feature of the "%{crate}" crate.

%package     -n %{name}+v2_76-devel
Summary:        FFI bindings to libgobject-2.0
BuildArch:      noarch
Requires:       pkgconfig(gobject-2.0) >= 2.76
%description -n %{name}+v2_76-devel

This package contains library source intended for building other packages which
use the "v2_76" feature of the "%{crate}" crate.

%package     -n %{name}+v2_78-devel
Summary:        FFI bindings to libgobject-2.0
BuildArch:      noarch
Requires:       pkgconfig(gobject-2.0) >= 2.77
%description -n %{name}+v2_78-devel

This package contains library source intended for building other packages which
use the "v2_78" feature of the "%{crate}" crate.

%package     -n %{name}+v2_80-devel
Summary:        FFI bindings to libgobject-2.0
BuildArch:      noarch
Requires:       pkgconfig(gobject-2.0) >= 2.80
%description -n %{name}+v2_80-devel

This package contains library source intended for building other packages which
use the "v2_80" feature of the "%{crate}" crate.

%package     -n %{name}+v2_82-devel
Summary:        FFI bindings to libgobject-2.0
BuildArch:      noarch
Requires:       pkgconfig(gobject-2.0) >= 2.82
%description -n %{name}+v2_82-devel

This package contains library source intended for building other packages which
use the "v2_82" feature of the "%{crate}" crate.

%package     -n %{name}+v2_84-devel
Summary:        FFI bindings to libgobject-2.0
BuildArch:      noarch
Requires:       pkgconfig(gobject-2.0) >= 2.84
%description -n %{name}+v2_84-devel

This package contains library source intended for building other packages which
use the "v2_84" feature of the "%{crate}" crate.

%package     -n %{name}+v2_86-devel
Summary:        FFI bindings to libgobject-2.0
BuildArch:      noarch
Requires:       pkgconfig(gobject-2.0) >= 2.86
%description -n %{name}+v2_86-devel

This package contains library source intended for building other packages which
use the "v2_86" feature of the "%{crate}" crate.

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
%files -n rust-gobject-sys-devel -f %{oreon_filedir}/rust-gobject-sys-devel.list

%changelog

%autochangelog
