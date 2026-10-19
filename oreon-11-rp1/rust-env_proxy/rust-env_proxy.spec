%global source0_hash 3a5019be18538406a43b5419a5501461f0c8b49ea7dfda0cfc32f4e51fc44be1
%bcond check 0
%global debug_package %{nil}
%global crate env_proxy
Name:           rust-env_proxy
Version:        0.4.1
Release:        1%{?dist}
Summary:        Determination of proxy parameters for a URL from the environment
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/env_proxy
Source0:        https://static.crates.io/crates/env_proxy/env_proxy-%{version}.crate
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
Summary:        Determination of proxy parameters for a URL from the environment
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
%files -n rust-env_proxy-devel -f %{oreon_filedir}/rust-env_proxy-devel.list

%changelog

%autochangelog
