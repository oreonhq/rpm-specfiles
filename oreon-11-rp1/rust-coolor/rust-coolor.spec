%global source0_hash 980c2afde4af43d6a05c5be738f9eae595cff86dce1f38f88b95058a98c027f3
%bcond check 0
%global debug_package %{nil}
%global crate coolor
Name:           rust-coolor
Version:        1.1.0
Release:        1%{?dist}
Summary:        conversion between color formats
License:        MIT
URL:            https://crates.io/crates/coolor
Source0:        https://static.crates.io/crates/coolor/coolor-%{version}.crate
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
Summary:        conversion between color formats
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+crossterm-devel
Summary:        conversion between color formats
BuildArch:      noarch
%description -n %{name}+crossterm-devel

This package contains library source intended for building other packages which
use the "crossterm" feature of the "%{crate}" crate.

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
%files -n rust-coolor-devel -f %{oreon_filedir}/rust-coolor-devel.list

%changelog

%autochangelog
