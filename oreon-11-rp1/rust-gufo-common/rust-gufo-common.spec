%global source0_hash d583cdde9eb6985dbb6e596d27677e5d353d5eee44763cbf7c7ead3147d337bf
%bcond check 1
%global debug_package %{nil}
%global crate gufo-common
Name:           rust-gufo-common
Version:        2.0.0
Release:        1%{?dist}
Summary:        Common features used in gufo crates
License:        MPL-2.0 OR LGPL-2.1-or-later
URL:            https://crates.io/crates/gufo-common
Source0:        https://static.crates.io/crates/gufo-common/gufo-common-%{version}.crate
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
Summary:        Common features used in gufo crates
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Common features used in gufo crates
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Common features used in gufo crates
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+zvariant-devel
Summary:        Common features used in gufo crates
BuildArch:      noarch
%description -n %{name}+zvariant-devel

This package contains library source intended for building other packages which
use the "zvariant" feature of the "%{crate}" crate.

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
%files -n rust-gufo-common-devel -f %{oreon_filedir}/rust-gufo-common-devel.list

%changelog

%autochangelog
