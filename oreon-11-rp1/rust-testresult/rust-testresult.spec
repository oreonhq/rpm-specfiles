%global source0_hash 614b328ff036a4ef882c61570f72918f7e9c5bee1da33f8e7f91e01daee7e56c
%bcond check 1
%global debug_package %{nil}
%global crate testresult
Name:           rust-testresult
Version:        0.4.1
Release:        1%{?dist}
Summary:        TestResult type for concise and precise test failures
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/testresult
Source0:        https://static.crates.io/crates/testresult/testresult-%{version}.crate
Patch:          testresult-fix-metadata.diff
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
Summary:        TestResult type for concise and precise test failures
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
%files -n rust-testresult-devel -f %{oreon_filedir}/rust-testresult-devel.list

%changelog

%autochangelog
