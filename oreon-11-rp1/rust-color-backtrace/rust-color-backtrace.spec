%global source0_hash 01fd62bba8d0ebaacae8e3faf5c05d3c80b215ea6a5dfe6069619bcd8d72451d
%bcond check 1
%global debug_package %{nil}
%global crate color-backtrace
Name:           rust-color-backtrace
Version:        0.7.4
Release:        1%{?dist}
Summary:        Colorful panic backtraces
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/color-backtrace
Source0:        https://static.crates.io/crates/color-backtrace/color-backtrace-%{version}.crate
Patch:          color-backtrace-fix-metadata.diff
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
Summary:        Colorful panic backtraces
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+resolve-modules-devel
Summary:        Colorful panic backtraces
BuildArch:      noarch
%description -n %{name}+resolve-modules-devel

This package contains library source intended for building other packages which
use the "resolve-modules" feature of the "%{crate}" crate.

%package     -n %{name}+use-backtrace-crate-devel
Summary:        Colorful panic backtraces
BuildArch:      noarch
%description -n %{name}+use-backtrace-crate-devel

This package contains library source intended for building other packages which
use the "use-backtrace-crate" feature of the "%{crate}" crate.

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
%files -n rust-color-backtrace-devel -f %{oreon_filedir}/rust-color-backtrace-devel.list

%changelog

%autochangelog
