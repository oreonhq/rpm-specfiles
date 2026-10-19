%global source0_hash 252429dbb8aeacc3233df500dc3a6a367bf28eb3a711272884d7540a7b636055
%bcond check 0
%global debug_package %{nil}
%global crate primal-bit
Name:           rust-primal-bit
Version:        0.3.2
Release:        1%{?dist}
Summary:        Bit-vector specialised to the prime-number-related needs of primal
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/primal-bit
Source0:        https://static.crates.io/crates/primal-bit/primal-bit-%{version}.crate
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
Summary:        Bit-vector specialised to the prime-number-related needs of primal
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Bit-vector specialised to the prime-number-related needs of primal
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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
%files -n rust-primal-bit-devel -f %{oreon_filedir}/rust-primal-bit-devel.list

%changelog

%autochangelog
