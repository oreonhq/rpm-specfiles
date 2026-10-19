%global source0_hash 2b90d566bffbce6a75bd8b09a05aa8c2cb1fabb6cb348f8840c9e4c90a0d83b0
%bcond check 0
%global debug_package %{nil}
%global crate hyper-timeout
Name:           rust-hyper-timeout
Version:        0.5.2
Release:        1%{?dist}
Summary:        A connect, read and write timeout aware connector to be used with hyp...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hyper-timeout
Source0:        https://static.crates.io/crates/hyper-timeout/hyper-timeout-%{version}.crate
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
Summary:        A connect, read and write timeout aware connector to be used with hyp...
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
%files -n rust-hyper-timeout-devel -f %{oreon_filedir}/rust-hyper-timeout-devel.list

%changelog

%autochangelog
