%global source0_hash ca2a8f2913ee65f60facd6a5905613afaa448497a0230cc41ce022d93290bc2c
%bcond check 0
%global debug_package %{nil}
%global crate http-body
Name:           rust-http-body
Version:        1.1.0
Release:        1%{?dist}
Summary:        Trait representing an asynchronous, streaming, HTTP request or respon...
License:        MIT
URL:            https://crates.io/crates/http-body
Source0:        https://static.crates.io/crates/http-body/http-body-%{version}.crate
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
Summary:        Trait representing an asynchronous, streaming, HTTP request or respon...
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
%files -n rust-http-body-devel -f %{oreon_filedir}/rust-http-body-devel.list

%changelog

%autochangelog
