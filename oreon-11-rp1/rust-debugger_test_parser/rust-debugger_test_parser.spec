%global source0_hash 91f5b4d1a7e92279513009c540f67f0798b42ac669171f6907d8ee820cfae0c4
%bcond check 1
%global debug_package %{nil}
%global crate debugger_test_parser
Name:           rust-debugger_test_parser
Version:        0.2.0
Release:        1%{?dist}
Summary:        Provides a library for parsing the output of a debugger and
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/debugger_test_parser
Source0:        https://static.crates.io/crates/debugger_test_parser/debugger_test_parser-%{version}.crate
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
Summary:        Provides a library for parsing the output of a debugger and
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
%files -n rust-debugger_test_parser-devel -f %{oreon_filedir}/rust-debugger_test_parser-devel.list

%changelog

%autochangelog
