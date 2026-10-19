%global source0_hash 0ce1bb7fb0c258a6600d699950da347a7a9dad66c3ce815769b5f11cf8fce78e
%bcond check 0
%global debug_package %{nil}
%global crate chainerror
Name:           rust-chainerror
Version:        0.7.1
Release:        1%{?dist}
Summary:        Make chaining errors easy
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/chainerror
Source0:        https://static.crates.io/crates/chainerror/chainerror-%{version}.crate
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
Summary:        Make chaining errors easy
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+display-cause-devel
Summary:        Make chaining errors easy
BuildArch:      noarch
%description -n %{name}+display-cause-devel

This package contains library source intended for building other packages which
use the "display-cause" feature of the "%{crate}" crate.

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
%files -n rust-chainerror-devel -f %{oreon_filedir}/rust-chainerror-devel.list

%changelog

%autochangelog
