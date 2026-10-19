%global source0_hash b093064383341eb3271f42e381cb8f10a01459478446953953c75d24bd339fc0
%bcond check 0
%global debug_package %{nil}
%global crate multiversion-macros
Name:           rust-multiversion-macros0.8
Version:        0.8.0
Release:        1%{?dist}
Summary:        Implementation crate for multiversion
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/multiversion-macros
Source0:        https://static.crates.io/crates/multiversion-macros/multiversion-macros-%{version}.crate
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
Summary:        Implementation crate for multiversion
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Implementation crate for multiversion
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-multiversion-macros0.8-devel -f %{oreon_filedir}/rust-multiversion-macros0.8-devel.list

%changelog

%autochangelog
