%global source0_hash b4f06627d36ed5ff303d2df65211fc2e52ba5b17bf18dd80ff3d9628d6e06cfd
%bcond check 0
%global debug_package %{nil}
%global crate pango-sys
Name:           rust-pango-sys0.21
Version:        0.21.5
Release:        1%{?dist}
Summary:        FFI bindings to libpango-1.0
License:        MIT
URL:            https://crates.io/crates/pango-sys
Source0:        https://static.crates.io/crates/pango-sys/pango-sys-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(pango)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(pango) >= 1.40
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        FFI bindings to libpango-1.0
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+v1_42-devel
Summary:        FFI bindings to libpango-1.0
BuildArch:      noarch
Requires:       pkgconfig(pango) >= 1.42
%description -n %{name}+v1_42-devel

This package contains library source intended for building other packages which
use the "v1_42" feature of the "%{crate}" crate.

%package     -n %{name}+v1_44-devel
Summary:        FFI bindings to libpango-1.0
BuildArch:      noarch
Requires:       pkgconfig(pango) >= 1.44
%description -n %{name}+v1_44-devel

This package contains library source intended for building other packages which
use the "v1_44" feature of the "%{crate}" crate.

%package     -n %{name}+v1_46-devel
Summary:        FFI bindings to libpango-1.0
BuildArch:      noarch
Requires:       pkgconfig(pango) >= 1.46
%description -n %{name}+v1_46-devel

This package contains library source intended for building other packages which
use the "v1_46" feature of the "%{crate}" crate.

%package     -n %{name}+v1_48-devel
Summary:        FFI bindings to libpango-1.0
BuildArch:      noarch
Requires:       pkgconfig(pango) >= 1.48
%description -n %{name}+v1_48-devel

This package contains library source intended for building other packages which
use the "v1_48" feature of the "%{crate}" crate.

%package     -n %{name}+v1_50-devel
Summary:        FFI bindings to libpango-1.0
BuildArch:      noarch
Requires:       pkgconfig(pango) >= 1.50
%description -n %{name}+v1_50-devel

This package contains library source intended for building other packages which
use the "v1_50" feature of the "%{crate}" crate.

%package     -n %{name}+v1_52-devel
Summary:        FFI bindings to libpango-1.0
BuildArch:      noarch
Requires:       pkgconfig(pango) >= 1.52
%description -n %{name}+v1_52-devel

This package contains library source intended for building other packages which
use the "v1_52" feature of the "%{crate}" crate.

%package     -n %{name}+v1_54-devel
Summary:        FFI bindings to libpango-1.0
BuildArch:      noarch
Requires:       pkgconfig(pango) >= 1.54
%description -n %{name}+v1_54-devel

This package contains library source intended for building other packages which
use the "v1_54" feature of the "%{crate}" crate.

%package     -n %{name}+v1_56-devel
Summary:        FFI bindings to libpango-1.0
BuildArch:      noarch
Requires:       pkgconfig(pango) >= 1.55
%description -n %{name}+v1_56-devel

This package contains library source intended for building other packages which
use the "v1_56" feature of the "%{crate}" crate.

%package     -n %{name}+v1_57-devel
Summary:        FFI bindings to libpango-1.0
BuildArch:      noarch
Requires:       pkgconfig(pango) >= 1.57
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
%files -n rust-pango-sys0.21-devel -f %{oreon_filedir}/rust-pango-sys0.21-devel.list

%changelog

%autochangelog
