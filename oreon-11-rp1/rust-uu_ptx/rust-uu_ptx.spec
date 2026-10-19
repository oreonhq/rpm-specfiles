%global source0_hash 268dc2ca3624228b9929fa60c843d54affa9024586e7f553a1484d029f6e9d99
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_ptx
Name:           rust-uu_ptx
Version:        0.7.0
Release:        1%{?dist}
Summary:        ptx ~ (uutils) display a permuted index of input
License:        MIT
URL:            https://crates.io/crates/uu_ptx
Source0:        https://static.crates.io/crates/uu_ptx/uu_ptx-%{version}.crate
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
Summary:        ptx ~ (uutils) display a permuted index of input
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
%files -n rust-uu_ptx-devel -f %{oreon_filedir}/rust-uu_ptx-devel.list

%changelog

%autochangelog
