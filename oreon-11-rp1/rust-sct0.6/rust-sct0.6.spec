%global source0_hash b362b83898e0e69f38515b82ee15aa80636befe47c3b6d3d89a911e78fc228ce
%bcond check 0
%global debug_package %{nil}
%global crate sct
Name:           rust-sct0.6
Version:        0.6.1
Release:        1%{?dist}
Summary:        Certificate transparency SCT verification library
License:        Apache-2.0 OR ISC OR MIT
URL:            https://crates.io/crates/sct
Source0:        https://static.crates.io/crates/sct/sct-%{version}.crate
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
Summary:        Certificate transparency SCT verification library
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
%files -n rust-sct0.6-devel -f %{oreon_filedir}/rust-sct0.6-devel.list

%changelog

%autochangelog
