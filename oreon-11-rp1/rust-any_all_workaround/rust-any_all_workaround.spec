%global source0_hash 88fea40735f2cc320a5133ce772d39c571bd6c9b0d4c1a326926eecdd5af2e86
%bcond check 0
%global debug_package %{nil}
%global crate any_all_workaround
Name:           rust-any_all_workaround
Version:        0.1.0
Release:        1%{?dist}
Summary:        Workaround for bad LLVM codegen for boolean reductions on 32-bit ARM
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/any_all_workaround
Source0:        https://static.crates.io/crates/any_all_workaround/any_all_workaround-%{version}.crate
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
Summary:        Workaround for bad LLVM codegen for boolean reductions on 32-bit ARM
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
%files -n rust-any_all_workaround-devel -f %{oreon_filedir}/rust-any_all_workaround-devel.list

%changelog

%autochangelog
