%global source0_hash 49045042e5fced01b80742aba5508de82aa4f13677ed3fa2b4cda709c40c5918
%bcond check 1
%global debug_package %{nil}
%global crate cxxbridge-flags
Name:           rust-cxxbridge-flags
Version:        1.0.202
Release:        2%{?dist}
Summary:        Compiler configuration of the cxx crate (implementation detail)
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cxxbridge-flags
Source0:        https://static.crates.io/crates/cxxbridge-flags/cxxbridge-flags-%{version}.crate
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
Summary:        Compiler configuration of the cxx crate (implementation detail)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+c++14-devel
Summary:        Compiler configuration of the cxx crate (implementation detail)
BuildArch:      noarch
%description -n %{name}+c++14-devel

This package contains library source intended for building other packages which
use the "c++14" feature of the "%{crate}" crate.

%package     -n %{name}+c++17-devel
Summary:        Compiler configuration of the cxx crate (implementation detail)
BuildArch:      noarch
%description -n %{name}+c++17-devel

This package contains library source intended for building other packages which
use the "c++17" feature of the "%{crate}" crate.

%package     -n %{name}+c++20-devel
Summary:        Compiler configuration of the cxx crate (implementation detail)
BuildArch:      noarch
%description -n %{name}+c++20-devel

This package contains library source intended for building other packages which
use the "c++20" feature of the "%{crate}" crate.

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
%files -n rust-cxxbridge-flags-devel -f %{oreon_filedir}/rust-cxxbridge-flags-devel.list

%changelog

%autochangelog
