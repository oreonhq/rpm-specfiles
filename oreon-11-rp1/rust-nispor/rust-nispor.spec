%global source0_hash 06ab2c5ba2edc4befae3bd67e5d1181c64f73d687dae9e1b06f68caf490b0345
%bcond check 0
%global debug_package %{nil}
%global crate nispor
Name:           rust-nispor
Version:        2.0.2
Release:        1%{?dist}
Summary:        Unified interface for Linux network state querying
License:        Apache-2.0
URL:            https://crates.io/crates/nispor
Source0:        https://static.crates.io/crates/nispor/nispor-%{version}.crate
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
Summary:        Unified interface for Linux network state querying
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
%files -n rust-nispor-devel -f %{oreon_filedir}/rust-nispor-devel.list

%changelog

%autochangelog
