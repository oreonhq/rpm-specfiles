%global source0_hash 9e7ab1c31cd9e92e56b63f4d85a6c6a854880aaf433191623f5d50e152dcdbc2
%bcond check 0
%global debug_package %{nil}
%global crate trybuild2
Name:           rust-trybuild2
Version:        1.2.0
Release:        1%{?dist}
Summary:        Test harness for ui tests of compiler diagnostics
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/trybuild2
Source0:        https://static.crates.io/crates/trybuild2/trybuild2-%{version}.crate
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
Summary:        Test harness for ui tests of compiler diagnostics
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+diff-devel
Summary:        Test harness for ui tests of compiler diagnostics
BuildArch:      noarch
%description -n %{name}+diff-devel

This package contains library source intended for building other packages which
use the "diff" feature of the "%{crate}" crate.

%package     -n %{name}+dissimilar-devel
Summary:        Test harness for ui tests of compiler diagnostics
BuildArch:      noarch
%description -n %{name}+dissimilar-devel

This package contains library source intended for building other packages which
use the "dissimilar" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -a
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-trybuild2-devel -f %{oreon_filedir}/rust-trybuild2-devel.list

%changelog

%autochangelog
