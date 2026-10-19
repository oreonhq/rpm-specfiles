%global source0_hash 34037907a12187df805f8581f4542ba3dd838794dca025adbbabbfc4d161eac7
%bcond check 1
%global debug_package %{nil}
%global crate in-toto
Name:           rust-in-toto
Version:        0.4.0
Release:        1%{?dist}
Summary:        Library for in-toto
License:        MIT
URL:            https://crates.io/crates/in-toto
Source0:        https://static.crates.io/crates/in-toto/in-toto-%{version}.crate
Patch:          in-toto-fix-metadata.diff
%if %{with check}
%endif
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  openssl
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
Summary:        Library for in-toto
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
%files -n rust-in-toto-devel -f %{oreon_filedir}/rust-in-toto-devel.list

%changelog

%autochangelog
