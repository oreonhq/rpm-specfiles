%global source0_hash 7c8a2469e56e6e5095c82ccd3afb98dad95f7af7929aab6d8ba8d6e0f73657da
%bcond check 0
%global debug_package %{nil}
%global crate uluru
Name:           rust-uluru
Version:        3.1.0
Release:        1%{?dist}
Summary:        A simple, fast, LRU cache implementation
License:        MPL-2.0
URL:            https://crates.io/crates/uluru
Source0:        https://static.crates.io/crates/uluru/uluru-%{version}.crate
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
Summary:        A simple, fast, LRU cache implementation
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
%files -n rust-uluru-devel -f %{oreon_filedir}/rust-uluru-devel.list

%changelog

%autochangelog
