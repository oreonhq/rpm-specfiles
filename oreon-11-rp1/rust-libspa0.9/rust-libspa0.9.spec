%global source0_hash b6b8cfa2a7656627b4c92c6b9ef929433acd673d5ab3708cda1b18478ac00df4
%bcond check 0
%global debug_package %{nil}
%global crate libspa
Name:           rust-libspa0.9
Version:        0.9.2
Release:        1%{?dist}
Summary:        Rust bindings for libspa
License:        MIT
URL:            https://crates.io/crates/libspa
Source0:        https://static.crates.io/crates/libspa/libspa-%{version}.crate
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
Summary:        Rust bindings for libspa
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+v0_3_33-devel
Summary:        Rust bindings for libspa
BuildArch:      noarch
%description -n %{name}+v0_3_33-devel

This package contains library source intended for building other packages which
use the "v0_3_33" feature of the "%{crate}" crate.

%package     -n %{name}+v0_3_40-devel
Summary:        Rust bindings for libspa
BuildArch:      noarch
%description -n %{name}+v0_3_40-devel

This package contains library source intended for building other packages which
use the "v0_3_40" feature of the "%{crate}" crate.

%package     -n %{name}+v0_3_65-devel
Summary:        Rust bindings for libspa
BuildArch:      noarch
%description -n %{name}+v0_3_65-devel

This package contains library source intended for building other packages which
use the "v0_3_65" feature of the "%{crate}" crate.

%package     -n %{name}+v0_3_75-devel
Summary:        Rust bindings for libspa
BuildArch:      noarch
%description -n %{name}+v0_3_75-devel

This package contains library source intended for building other packages which
use the "v0_3_75" feature of the "%{crate}" crate.

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
%files -n rust-libspa0.9-devel -f %{oreon_filedir}/rust-libspa0.9-devel.list

%changelog

%autochangelog
