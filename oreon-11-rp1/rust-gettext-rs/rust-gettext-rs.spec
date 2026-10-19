%global source0_hash 9df5e3fa8c077b15fdfa8ce130e2bc73d663b8aaa6d51b71421b8659980b1d80
%bcond check 1
%global debug_package %{nil}
%global crate gettext-rs
Name:           rust-gettext-rs
Version:        0.8.0
Release:        1%{?dist}
Summary:        Safe bindings for gettext
License:        MIT
URL:            https://crates.io/crates/gettext-rs
Source0:        https://static.crates.io/crates/gettext-rs/gettext-rs-%{version}.crate
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
Summary:        Safe bindings for gettext
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+gettext-system-devel
Summary:        Safe bindings for gettext
BuildArch:      noarch
%description -n %{name}+gettext-system-devel

This package contains library source intended for building other packages which
use the "gettext-system" feature of the "%{crate}" crate.

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
%files -n rust-gettext-rs-devel -f %{oreon_filedir}/rust-gettext-rs-devel.list

%changelog

%autochangelog
