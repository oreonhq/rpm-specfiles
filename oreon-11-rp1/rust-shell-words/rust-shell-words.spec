%global source0_hash dc6fe69c597f9c37bfeeeeeb33da3530379845f10be461a66d16d03eca2ded77
%bcond check 0
%global debug_package %{nil}
%global crate shell-words
Name:           rust-shell-words
Version:        1.1.1
Release:        1%{?dist}
Summary:        Process command line according to parsing rules of UNIX shell
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/shell-words
Source0:        https://static.crates.io/crates/shell-words/shell-words-%{version}.crate
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
Summary:        Process command line according to parsing rules of UNIX shell
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Process command line according to parsing rules of UNIX shell
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-shell-words-devel -f %{oreon_filedir}/rust-shell-words-devel.list

%changelog

%autochangelog
