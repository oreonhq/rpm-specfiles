%global source0_hash 8267aa6001e25494f3015f9663bbd88a18240c74483afa5f0934a1b3e4c388e9
%bcond check 0
%global debug_package %{nil}
%global crate is-macro
Name:           rust-is-macro
Version:        0.3.8
Release:        1%{?dist}
Summary:        Derive methods for using custom enums like Option / Result
License:        Apache-2.0
URL:            https://crates.io/crates/is-macro
Source0:        https://static.crates.io/crates/is-macro/is-macro-%{version}.crate
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
Summary:        Derive methods for using custom enums like Option / Result
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
%files -n rust-is-macro-devel -f %{oreon_filedir}/rust-is-macro-devel.list

%changelog

%autochangelog
