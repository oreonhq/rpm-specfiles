%global source0_hash 64e9829a50b42bb782c1df523f78d332fe371b10c661e78b7a3c34b0198e9fac
%bcond check 0
%global debug_package %{nil}
%global crate infer
Name:           rust-infer
Version:        0.2.3
Release:        1%{?dist}
Summary:        Small crate to infer file types based on its magic number signature
License:        MIT
URL:            https://crates.io/crates/infer
Source0:        https://static.crates.io/crates/infer/infer-%{version}.crate
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
Summary:        Small crate to infer file types based on its magic number signature
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
%files -n rust-infer-devel -f %{oreon_filedir}/rust-infer-devel.list

%changelog

%autochangelog
