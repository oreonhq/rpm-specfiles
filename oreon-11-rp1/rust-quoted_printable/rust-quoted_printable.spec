%global source0_hash 478e0585659a122aa407eb7e3c0e1fa51b1d8a870038bd29f0cf4a8551eea972
%bcond check 0
%global debug_package %{nil}
%global crate quoted_printable
Name:           rust-quoted_printable
Version:        0.5.2
Release:        1%{?dist}
Summary:        A simple encoder/decoder for quoted-printable data
License:        0BSD
URL:            https://crates.io/crates/quoted_printable
Source0:        https://static.crates.io/crates/quoted_printable/quoted_printable-%{version}.crate
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
Summary:        A simple encoder/decoder for quoted-printable data
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A simple encoder/decoder for quoted-printable data
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-quoted_printable-devel -f %{oreon_filedir}/rust-quoted_printable-devel.list

%changelog

%autochangelog
