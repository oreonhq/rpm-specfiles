%global source0_hash 05f360fc0b24296329c78fda852a1e9ae82de9cf7b27dae4b7f62f118f77b9ed
%bcond check 0
%global debug_package %{nil}
%global crate wyz
Name:           rust-wyz
Version:        0.5.1
Release:        1%{?dist}
Summary:        myrrlyn’s utility collection
License:        MIT
URL:            https://crates.io/crates/wyz
Source0:        https://static.crates.io/crates/wyz/wyz-%{version}.crate
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
Summary:        myrrlyn’s utility collection
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        myrrlyn’s utility collection
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+garbage-devel
Summary:        myrrlyn’s utility collection
BuildArch:      noarch
%description -n %{name}+garbage-devel

This package contains library source intended for building other packages which
use the "garbage" feature of the "%{crate}" crate.

%package     -n %{name}+once_cell-devel
Summary:        myrrlyn’s utility collection
BuildArch:      noarch
%description -n %{name}+once_cell-devel

This package contains library source intended for building other packages which
use the "once_cell" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        myrrlyn’s utility collection
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+typemap-devel
Summary:        myrrlyn’s utility collection
BuildArch:      noarch
%description -n %{name}+typemap-devel

This package contains library source intended for building other packages which
use the "typemap" feature of the "%{crate}" crate.

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
%files -n rust-wyz-devel -f %{oreon_filedir}/rust-wyz-devel.list

%changelog

%autochangelog
