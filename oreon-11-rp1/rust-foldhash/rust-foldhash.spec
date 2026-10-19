%global source0_hash 77ce24cb58228fbb8aa041425bb1050850ac19177686ea6e0f41a70416f56fdb
%bcond check 0
%global debug_package %{nil}
%global crate foldhash
Name:           rust-foldhash
Version:        0.2.0
Release:        1%{?dist}
Summary:        Fast, non-cryptographic, minimally DoS-resistant hashing algorithm
License:        Zlib
URL:            https://crates.io/crates/foldhash
Source0:        https://static.crates.io/crates/foldhash/foldhash-%{version}.crate
Patch:          foldhash-fix-metadata.diff
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
Summary:        Fast, non-cryptographic, minimally DoS-resistant hashing algorithm
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Fast, non-cryptographic, minimally DoS-resistant hashing algorithm
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
%files -n rust-foldhash-devel -f %{oreon_filedir}/rust-foldhash-devel.list

%changelog

%autochangelog
