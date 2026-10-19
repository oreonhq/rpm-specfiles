%global source0_hash f1f927b07c74ba84c7e5fe4db2baeb3e996ab2688992e39ac68ce3220a677c7e
%bcond check 0
%global debug_package %{nil}
%global crate charset
Name:           rust-charset
Version:        0.1.5
Release:        1%{?dist}
Summary:        Character encoding decoding for email
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/charset
Source0:        https://static.crates.io/crates/charset/charset-%{version}.crate
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

%package     -n %{name}+serde-devel
Summary:        Character encoding decoding for email
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-charset-devel -f %{oreon_filedir}/rust-charset-devel.list

%changelog

%autochangelog
