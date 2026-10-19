%global source0_hash da25490ff9892aab3fcf7c36f08cfb902dd3e71ca0f9f9517bea02a73a5ce38c
%bcond check 0
%global debug_package %{nil}
%global crate proc-macro-error
Name:           rust-proc-macro-error
Version:        1.0.4
Release:        1%{?dist}
Summary:        Almost drop-in replacement to panics in proc-macros
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/proc-macro-error
Source0:        https://static.crates.io/crates/proc-macro-error/proc-macro-error-%{version}.crate
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
Summary:        Almost drop-in replacement to panics in proc-macros
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+syn-devel
Summary:        Almost drop-in replacement to panics in proc-macros
BuildArch:      noarch
%description -n %{name}+syn-devel

This package contains library source intended for building other packages which
use the "syn" feature of the "%{crate}" crate.

%package     -n %{name}+syn-error-devel
Summary:        Almost drop-in replacement to panics in proc-macros
BuildArch:      noarch
%description -n %{name}+syn-error-devel

This package contains library source intended for building other packages which
use the "syn-error" feature of the "%{crate}" crate.

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
%files -n rust-proc-macro-error-devel -f %{oreon_filedir}/rust-proc-macro-error-devel.list

%changelog

%autochangelog
