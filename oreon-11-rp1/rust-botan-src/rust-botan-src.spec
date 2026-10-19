%global source0_hash e19afa24979ebb37fd22894895219e5f6bb6ba3d98f87c4aa147e59f4860efb7
%bcond check 0
%global debug_package %{nil}
%global crate botan-src
Name:           rust-botan-src
Version:        0.31300.1
Release:        1%{?dist}
Summary:        Sources of Botan cryptography library
License:        MIT
URL:            https://crates.io/crates/botan-src
Source0:        https://static.crates.io/crates/botan-src/botan-src-%{version}.crate
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
Summary:        Sources of Botan cryptography library
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
%files -n rust-botan-src-devel -f %{oreon_filedir}/rust-botan-src-devel.list

%changelog

%autochangelog
