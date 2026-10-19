%global source0_hash d9ca7d0f520afcd6d817970d0b2d5fd7c630c75e7783cae046b8b8a783c5befa
%bcond check 1
%global debug_package %{nil}
%global crate anstyle-lossy
Name:           rust-anstyle-lossy
Version:        1.1.5
Release:        1%{?dist}
Summary:        Lossy conversion between ANSI Color Codes
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/anstyle-lossy
Source0:        https://static.crates.io/crates/anstyle-lossy/anstyle-lossy-%{version}.crate
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
Summary:        Lossy conversion between ANSI Color Codes
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
%files -n rust-anstyle-lossy-devel -f %{oreon_filedir}/rust-anstyle-lossy-devel.list

%changelog

%autochangelog
