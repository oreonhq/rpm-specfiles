%global source0_hash ea6438ba0a08d81529c69b36700fa2f95837bfe3e776ab39cde9c14d9149da88
%bcond check 1
%global debug_package %{nil}
%global crate async-process
Name:           rust-async-process1
Version:        1.8.1
Release:        1%{?dist}
Summary:        Async interface for working with processes
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/async-process
Source0:        https://static.crates.io/crates/async-process/async-process-%{version}.crate
Patch:          async-process-fix-metadata-auto.diff
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
Summary:        Async interface for working with processes
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
%files -n rust-async-process1-devel -f %{oreon_filedir}/rust-async-process1-devel.list

%changelog

%autochangelog
