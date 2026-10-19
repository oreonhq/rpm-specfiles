%global source0_hash cceeca12036b18857d4c773373419185ffa057b32b0c87a447a1861a06c5ddc3
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_nproc
Name:           rust-uu_nproc
Version:        0.7.0
Release:        1%{?dist}
Summary:        nproc ~ (uutils) display the number of processing units available
License:        MIT
URL:            https://crates.io/crates/uu_nproc
Source0:        https://static.crates.io/crates/uu_nproc/uu_nproc-%{version}.crate
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
Summary:        nproc ~ (uutils) display the number of processing units available
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
%files -n rust-uu_nproc-devel -f %{oreon_filedir}/rust-uu_nproc-devel.list

%changelog

%autochangelog
