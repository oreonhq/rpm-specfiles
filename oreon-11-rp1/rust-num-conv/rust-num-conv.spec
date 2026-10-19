%global source0_hash 521739c6d2bac4aa25192232afe6841231376b2b26d4d9fae5ecf8ca5772e441
%bcond check 0
%global debug_package %{nil}
%global crate num-conv
Name:           rust-num-conv
Version:        0.2.2
Release:        1%{?dist}
Summary:        `num_conv` is a crate to convert between integer types without using...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/num-conv
Source0:        https://static.crates.io/crates/num-conv/num-conv-%{version}.crate
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
Summary:        `num_conv` is a crate to convert between integer types without using...
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
%files -n rust-num-conv-devel -f %{oreon_filedir}/rust-num-conv-devel.list

%changelog

%autochangelog
