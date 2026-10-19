%global source0_hash abd57806937c9cc163efc8ea3910e00a62e2aeb0b8119f1793a978088f8f6b04
%bcond check 0
%global debug_package %{nil}
%global crate deunicode
Name:           rust-deunicode
Version:        1.6.2
Release:        1%{?dist}
Summary:        Convert Unicode strings to pure ASCII by intelligently transliteratin...
License:        BSD-3-Clause
URL:            https://crates.io/crates/deunicode
Source0:        https://static.crates.io/crates/deunicode/deunicode-%{version}.crate
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
Summary:        Convert Unicode strings to pure ASCII by intelligently transliteratin...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Convert Unicode strings to pure ASCII by intelligently transliteratin...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

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
%files -n rust-deunicode-devel -f %{oreon_filedir}/rust-deunicode-devel.list

%changelog

%autochangelog
