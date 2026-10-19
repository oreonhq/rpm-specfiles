%global source0_hash 369e86b80fa7dc8c561dd9613a5bf25c59d2d3073cd66c47fd9e39802f0ecb58
%bcond check 0
%global debug_package %{nil}
%global crate refpool
Name:           rust-refpool
Version:        0.4.3
Release:        1%{?dist}
Summary:        Efficient memory pool with reference counting
License:        MPL-2.0+
URL:            https://crates.io/crates/refpool
Source0:        https://static.crates.io/crates/refpool/refpool-%{version}.crate
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
Summary:        Efficient memory pool with reference counting
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+default_impl-devel
Summary:        Efficient memory pool with reference counting
BuildArch:      noarch
%description -n %{name}+default_impl-devel

This package contains library source intended for building other packages which
use the "default_impl" feature of the "%{crate}" crate.

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
%files -n rust-refpool-devel -f %{oreon_filedir}/rust-refpool-devel.list

%changelog

%autochangelog
