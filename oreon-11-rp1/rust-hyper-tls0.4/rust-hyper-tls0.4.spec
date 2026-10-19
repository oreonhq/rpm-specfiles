%global source0_hash d979acc56dcb5b8dddba3917601745e877576475aa046df3226eabdecef78eed
%bcond check 0
%global debug_package %{nil}
%global crate hyper-tls
Name:           rust-hyper-tls0.4
Version:        0.4.3
Release:        1%{?dist}
Summary:        Default TLS implementation for use with hyper
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hyper-tls
Source0:        https://static.crates.io/crates/hyper-tls/hyper-tls-%{version}.crate
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

%package     -n %{name}+vendored-devel
Summary:        Default TLS implementation for use with hyper
BuildArch:      noarch
%description -n %{name}+vendored-devel

This package contains library source intended for building other packages which
use the "vendored" feature of the "%{crate}" crate.

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
%files -n rust-hyper-tls0.4-devel -f %{oreon_filedir}/rust-hyper-tls0.4-devel.list

%changelog

%autochangelog
