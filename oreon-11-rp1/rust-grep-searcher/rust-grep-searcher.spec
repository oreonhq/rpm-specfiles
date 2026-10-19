%global source0_hash 72348823a0eafc4bc2e9051064f28b5b42cc100b571b3a35d67918d711efcbc6
%bcond check 1
%global debug_package %{nil}
%global crate grep-searcher
Name:           rust-grep-searcher
Version:        0.1.17
Release:        1%{?dist}
Summary:        Fast line oriented regex searching as a library
License:        Unlicense OR MIT
URL:            https://crates.io/crates/grep-searcher
Source0:        https://static.crates.io/crates/grep-searcher/grep-searcher-%{version}.crate
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
Summary:        Fast line oriented regex searching as a library
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
%files -n rust-grep-searcher-devel -f %{oreon_filedir}/rust-grep-searcher-devel.list

%changelog

%autochangelog
