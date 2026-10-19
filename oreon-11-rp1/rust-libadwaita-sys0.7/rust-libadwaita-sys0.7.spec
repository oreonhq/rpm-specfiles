%global source0_hash 6680988058c2558baf3f548a370e4e78da3bf7f08469daa822ac414842c912db
%bcond check 0
%global debug_package %{nil}
%global crate libadwaita-sys
Name:           rust-libadwaita-sys0.7
Version:        0.7.2
Release:        1%{?dist}
Summary:        FFI bindings for libadwaita
License:        MIT
URL:            https://crates.io/crates/libadwaita-sys
Source0:        https://static.crates.io/crates/libadwaita-sys/libadwaita-sys-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libadwaita-1) >= 1.0.0
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        FFI bindings for libadwaita
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+v1_1-devel
Summary:        FFI bindings for libadwaita
BuildArch:      noarch
Requires:       pkgconfig(libadwaita-1) >= 1.1
%description -n %{name}+v1_1-devel

This package contains library source intended for building other packages which
use the "v1_1" feature of the "%{crate}" crate.

%package     -n %{name}+v1_2-devel
Summary:        FFI bindings for libadwaita
BuildArch:      noarch
Requires:       pkgconfig(libadwaita-1) >= 1.2
%description -n %{name}+v1_2-devel

This package contains library source intended for building other packages which
use the "v1_2" feature of the "%{crate}" crate.

%package     -n %{name}+v1_3-devel
Summary:        FFI bindings for libadwaita
BuildArch:      noarch
Requires:       pkgconfig(libadwaita-1) >= 1.3
%description -n %{name}+v1_3-devel

This package contains library source intended for building other packages which
use the "v1_3" feature of the "%{crate}" crate.

%package     -n %{name}+v1_4-devel
Summary:        FFI bindings for libadwaita
BuildArch:      noarch
Requires:       pkgconfig(libadwaita-1) >= 1.4
%description -n %{name}+v1_4-devel

This package contains library source intended for building other packages which
use the "v1_4" feature of the "%{crate}" crate.

%package     -n %{name}+v1_5-devel
Summary:        FFI bindings for libadwaita
BuildArch:      noarch
Requires:       pkgconfig(libadwaita-1) >= 1.5
%description -n %{name}+v1_5-devel

This package contains library source intended for building other packages which
use the "v1_5" feature of the "%{crate}" crate.

%package     -n %{name}+v1_6-devel
Summary:        FFI bindings for libadwaita
BuildArch:      noarch
Requires:       pkgconfig(libadwaita-1) >= 1.6
%description -n %{name}+v1_6-devel

This package contains library source intended for building other packages which
use the "v1_6" feature of the "%{crate}" crate.

%package     -n %{name}+v1_7-devel
Summary:        FFI bindings for libadwaita
BuildArch:      noarch
Requires:       pkgconfig(libadwaita-1) >= 1.7
%description -n %{name}+v1_7-devel

This package contains library source intended for building other packages which
use the "v1_7" feature of the "%{crate}" crate.

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
%files -n rust-libadwaita-sys0.7-devel -f %{oreon_filedir}/rust-libadwaita-sys0.7-devel.list

%changelog

%autochangelog
