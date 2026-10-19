%global source0_hash 96de42df36bb9bba5542fe9f1a054b8cc87e172759a1868aa05c1f3acc89dfc5
%bcond check 0
%global debug_package %{nil}
%global crate proc-macro-error-attr2
Name:           rust-proc-macro-error-attr2
Version:        2.0.0
Release:        1%{?dist}
Summary:        Attribute macro for the proc-macro-error2 crate
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/proc-macro-error-attr2
Source0:        https://static.crates.io/crates/proc-macro-error-attr2/proc-macro-error-attr2-%{version}.crate
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
Summary:        Attribute macro for the proc-macro-error2 crate
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
%files -n rust-proc-macro-error-attr2-devel -f %{oreon_filedir}/rust-proc-macro-error-attr2-devel.list

%changelog

%autochangelog
