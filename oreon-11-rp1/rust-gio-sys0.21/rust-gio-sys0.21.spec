%global source0_hash 0071fe88dba8e40086c8ff9bbb62622999f49628344b1d1bf490a48a29d80f22
%bcond check 0
%global debug_package %{nil}
%global crate gio-sys
Name:           rust-gio-sys0.21
Version:        0.21.5
Release:        1%{?dist}
Summary:        FFI bindings to libgio-2.0
License:        MIT
URL:            https://crates.io/crates/gio-sys
Source0:        https://static.crates.io/crates/gio-sys/gio-sys-%{version}.crate
Patch:          gio-sys-fix-metadata-auto.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gio-2.0) >= 2.56
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        FFI bindings to libgio-2.0
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+v2_58-devel
Summary:        FFI bindings to libgio-2.0
BuildArch:      noarch
Requires:       pkgconfig(gio-2.0) >= 2.58
%description -n %{name}+v2_58-devel

This package contains library source intended for building other packages which
use the "v2_58" feature of the "%{crate}" crate.

%package     -n %{name}+v2_60-devel
Summary:        FFI bindings to libgio-2.0
BuildArch:      noarch
Requires:       pkgconfig(gio-2.0) >= 2.60
%description -n %{name}+v2_60-devel

This package contains library source intended for building other packages which
use the "v2_60" feature of the "%{crate}" crate.

%package     -n %{name}+v2_62-devel
Summary:        FFI bindings to libgio-2.0
BuildArch:      noarch
Requires:       pkgconfig(gio-2.0) >= 2.62
%description -n %{name}+v2_62-devel

This package contains library source intended for building other packages which
use the "v2_62" feature of the "%{crate}" crate.

%package     -n %{name}+v2_64-devel
Summary:        FFI bindings to libgio-2.0
BuildArch:      noarch
Requires:       pkgconfig(gio-2.0) >= 2.64
%description -n %{name}+v2_64-devel

This package contains library source intended for building other packages which
use the "v2_64" feature of the "%{crate}" crate.

%package     -n %{name}+v2_66-devel
Summary:        FFI bindings to libgio-2.0
BuildArch:      noarch
Requires:       pkgconfig(gio-2.0) >= 2.66
%description -n %{name}+v2_66-devel

This package contains library source intended for building other packages which
use the "v2_66" feature of the "%{crate}" crate.

%package     -n %{name}+v2_68-devel
Summary:        FFI bindings to libgio-2.0
BuildArch:      noarch
Requires:       pkgconfig(gio-2.0) >= 2.68
%description -n %{name}+v2_68-devel

This package contains library source intended for building other packages which
use the "v2_68" feature of the "%{crate}" crate.

%package     -n %{name}+v2_70-devel
Summary:        FFI bindings to libgio-2.0
BuildArch:      noarch
Requires:       pkgconfig(gio-2.0) >= 2.70
%description -n %{name}+v2_70-devel

This package contains library source intended for building other packages which
use the "v2_70" feature of the "%{crate}" crate.

%package     -n %{name}+v2_72-devel
Summary:        FFI bindings to libgio-2.0
BuildArch:      noarch
Requires:       pkgconfig(gio-2.0) >= 2.72
%description -n %{name}+v2_72-devel

This package contains library source intended for building other packages which
use the "v2_72" feature of the "%{crate}" crate.

%package     -n %{name}+v2_74-devel
Summary:        FFI bindings to libgio-2.0
BuildArch:      noarch
Requires:       pkgconfig(gio-2.0) >= 2.74
%description -n %{name}+v2_74-devel

This package contains library source intended for building other packages which
use the "v2_74" feature of the "%{crate}" crate.

%package     -n %{name}+v2_76-devel
Summary:        FFI bindings to libgio-2.0
BuildArch:      noarch
Requires:       pkgconfig(gio-2.0) >= 2.76
%description -n %{name}+v2_76-devel

This package contains library source intended for building other packages which
use the "v2_76" feature of the "%{crate}" crate.

%package     -n %{name}+v2_78-devel
Summary:        FFI bindings to libgio-2.0
BuildArch:      noarch
Requires:       pkgconfig(gio-2.0) >= 2.77
%description -n %{name}+v2_78-devel

This package contains library source intended for building other packages which
use the "v2_78" feature of the "%{crate}" crate.

%package     -n %{name}+v2_80-devel
Summary:        FFI bindings to libgio-2.0
BuildArch:      noarch
Requires:       pkgconfig(gio-2.0) >= 2.80
%description -n %{name}+v2_80-devel

This package contains library source intended for building other packages which
use the "v2_80" feature of the "%{crate}" crate.

%package     -n %{name}+v2_82-devel
Summary:        FFI bindings to libgio-2.0
BuildArch:      noarch
Requires:       pkgconfig(gio-2.0) >= 2.82
%description -n %{name}+v2_82-devel

This package contains library source intended for building other packages which
use the "v2_82" feature of the "%{crate}" crate.

%package     -n %{name}+v2_84-devel
Summary:        FFI bindings to libgio-2.0
BuildArch:      noarch
Requires:       pkgconfig(gio-2.0) >= 2.84
%description -n %{name}+v2_84-devel

This package contains library source intended for building other packages which
use the "v2_84" feature of the "%{crate}" crate.

%package     -n %{name}+v2_86-devel
Summary:        FFI bindings to libgio-2.0
BuildArch:      noarch
Requires:       pkgconfig(gio-2.0) >= 2.85
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
%files -n rust-gio-sys0.21-devel -f %{oreon_filedir}/rust-gio-sys0.21-devel.list

%changelog

%autochangelog
