%global source0_hash 6d92b727cb45d33ae956f7f46b966b25f1bc712092aeef9dba5ac798fc89f720
%bcond check 0
%global debug_package %{nil}
%global crate testing_logger
Name:           rust-testing_logger
Version:        0.1.1
Release:        1%{?dist}
Summary:        Supports writing tests to verify log crate calls
License:        BSD-3-Clause
URL:            https://crates.io/crates/testing_logger
Source0:        https://static.crates.io/crates/testing_logger/testing_logger-%{version}.crate
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
Summary:        Supports writing tests to verify log crate calls
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
%files -n rust-testing_logger-devel -f %{oreon_filedir}/rust-testing_logger-devel.list

%changelog

%autochangelog
