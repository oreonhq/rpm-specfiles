%global source0_hash a432100a0b3a61085e75b5f89e9f42de73c0acb7dea5038b893697918105d822
%bcond check 0
%global debug_package %{nil}
%global crate primal-estimate
Name:           rust-primal-estimate
Version:        0.3.3
Release:        1%{?dist}
Summary:        State-of-the-art estimation of upper and lower bounds for π(n)
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/primal-estimate
Source0:        https://static.crates.io/crates/primal-estimate/primal-estimate-%{version}.crate
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
Summary:        State-of-the-art estimation of upper and lower bounds for π(n)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        State-of-the-art estimation of upper and lower bounds for π(n)
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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
%files -n rust-primal-estimate-devel -f %{oreon_filedir}/rust-primal-estimate-devel.list

%changelog

%autochangelog
