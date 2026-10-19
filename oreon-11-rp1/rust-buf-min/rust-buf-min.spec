%global source0_hash 22d5698cf6842742ed64805705798f8b351fff53fa546fd45c52184bee58dc90
%bcond check 0
%global debug_package %{nil}
%global crate buf-min
Name:           rust-buf-min
Version:        0.7.1
Release:        1%{?dist}
Summary:        Minimal utf-8 safe buffer traits
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/buf-min
Source0:        https://static.crates.io/crates/buf-min/buf-min-%{version}.crate
Patch:          buf-min-fix-metadata.diff
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
Summary:        Minimal utf-8 safe buffer traits
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bytes-devel
Summary:        Minimal utf-8 safe buffer traits
BuildArch:      noarch
%description -n %{name}+bytes-devel

This package contains library source intended for building other packages which
use the "bytes" feature of the "%{crate}" crate.

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
%files -n rust-buf-min-devel -f %{oreon_filedir}/rust-buf-min-devel.list

%changelog

%autochangelog
