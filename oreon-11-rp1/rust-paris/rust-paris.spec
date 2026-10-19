%global source0_hash 8fecab3723493c7851f292cb060f3ee1c42f19b8d749345d0d7eaf3fd19aa62d
%bcond check 0
%global debug_package %{nil}
%global crate paris
Name:           rust-paris
Version:        1.5.15
Release:        1%{?dist}
Summary:        Simple logger for your CLI apps or other things you want in the terminal
License:        MPL-2.0
URL:            https://crates.io/crates/paris
Source0:        https://static.crates.io/crates/paris/paris-%{version}.crate
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
Summary:        Simple logger for your CLI apps or other things you want in the terminal
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+macros-devel
Summary:        Simple logger for your CLI apps or other things you want in the terminal
BuildArch:      noarch
%description -n %{name}+macros-devel

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%package     -n %{name}+no_logger-devel
Summary:        Simple logger for your CLI apps or other things you want in the terminal
BuildArch:      noarch
%description -n %{name}+no_logger-devel

This package contains library source intended for building other packages which
use the "no_logger" feature of the "%{crate}" crate.

%package     -n %{name}+timestamps-devel
Summary:        Simple logger for your CLI apps or other things you want in the terminal
BuildArch:      noarch
%description -n %{name}+timestamps-devel

This package contains library source intended for building other packages which
use the "timestamps" feature of the "%{crate}" crate.

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
%files -n rust-paris-devel -f %{oreon_filedir}/rust-paris-devel.list

%changelog

%autochangelog
