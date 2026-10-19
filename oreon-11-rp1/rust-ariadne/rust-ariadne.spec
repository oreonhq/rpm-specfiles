%global source0_hash 44055e597c674aef7cb903b2b9f6e4cba1277ed0d2d61dae7cd52d7ffa81f8e2
%bcond check 0
%global debug_package %{nil}
%global crate ariadne
Name:           rust-ariadne
Version:        0.4.1
Release:        1%{?dist}
Summary:        Fancy diagnostics & reporting crate
License:        MIT
URL:            https://crates.io/crates/ariadne
Source0:        https://static.crates.io/crates/ariadne/ariadne-%{version}.crate
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
Summary:        Fancy diagnostics & reporting crate
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+auto-color-devel
Summary:        Fancy diagnostics & reporting crate
BuildArch:      noarch
%description -n %{name}+auto-color-devel

This package contains library source intended for building other packages which
use the "auto-color" feature of the "%{crate}" crate.

%package     -n %{name}+concolor-devel
Summary:        Fancy diagnostics & reporting crate
BuildArch:      noarch
%description -n %{name}+concolor-devel

This package contains library source intended for building other packages which
use the "concolor" feature of the "%{crate}" crate.

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
%files -n rust-ariadne-devel -f %{oreon_filedir}/rust-ariadne-devel.list

%changelog

%autochangelog
