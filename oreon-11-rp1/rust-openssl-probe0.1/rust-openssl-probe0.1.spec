%global source0_hash d05e27ee213611ffe7d6348b942e8f942b37114c00cc03cec254295a4a17852e
%bcond check 1
%global debug_package %{nil}
%global crate openssl-probe
Name:           rust-openssl-probe0.1
Version:        0.1.6
Release:        1%{?dist}
Summary:        Tool for helping to find SSL certificate locations on the system for OpenSSL
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/openssl-probe
Source0:        https://static.crates.io/crates/openssl-probe/openssl-probe-%{version}.crate
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
Summary:        Tool for helping to find SSL certificate locations on the system for OpenSSL
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
%files -n rust-openssl-probe0.1-devel -f %{oreon_filedir}/rust-openssl-probe0.1-devel.list

%changelog

%autochangelog
