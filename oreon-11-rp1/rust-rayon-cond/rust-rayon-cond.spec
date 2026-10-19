%global source0_hash 2964d0cf57a3e7a06e8183d14a8b527195c706b7983549cd5462d5aa3747438f
%bcond check 1
%global debug_package %{nil}
%global crate rayon-cond
Name:           rust-rayon-cond
Version:        0.4.0
Release:        1%{?dist}
Summary:        Experimental iterator wrapper that is conditionally parallel or serial
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/rayon-cond
Source0:        https://static.crates.io/crates/rayon-cond/rayon-cond-%{version}.crate
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
Summary:        Experimental iterator wrapper that is conditionally parallel or serial
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
%files -n rust-rayon-cond-devel -f %{oreon_filedir}/rust-rayon-cond-devel.list

%changelog

%autochangelog
