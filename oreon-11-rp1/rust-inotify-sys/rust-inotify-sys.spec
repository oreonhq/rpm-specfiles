%global source0_hash e05c02b5e89bff3b946cedeca278abc628fe811e604f027c45a8aa3cf793d0eb
%bcond check 0
%global debug_package %{nil}
%global crate inotify-sys
Name:           rust-inotify-sys
Version:        0.1.5
Release:        1%{?dist}
Summary:        Inotify bindings for the Rust programming language
License:        ISC
URL:            https://crates.io/crates/inotify-sys
Source0:        https://static.crates.io/crates/inotify-sys/inotify-sys-%{version}.crate
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
Summary:        Inotify bindings for the Rust programming language
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
%files -n rust-inotify-sys-devel -f %{oreon_filedir}/rust-inotify-sys-devel.list

%changelog

%autochangelog
