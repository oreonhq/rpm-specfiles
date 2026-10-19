%global source0_hash ea27d8d5fd867b17523bf6788b1175fa9867f34669d057e9adaf76e27bcea44b
%bcond check 0
%global debug_package %{nil}
%global crate box_drawing
Name:           rust-box_drawing
Version:        0.1.2
Release:        1%{?dist}
Summary:        Very simple library containing constants for UTF-8 box drawing
License:        MIT
URL:            https://crates.io/crates/box_drawing
Source0:        https://static.crates.io/crates/box_drawing/box_drawing-%{version}.crate
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
Summary:        Very simple library containing constants for UTF-8 box drawing
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-box_drawing-devel -f %{oreon_filedir}/rust-box_drawing-devel.list

%changelog

%autochangelog
