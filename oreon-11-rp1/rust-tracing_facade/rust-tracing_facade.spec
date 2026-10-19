%global source1_hash 47efd1f81483c5255e366e10a9faf1c6171f7daf6c3a834e01e70d0e65a3849f
%global source0_hash 5240e4a28639b8f6a7871acb435c36da749f553a12d1769e4c4a9d34ce2a00cf
%bcond check 0
%global debug_package %{nil}
%global crate tracing_facade
Name:           rust-tracing_facade
Version:        0.1.0
Release:        1%{?dist}
Summary:        Facade for tracing
License:        0BSD
URL:            https://crates.io/crates/tracing_facade
Source0:        https://static.crates.io/crates/tracing_facade/tracing_facade-%{version}.crate
Source1:        https://raw.githubusercontent.com/jmgao/tracing/master/LICENSE
Patch:          tracing_facade-fix-metadata.diff
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
Summary:        Facade for tracing
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE1} .
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
%files -n rust-tracing_facade-devel -f %{oreon_filedir}/rust-tracing_facade-devel.list

%changelog

%autochangelog
