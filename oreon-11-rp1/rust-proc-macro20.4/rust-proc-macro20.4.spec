%global source0_hash cf3d2011ab5c909338f7887f4fc896d35932e29146c12c8d01da6b22a80ba759
%bcond check 0
%global debug_package %{nil}
%global crate proc-macro2
Name:           rust-proc-macro20.4
Version:        0.4.30
Release:        1%{?dist}
Summary:        A stable implementation of the upcoming new `proc_macro` API. Comes w...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/proc-macro2
Source0:        https://static.crates.io/crates/proc-macro2/proc-macro2-%{version}.crate
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
Summary:        A stable implementation of the upcoming new `proc_macro` API. Comes w...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        A stable implementation of the upcoming new `proc_macro` API. Comes w...
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+proc-macro-devel
Summary:        A stable implementation of the upcoming new `proc_macro` API. Comes w...
BuildArch:      noarch
%description -n %{name}+proc-macro-devel

This package contains library source intended for building other packages which
use the "proc-macro" feature of the "%{crate}" crate.

%package     -n %{name}+span-locations-devel
Summary:        A stable implementation of the upcoming new `proc_macro` API. Comes w...
BuildArch:      noarch
%description -n %{name}+span-locations-devel

This package contains library source intended for building other packages which
use the "span-locations" feature of the "%{crate}" crate.

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
%files -n rust-proc-macro20.4-devel -f %{oreon_filedir}/rust-proc-macro20.4-devel.list

%changelog

%autochangelog
