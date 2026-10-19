%global source0_hash 60a357793950651c4ed0f3f52338f53b2f809f32d83a07f72909fa13e4c6c1e3
%bcond check 0
%global debug_package %{nil}
%global crate rawpointer
Name:           rust-rawpointer
Version:        0.2.1
Release:        1%{?dist}
Summary:        Extra methods for raw pointers and `NonNull<T>`.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rawpointer
Source0:        https://static.crates.io/crates/rawpointer/rawpointer-%{version}.crate
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
Summary:        Extra methods for raw pointers and `NonNull<T>`.
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
%files -n rust-rawpointer-devel -f %{oreon_filedir}/rust-rawpointer-devel.list

%changelog

%autochangelog
