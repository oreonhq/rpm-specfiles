%global source0_hash e40758ed24c9b2eeb76c35fb0aebc66c626084edd827e07e1552279814c6682d
%bcond check 0
%global debug_package %{nil}
%global crate filedescriptor
Name:           rust-filedescriptor
Version:        0.8.3
Release:        1%{?dist}
Summary:        More ergonomic wrappers around RawFd and RawHandle
License:        MIT
URL:            https://crates.io/crates/filedescriptor
Source0:        https://static.crates.io/crates/filedescriptor/filedescriptor-%{version}.crate
Patch:          filedescriptor-fix-metadata-auto.diff
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
Summary:        More ergonomic wrappers around RawFd and RawHandle
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
%files -n rust-filedescriptor-devel -f %{oreon_filedir}/rust-filedescriptor-devel.list

%changelog

%autochangelog
