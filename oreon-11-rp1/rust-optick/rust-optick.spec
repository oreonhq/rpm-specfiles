%global source0_hash d7e7ab6068cdba9928db83674b18fe7aa2efbaa9920698d260ecbaf7906c6548
%bcond check 0
%global debug_package %{nil}
%global crate optick
Name:           rust-optick
Version:        1.3.4
Release:        1%{?dist}
Summary:        Super Lightweight Performance Profiler
License:        MIT
URL:            https://crates.io/crates/optick
Source0:        https://static.crates.io/crates/optick/optick-%{version}.crate
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
Summary:        Super Lightweight Performance Profiler
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+enable-devel
Summary:        Super Lightweight Performance Profiler
BuildArch:      noarch
%description -n %{name}+enable-devel

This package contains library source intended for building other packages which
use the "enable" feature of the "%{crate}" crate.

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
%files -n rust-optick-devel -f %{oreon_filedir}/rust-optick-devel.list

%changelog

%autochangelog
