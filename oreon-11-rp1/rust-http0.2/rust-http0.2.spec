%global source0_hash 601cbb57e577e2f5ef5be8e7b83f0f63994f25aa94d673e54a92d5c516d101f1
%bcond check 0
%global debug_package %{nil}
%global crate http
Name:           rust-http0.2
Version:        0.2.12
Release:        1%{?dist}
Summary:        A set of types for representing HTTP requests and responses.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/http
Source0:        https://static.crates.io/crates/http/http-%{version}.crate
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
Summary:        A set of types for representing HTTP requests and responses.
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
%files -n rust-http0.2-devel -f %{oreon_filedir}/rust-http0.2-devel.list

%changelog

%autochangelog
