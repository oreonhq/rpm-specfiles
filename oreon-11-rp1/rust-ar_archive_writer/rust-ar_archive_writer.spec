%global source0_hash 73cd58deff2140a0a8eae87e417bd01db68a33e148aa93d1e8cd837e55e312b6
%bcond check 0
%global debug_package %{nil}
%global crate ar_archive_writer
Name:           rust-ar_archive_writer
Version:        0.5.3
Release:        1%{?dist}
Summary:        A writer for object file ar archives
License:        Apache-2.0 WITH LLVM-exception
URL:            https://crates.io/crates/ar_archive_writer
Source0:        https://static.crates.io/crates/ar_archive_writer/ar_archive_writer-%{version}.crate
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
Summary:        A writer for object file ar archives
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
%files -n rust-ar_archive_writer-devel -f %{oreon_filedir}/rust-ar_archive_writer-devel.list

%changelog

%autochangelog
