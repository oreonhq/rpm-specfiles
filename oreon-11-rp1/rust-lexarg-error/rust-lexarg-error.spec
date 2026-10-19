%global source0_hash 178daf11ee95fa4bf31ff1af878dda4c637dc08a37aabdd63ae3683481fd13a9
%bcond check 1
%global debug_package %{nil}
%global crate lexarg-error
Name:           rust-lexarg-error
Version:        0.0.2
Release:        1%{?dist}
Summary:        Argument error type for use with lexarg
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/lexarg-error
Source0:        https://static.crates.io/crates/lexarg-error/lexarg-error-%{version}.crate
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
Summary:        Argument error type for use with lexarg
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
%files -n rust-lexarg-error-devel -f %{oreon_filedir}/rust-lexarg-error-devel.list

%changelog

%autochangelog
