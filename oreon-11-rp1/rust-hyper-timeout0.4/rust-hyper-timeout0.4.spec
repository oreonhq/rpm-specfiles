%global source0_hash bbb958482e8c7be4bc3cf272a766a2b0bf1a6755e7a6ae777f017a31d11b13b1
%bcond check 0
%global debug_package %{nil}
%global crate hyper-timeout
Name:           rust-hyper-timeout0.4
Version:        0.4.1
Release:        1%{?dist}
Summary:        A connect, read and write timeout aware connector to be used with hyp...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hyper-timeout
Source0:        https://static.crates.io/crates/hyper-timeout/hyper-timeout-%{version}.crate
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
Summary:        A connect, read and write timeout aware connector to be used with hyp...
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
%files -n rust-hyper-timeout0.4-devel -f %{oreon_filedir}/rust-hyper-timeout0.4-devel.list

%changelog

%autochangelog
