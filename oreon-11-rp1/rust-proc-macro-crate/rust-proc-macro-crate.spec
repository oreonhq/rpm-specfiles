%global source0_hash e67ba7e9b2b56446f1d419b1d807906278ffa1a658a8a5d8a39dcb1f5a78614f
%bcond check 0
%global debug_package %{nil}
%global crate proc-macro-crate
Name:           rust-proc-macro-crate
Version:        3.5.0
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
%files -n rust-proc-macro-crate-devel -f %{oreon_filedir}/rust-proc-macro-crate-devel.list

%changelog

%autochangelog
