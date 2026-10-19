%global source0_hash c96395f0a926bc13b1c17622aaddda1ecb55d49c8f1bf9777e4d877800a43f8b
%bcond check 0
%global debug_package %{nil}
%global crate pin-project-internal
Name:           rust-pin-project-internal
Version:        1.1.13
Release:        1%{?dist}
Summary:        Implementation detail of the pin-project crate
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/pin-project-internal
Source0:        https://static.crates.io/crates/pin-project-internal/pin-project-internal-%{version}.crate
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
Summary:        Implementation detail of the pin-project crate
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
%files -n rust-pin-project-internal-devel -f %{oreon_filedir}/rust-pin-project-internal-devel.list

%changelog

%autochangelog
