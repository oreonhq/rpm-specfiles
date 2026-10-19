%global source0_hash 40c48f72fd53cd289104fc64099abca73db4166ad86ea0b4341abe65af83dadc
%bcond check 1
%global debug_package %{nil}
%global crate anstyle-query
Name:           rust-anstyle-query
Version:        1.1.5
Release:        1%{?dist}
Summary:        Look up colored console capabilities
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/anstyle-query
Source0:        https://static.crates.io/crates/anstyle-query/anstyle-query-%{version}.crate
Patch:          anstyle-query-fix-metadata-auto.diff
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
Summary:        Look up colored console capabilities
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
%files -n rust-anstyle-query-devel -f %{oreon_filedir}/rust-anstyle-query-devel.list

%changelog

%autochangelog
