%global source0_hash 0103b1cef7ec0cf76490e969665504990193874ea05c85ff9bab8b911d0a0564
%bcond check 0
%global debug_package %{nil}
%global crate potential_utf
Name:           rust-potential_utf
Version:        0.1.5
Release:        2%{?dist}
Summary:        Unvalidated string and character types
License:        Unicode-3.0
URL:            https://crates.io/crates/potential_utf
Source0:        https://static.crates.io/crates/potential_utf/potential_utf-%{version}.crate
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
Summary:        Unvalidated string and character types
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Unvalidated string and character types
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+databake-devel
Summary:        Unvalidated string and character types
BuildArch:      noarch
%description -n %{name}+databake-devel

This package contains library source intended for building other packages which
use the "databake" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Unvalidated string and character types
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+writeable-devel
Summary:        Unvalidated string and character types
BuildArch:      noarch
%description -n %{name}+writeable-devel

This package contains library source intended for building other packages which
use the "writeable" feature of the "%{crate}" crate.

%package     -n %{name}+zerovec-devel
Summary:        Unvalidated string and character types
BuildArch:      noarch
%description -n %{name}+zerovec-devel

This package contains library source intended for building other packages which
use the "zerovec" feature of the "%{crate}" crate.

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
%files -n rust-potential_utf-devel -f %{oreon_filedir}/rust-potential_utf-devel.list

%changelog

%autochangelog
