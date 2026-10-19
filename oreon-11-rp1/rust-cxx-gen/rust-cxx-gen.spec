%global source0_hash 5010d4044b4ac8b18aca2341f3a6227aaf332ec8f5e38fcb93cba53451f2dc92
%bcond check 0
%global debug_package %{nil}
%global crate cxx-gen
Name:           rust-cxx-gen
Version:        0.7.202
Release:        1%{?dist}
Summary:        C++ code generator for integrating cxx crate into higher level tools
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cxx-gen
Source0:        https://static.crates.io/crates/cxx-gen/cxx-gen-%{version}.crate
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
Summary:        C++ code generator for integrating cxx crate into higher level tools
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
%files -n rust-cxx-gen-devel -f %{oreon_filedir}/rust-cxx-gen-devel.list

%changelog

%autochangelog
