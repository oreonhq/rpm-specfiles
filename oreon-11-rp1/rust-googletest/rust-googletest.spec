%global source0_hash f6b5e2f2b556b7b90297a5a35c8267dd43a537923d2b329beefdba2b4ec19d94
%bcond check 0
%global debug_package %{nil}
%global crate googletest
Name:           rust-googletest
Version:        0.14.3
Release:        1%{?dist}
Summary:        Rich assertion and matcher library inspired by GoogleTest for C++
License:        Apache-2.0
URL:            https://crates.io/crates/googletest
Source0:        https://static.crates.io/crates/googletest/googletest-%{version}.crate
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
Summary:        Rich assertion and matcher library inspired by GoogleTest for C++
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+anyhow-devel
Summary:        Rich assertion and matcher library inspired by GoogleTest for C++
BuildArch:      noarch
%description -n %{name}+anyhow-devel

This package contains library source intended for building other packages which
use the "anyhow" feature of the "%{crate}" crate.

%package     -n %{name}+proptest-devel
Summary:        Rich assertion and matcher library inspired by GoogleTest for C++
BuildArch:      noarch
%description -n %{name}+proptest-devel

This package contains library source intended for building other packages which
use the "proptest" feature of the "%{crate}" crate.

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
%files -n rust-googletest-devel -f %{oreon_filedir}/rust-googletest-devel.list

%changelog

%autochangelog
