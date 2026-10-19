%global source0_hash e5a7d05ea6aea7e9e64d25b9156ba2fee3fdd659e34e41063cd2fc7cd020d7f4
%bcond check 0
%global debug_package %{nil}
%global crate alloca
Name:           rust-alloca
Version:        0.4.0
Release:        1%{?dist}
Summary:        Mostly safe wrapper for alloca
License:        MIT
URL:            https://crates.io/crates/alloca
Source0:        https://static.crates.io/crates/alloca/alloca-%{version}.crate
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
Summary:        Mostly safe wrapper for alloca
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+stack-clash-protection-devel
Summary:        Mostly safe wrapper for alloca
BuildArch:      noarch
%description -n %{name}+stack-clash-protection-devel

This package contains library source intended for building other packages which
use the "stack-clash-protection" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
rm -f %{buildroot}%{_bindir}/alloca
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-alloca-devel -f %{oreon_filedir}/rust-alloca-devel.list

%changelog

%autochangelog
