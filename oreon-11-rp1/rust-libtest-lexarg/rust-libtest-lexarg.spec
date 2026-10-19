%global source0_hash 914e11e515e22a1b2a0aac76c0615e6417d470789c2f0433a0598a5b6aae491f
%bcond check 1
%global debug_package %{nil}
%global crate libtest-lexarg
Name:           rust-libtest-lexarg
Version:        0.0.3
Release:        1%{?dist}
Summary:        libtest-compatible argument parser
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/libtest-lexarg
Source0:        https://static.crates.io/crates/libtest-lexarg/libtest-lexarg-%{version}.crate
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
Summary:        libtest-compatible argument parser
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
%files -n rust-libtest-lexarg-devel -f %{oreon_filedir}/rust-libtest-lexarg-devel.list

%changelog

%autochangelog
