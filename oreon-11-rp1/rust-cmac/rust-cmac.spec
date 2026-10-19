%global source0_hash ac78aa94ce13e432b332a4d1bf2eff167d3a2520188ee05b337180a42fd2e62e
%bcond check 0
%global debug_package %{nil}
%global crate cmac
Name:           rust-cmac
Version:        0.8.0
Release:        1%{?dist}
Summary:        Generic implementation of Cipher-based Message Authentication Code
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cmac
Source0:        https://static.crates.io/crates/cmac/cmac-%{version}.crate
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

%package     -n %{name}+std-devel
Summary:        Generic implementation of Cipher-based Message Authentication Code
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Generic implementation of Cipher-based Message Authentication Code
BuildArch:      noarch
%description -n %{name}+zeroize-devel

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

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
%files -n rust-cmac-devel -f %{oreon_filedir}/rust-cmac-devel.list

%changelog

%autochangelog
