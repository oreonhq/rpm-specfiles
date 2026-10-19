%global source0_hash 2cf3e4baa7f516441f58373f58aaf6e91a5dfa2e2b50e68a0d313b082014c61d
%bcond check 0
%global debug_package %{nil}
%global crate openat-ext
Name:           rust-openat-ext
Version:        0.2.3
Release:        1%{?dist}
Summary:        Extension methods for the openat crate
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/openat-ext
Source0:        https://static.crates.io/crates/openat-ext/openat-ext-%{version}.crate
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
Summary:        Extension methods for the openat crate
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
%files -n rust-openat-ext-devel -f %{oreon_filedir}/rust-openat-ext-devel.list

%changelog

%autochangelog
