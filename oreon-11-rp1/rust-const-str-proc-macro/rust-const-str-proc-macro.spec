%global source0_hash 1c7e7913ec01ed98b697e62f8d3fd63c86dc6cccaf983c7eebc64d0e563b0ad9
%bcond check 1
%global debug_package %{nil}
%global crate const-str-proc-macro
Name:           rust-const-str-proc-macro
Version:        1.1.0
Release:        1%{?dist}
Summary:        Compile-time string operations
License:        MIT
URL:            https://crates.io/crates/const-str-proc-macro
Source0:        https://static.crates.io/crates/const-str-proc-macro/const-str-proc-macro-%{version}.crate
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
Summary:        Compile-time string operations
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+heck-devel
Summary:        Compile-time string operations
BuildArch:      noarch
%description -n %{name}+heck-devel

This package contains library source intended for building other packages which
use the "heck" feature of the "%{crate}" crate.

%package     -n %{name}+http-devel
Summary:        Compile-time string operations
BuildArch:      noarch
%description -n %{name}+http-devel

This package contains library source intended for building other packages which
use the "http" feature of the "%{crate}" crate.

%package     -n %{name}+regex-devel
Summary:        Compile-time string operations
BuildArch:      noarch
%description -n %{name}+regex-devel

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

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
%files -n rust-const-str-proc-macro-devel -f %{oreon_filedir}/rust-const-str-proc-macro-devel.list

%changelog

%autochangelog
