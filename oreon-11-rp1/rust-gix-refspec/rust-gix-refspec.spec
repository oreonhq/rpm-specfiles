%global source0_hash 7de280d46e8fd9e4d3e7e2ab4276b965e377ba68b2b9a8fce56371015e8bb059
%bcond check 0
%global debug_package %{nil}
%global crate gix-refspec
Name:           rust-gix-refspec
Version:        0.45.1
Release:        1%{?dist}
Summary:        A crate of the gitoxide project for parsing and representing refspecs
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-refspec
Source0:        https://static.crates.io/crates/gix-refspec/gix-refspec-%{version}.crate
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
Summary:        A crate of the gitoxide project for parsing and representing refspecs
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
%files -n rust-gix-refspec-devel -f %{oreon_filedir}/rust-gix-refspec-devel.list

%changelog

%autochangelog
