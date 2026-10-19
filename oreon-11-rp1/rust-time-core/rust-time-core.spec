%global source0_hash 9e1c906769ad99c88eaa54e728060edef082f8e358ff32030cb7c7d315e81109
%bcond check 0
%global debug_package %{nil}
%global crate time-core
Name:           rust-time-core
Version:        0.1.9
Release:        1%{?dist}
Summary:        This crate is an implementation detail and should not be relied upon...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/time-core
Source0:        https://static.crates.io/crates/time-core/time-core-%{version}.crate
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
Summary:        This crate is an implementation detail and should not be relied upon...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+large-dates-devel
Summary:        This crate is an implementation detail and should not be relied upon...
BuildArch:      noarch
%description -n %{name}+large-dates-devel

This package contains library source intended for building other packages which
use the "large-dates" feature of the "%{crate}" crate.

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
%files -n rust-time-core-devel -f %{oreon_filedir}/rust-time-core-devel.list

%changelog

%autochangelog
