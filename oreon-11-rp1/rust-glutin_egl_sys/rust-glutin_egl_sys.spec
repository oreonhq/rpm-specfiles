%global source0_hash 4c4680ba6195f424febdc3ba46e7a42a0e58743f2edb115297b86d7f8ecc02d2
%bcond check 1
%global debug_package %{nil}
%global crate glutin_egl_sys
Name:           rust-glutin_egl_sys
Version:        0.7.1
Release:        1%{?dist}
Summary:        Egl bindings for glutin
License:        Apache-2.0
URL:            https://crates.io/crates/glutin_egl_sys
Source0:        https://static.crates.io/crates/glutin_egl_sys/glutin_egl_sys-%{version}.crate
Patch:          glutin_egl_sys-fix-metadata-auto.diff
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
Summary:        Egl bindings for glutin
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
%files -n rust-glutin_egl_sys-devel -f %{oreon_filedir}/rust-glutin_egl_sys-devel.list

%changelog

%autochangelog
