%global source0_hash ec657fd32bbcbeaef5c7bc8e10b3db95b143fab8db0a50079773dbf936fd4f73
%bcond check 0
%global debug_package %{nil}
%global crate yeslogic-fontconfig-sys
Name:           rust-yeslogic-fontconfig-sys4
Version:        4.0.1
Release:        1%{?dist}
Summary:        Raw bindings to Fontconfig
License:        MIT
URL:            https://crates.io/crates/yeslogic-fontconfig-sys
Source0:        https://static.crates.io/crates/yeslogic-fontconfig-sys/yeslogic-fontconfig-sys-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(fontconfig)
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Raw bindings to Fontconfig
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+dlopen-devel
Summary:        Raw bindings to Fontconfig
BuildArch:      noarch
%description -n %{name}+dlopen-devel

This package contains library source intended for building other packages which
use the "dlopen" feature of the "%{crate}" crate.

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
%files -n rust-yeslogic-fontconfig-sys4-devel -f %{oreon_filedir}/rust-yeslogic-fontconfig-sys4-devel.list

%changelog

%autochangelog
