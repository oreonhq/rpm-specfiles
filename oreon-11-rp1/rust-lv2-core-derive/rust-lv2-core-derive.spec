%global source0_hash 7bf98f786ecb49030330834aaa458f84bbaf545d7084cf3dcb2fab2f03a1838b
%bcond check 0
%global debug_package %{nil}
%global crate lv2-core-derive
Name:           rust-lv2-core-derive
Version:        2.1.1
Release:        1%{?dist}
Summary:        Procedural macros for lv2-core
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/lv2-core-derive
Source0:        https://static.crates.io/crates/lv2-core-derive/lv2-core-derive-%{version}.crate
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
Summary:        Procedural macros for lv2-core
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
%files -n rust-lv2-core-derive-devel -f %{oreon_filedir}/rust-lv2-core-derive-devel.list

%changelog

%autochangelog
