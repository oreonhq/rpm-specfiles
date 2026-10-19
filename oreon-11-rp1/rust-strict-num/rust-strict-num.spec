%global source0_hash 6637bab7722d379c8b41ba849228d680cc12d0a45ba1fa2b48f2a30577a06731
%bcond check 0
%global debug_package %{nil}
%global crate strict-num
Name:           rust-strict-num
Version:        0.1.1
Release:        1%{?dist}
Summary:        Collection of bounded numeric types
License:        MIT
URL:            https://crates.io/crates/strict-num
Source0:        https://static.crates.io/crates/strict-num/strict-num-%{version}.crate
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
Summary:        Collection of bounded numeric types
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+approx-eq-devel
Summary:        Collection of bounded numeric types
BuildArch:      noarch
%description -n %{name}+approx-eq-devel

This package contains library source intended for building other packages which
use the "approx-eq" feature of the "%{crate}" crate.

%package     -n %{name}+float-cmp-devel
Summary:        Collection of bounded numeric types
BuildArch:      noarch
%description -n %{name}+float-cmp-devel

This package contains library source intended for building other packages which
use the "float-cmp" feature of the "%{crate}" crate.

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
%files -n rust-strict-num-devel -f %{oreon_filedir}/rust-strict-num-devel.list

%changelog

%autochangelog
