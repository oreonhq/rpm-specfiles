%global source0_hash 61807f77802ff30975e01f4f071c8ba10c022052f98b3294119f3e615d13e5be
%bcond check 1
%global debug_package %{nil}
%global crate normalize-line-endings
Name:           rust-normalize-line-endings
Version:        0.3.0
Release:        1%{?dist}
Summary:        Takes an iterator over chars and returns a new iterator with all
License:        Apache-2.0
URL:            https://crates.io/crates/normalize-line-endings
Source0:        https://static.crates.io/crates/normalize-line-endings/normalize-line-endings-%{version}.crate
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
Summary:        Takes an iterator over chars and returns a new iterator with all
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
%files -n rust-normalize-line-endings-devel -f %{oreon_filedir}/rust-normalize-line-endings-devel.list

%changelog

%autochangelog
