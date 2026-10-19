%global source0_hash 7a949c44fcacbbbb7ada007dc7acb34603dd97cd47de5d054f2b6493ecebb483
%bcond check 1
%global debug_package %{nil}
%global crate ctor-proc-macro
Name:           rust-ctor-proc-macro
Version:        0.0.13
Release:        1%{?dist}
Summary:        Proc-macro support for the ctor crate
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/ctor-proc-macro
Source0:        https://static.crates.io/crates/ctor-proc-macro/ctor-proc-macro-%{version}.crate
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
Summary:        Proc-macro support for the ctor crate
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
%files -n rust-ctor-proc-macro-devel -f %{oreon_filedir}/rust-ctor-proc-macro-devel.list

%changelog

%autochangelog
