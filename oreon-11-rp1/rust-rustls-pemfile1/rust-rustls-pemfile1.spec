%global source0_hash 1c74cae0a4cf6ccbbf5f359f08efdf8ee7e1dc532573bf0db71968cb56b1448c
%bcond check 0
%global debug_package %{nil}
%global crate rustls-pemfile
Name:           rust-rustls-pemfile1
Version:        1.0.4
Release:        1%{?dist}
Summary:        Basic .pem file parser for keys and certificates
License:        Apache-2.0 OR ISC OR MIT
URL:            https://crates.io/crates/rustls-pemfile
Source0:        https://static.crates.io/crates/rustls-pemfile/rustls-pemfile-%{version}.crate
Patch:          rustls-pemfile-fix-metadata.diff
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
Summary:        Basic .pem file parser for keys and certificates
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
%files -n rust-rustls-pemfile1-devel -f %{oreon_filedir}/rust-rustls-pemfile1-devel.list

%changelog

%autochangelog
