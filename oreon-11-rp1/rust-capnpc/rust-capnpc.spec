%global source0_hash 82ca16312ddb64529d31c8dc46148671c22e57b80134fa5f17811ad5a6a79492
%bcond check 0
%global debug_package %{nil}
%global crate capnpc
Name:           rust-capnpc
Version:        0.27.0
Release:        1%{?dist}
Summary:        Cap'n Proto code generation
License:        MIT
URL:            https://crates.io/crates/capnpc
Source0:        https://static.crates.io/crates/capnpc/capnpc-%{version}.crate
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
Summary:        Cap'n Proto code generation
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
%files -n rust-capnpc-devel -f %{oreon_filedir}/rust-capnpc-devel.list

%changelog

%autochangelog
