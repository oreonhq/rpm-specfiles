%global source0_hash b3314d5adb5d94bcdf56771f2e50dbbc80bb4bdf88967526706205ac9eff24eb
%bcond check 0
%global debug_package %{nil}
%global crate headers
Name:           rust-headers
Version:        0.4.1
Release:        1%{?dist}
Summary:        typed HTTP headers
License:        MIT
URL:            https://crates.io/crates/headers
Source0:        https://static.crates.io/crates/headers/headers-%{version}.crate
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

%package     -n %{name}+nightly-devel
Summary:        typed HTTP headers
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

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
%files -n rust-headers-devel -f %{oreon_filedir}/rust-headers-devel.list

%changelog

%autochangelog
