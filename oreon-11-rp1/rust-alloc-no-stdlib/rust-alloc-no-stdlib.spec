%global source0_hash cc7bb162ec39d46ab1ca8c77bf72e890535becd1751bb45f64c597edb4c8c6b3
%bcond check 0
%global debug_package %{nil}
%global crate alloc-no-stdlib
Name:           rust-alloc-no-stdlib
Version:        2.0.4
Release:        1%{?dist}
Summary:        A dynamic allocator that may be used with or without the stdlib. This...
License:        BSD-3-Clause
URL:            https://crates.io/crates/alloc-no-stdlib
Source0:        https://static.crates.io/crates/alloc-no-stdlib/alloc-no-stdlib-%{version}.crate
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

%package     -n %{name}+unsafe-devel
Summary:        A dynamic allocator that may be used with or without the stdlib. This...
BuildArch:      noarch
%description -n %{name}+unsafe-devel

This package contains library source intended for building other packages which
use the "unsafe" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
find . -type f -name '*.rs' -exec chmod -x {} +
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
%files -n rust-alloc-no-stdlib-devel -f %{oreon_filedir}/rust-alloc-no-stdlib-devel.list

%changelog

%autochangelog

