%global source0_hash cd1511a7b6a56299bd043a9c167a6d2bfb37bf84a6dfceaba651168adfb43c87
%bcond check 0
%global debug_package %{nil}
%global crate dtoa-short
Name:           rust-dtoa-short
Version:        0.3.5
Release:        1%{?dist}
Summary:        Serialize float number and truncate to certain precision
License:        MPL-2.0
URL:            https://crates.io/crates/dtoa-short
Source0:        https://static.crates.io/crates/dtoa-short/dtoa-short-%{version}.crate
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
Summary:        Serialize float number and truncate to certain precision
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
%files -n rust-dtoa-short-devel -f %{oreon_filedir}/rust-dtoa-short-devel.list

%changelog

%autochangelog
