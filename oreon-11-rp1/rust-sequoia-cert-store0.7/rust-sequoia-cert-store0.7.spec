%global source0_hash 966d3841a6ea69325719c742b8123c7757d18f0f2d4f728ec7b15e849df3ba35
%bcond check 1
%global debug_package %{nil}
%global crate sequoia-cert-store
Name:           rust-sequoia-cert-store0.7
Version:        0.7.6
Release:        1%{?dist}
Summary:        Certificate database interface
License:        LGPL-2.0-or-later
URL:            https://crates.io/crates/sequoia-cert-store
Source0:        https://static.crates.io/crates/sequoia-cert-store/sequoia-cert-store-%{version}.crate
Patch:          sequoia-cert-store-fix-metadata-auto.diff
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
Summary:        Certificate database interface
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+keyserver-devel
Summary:        Certificate database interface
BuildArch:      noarch
%description -n %{name}+keyserver-devel

This package contains library source intended for building other packages which
use the "keyserver" feature of the "%{crate}" crate.

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
%files -n rust-sequoia-cert-store0.7-devel -f %{oreon_filedir}/rust-sequoia-cert-store0.7-devel.list

%changelog

%autochangelog
