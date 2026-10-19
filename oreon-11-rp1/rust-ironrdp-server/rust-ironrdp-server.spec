%global source0_hash 1d3922b23ad9f262b932d42fa37df87f7e45c2d12f45433c0cc084f8762fb09a
%bcond check 1
%global debug_package %{nil}
%global crate ironrdp-server
Name:           rust-ironrdp-server
Version:        0.13.0
Release:        1%{?dist}
Summary:        Extendable skeleton for implementing custom RDP servers
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ironrdp-server
Source0:        https://static.crates.io/crates/ironrdp-server/ironrdp-server-%{version}.crate
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
Summary:        Extendable skeleton for implementing custom RDP servers
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+helper-devel
Summary:        Extendable skeleton for implementing custom RDP servers
BuildArch:      noarch
%description -n %{name}+helper-devel

This package contains library source intended for building other packages which
use the "helper" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        Extendable skeleton for implementing custom RDP servers
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

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
%files -n rust-ironrdp-server-devel -f %{oreon_filedir}/rust-ironrdp-server-devel.list

%changelog

%autochangelog
