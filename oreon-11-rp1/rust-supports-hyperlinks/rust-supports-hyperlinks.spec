%global source0_hash e396b6523b11ccb83120b115a0b7366de372751aa6edf19844dfb13a6af97e91
%bcond check 0
%global debug_package %{nil}
%global crate supports-hyperlinks
Name:           rust-supports-hyperlinks
Version:        3.2.0
Release:        1%{?dist}
Summary:        Detects whether a terminal supports rendering hyperlinks.
License:        Apache-2.0
URL:            https://crates.io/crates/supports-hyperlinks
Source0:        https://static.crates.io/crates/supports-hyperlinks/supports-hyperlinks-%{version}.crate
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
Summary:        Detects whether a terminal supports rendering hyperlinks.
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
%files -n rust-supports-hyperlinks-devel -f %{oreon_filedir}/rust-supports-hyperlinks-devel.list

%changelog

%autochangelog
