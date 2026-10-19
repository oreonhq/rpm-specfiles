%global source0_hash d9c4f5dac5e15c24eb999c26181a6ca40b39fe946cbe4c263c7209467bc83af2
%bcond check 0
%global debug_package %{nil}
%global crate foldhash
Name:           rust-foldhash0.1
Version:        0.1.5
Release:        1%{?dist}
Summary:        A fast, non-cryptographic, minimally DoS-resistant hashing algorithm.
License:        Zlib
URL:            https://crates.io/crates/foldhash
Source0:        https://static.crates.io/crates/foldhash/foldhash-%{version}.crate
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
Summary:        A fast, non-cryptographic, minimally DoS-resistant hashing algorithm.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A fast, non-cryptographic, minimally DoS-resistant hashing algorithm.
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
%files -n rust-foldhash0.1-devel -f %{oreon_filedir}/rust-foldhash0.1-devel.list

%changelog

%autochangelog
