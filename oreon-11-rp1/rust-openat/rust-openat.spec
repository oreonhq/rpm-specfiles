%global source0_hash 95aa7c05907b3ebde2610d602f4ddd992145cc6a84493647c30396f30ba83abe
%bcond check 0
%global debug_package %{nil}
%global crate openat
Name:           rust-openat
Version:        0.1.21
Release:        1%{?dist}
Summary:        A wrapper around openat, symlinkat, and similar system calls
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/openat
Source0:        https://static.crates.io/crates/openat/openat-%{version}.crate
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
Summary:        A wrapper around openat, symlinkat, and similar system calls
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
%files -n rust-openat-devel -f %{oreon_filedir}/rust-openat-devel.list

%changelog

%autochangelog
