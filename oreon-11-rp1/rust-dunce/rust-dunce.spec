%global source0_hash 92773504d58c093f6de2459af4af33faa518c13451eb8f2b5698ed3d36e7c813
%bcond check 1
%global debug_package %{nil}
%global crate dunce
Name:           rust-dunce
Version:        1.0.5
Release:        1%{?dist}
Summary:        Normalize Windows paths to the most compatible format, avoiding
License:        CC0-1.0 OR MIT-0 OR Apache-2.0
URL:            https://crates.io/crates/dunce
Source0:        https://static.crates.io/crates/dunce/dunce-%{version}.crate
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
Summary:        Normalize Windows paths to the most compatible format, avoiding
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
%files -n rust-dunce-devel -f %{oreon_filedir}/rust-dunce-devel.list

%changelog

%autochangelog
