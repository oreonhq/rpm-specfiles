%global source0_hash 3d52eff69cd5e647efe296129160853a42795992097e8af39800e1060caeea9b
%bcond check 0
%global debug_package %{nil}
%global crate constant_time_eq
Name:           rust-constant_time_eq0.4
Version:        0.4.2
Release:        2%{?dist}
Summary:        Compares two equal-sized byte strings in constant time.
License:        CC0-1.0 OR MIT-0 OR Apache-2.0
URL:            https://crates.io/crates/constant_time_eq
Source0:        https://static.crates.io/crates/constant_time_eq/constant_time_eq-%{version}.crate
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
Summary:        Compares two equal-sized byte strings in constant time.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+count_instructions_test-devel
Summary:        Compares two equal-sized byte strings in constant time.
BuildArch:      noarch
%description -n %{name}+count_instructions_test-devel

This package contains library source intended for building other packages which
use the "count_instructions_test" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Compares two equal-sized byte strings in constant time.
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
%files -n rust-constant_time_eq0.4-devel -f %{oreon_filedir}/rust-constant_time_eq0.4-devel.list

%changelog

%autochangelog
