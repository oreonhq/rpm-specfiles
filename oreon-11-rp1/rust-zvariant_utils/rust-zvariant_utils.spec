%global source0_hash 90cb9383f9b45290407a1258b202d3f8f01db719eb60b4e4055c6375af4fc7c7
%bcond check 0
%global debug_package %{nil}
%global crate zvariant_utils
Name:           rust-zvariant_utils
Version:        3.5.0
Release:        1%{?dist}
Summary:        Various utilities used internally by the zvariant crate.
License:        MIT
URL:            https://crates.io/crates/zvariant_utils
Source0:        https://static.crates.io/crates/zvariant_utils/zvariant_utils-%{version}.crate
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
Summary:        Various utilities used internally by the zvariant crate.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+gvariant-devel
Summary:        Various utilities used internally by the zvariant crate.
BuildArch:      noarch
%description -n %{name}+gvariant-devel

This package contains library source intended for building other packages which
use the "gvariant" feature of the "%{crate}" crate.

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
%files -n rust-zvariant_utils-devel -f %{oreon_filedir}/rust-zvariant_utils-devel.list

%changelog

%autochangelog
