%global source0_hash 323c417e1d9665a65b263ec744ba09030cfb277e9daa0b018a4ab62e57bc8189
%bcond check 0
%global debug_package %{nil}
%global crate roff
Name:           rust-roff1
Version:        1.1.1
Release:        2%{?dist}
Summary:        ROFF (man page format) generation library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/roff
Source0:        https://static.crates.io/crates/roff/roff-%{version}.crate
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
Summary:        ROFF (man page format) generation library
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
%files -n rust-roff1-devel -f %{oreon_filedir}/rust-roff1-devel.list

%changelog

%autochangelog
