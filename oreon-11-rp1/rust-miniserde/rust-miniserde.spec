%global source0_hash e8f82621301d3b99a1542736de96e5df69865b235987d6470b28c7aa670cfeb1
%bcond check 0
%global debug_package %{nil}
%global crate miniserde
Name:           rust-miniserde
Version:        0.1.46
Release:        1%{?dist}
Summary:        Data structure serialization library with several opposite design goa...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/miniserde
Source0:        https://static.crates.io/crates/miniserde/miniserde-%{version}.crate
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
Summary:        Data structure serialization library with several opposite design goa...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Data structure serialization library with several opposite design goa...
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
%files -n rust-miniserde-devel -f %{oreon_filedir}/rust-miniserde-devel.list

%changelog

%autochangelog
