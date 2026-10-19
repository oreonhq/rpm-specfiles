%global source0_hash 7f4c021e1093a56626774e81216a4ce732a735e5bad4868a03f3ed65ca0c3919
%bcond check 0
%global debug_package %{nil}
%global crate proc-macro-crate
Name:           rust-proc-macro-crate1
Version:        1.3.1
Release:        1%{?dist}
Summary:        Replacement for crate (macro_rules keyword) in proc-macros
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/proc-macro-crate
Source0:        https://static.crates.io/crates/proc-macro-crate/proc-macro-crate-%{version}.crate
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
Summary:        Replacement for crate (macro_rules keyword) in proc-macros
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
%files -n rust-proc-macro-crate1-devel -f %{oreon_filedir}/rust-proc-macro-crate1-devel.list

%changelog

%autochangelog
