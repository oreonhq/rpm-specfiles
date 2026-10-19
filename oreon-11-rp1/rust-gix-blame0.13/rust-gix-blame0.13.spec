%global source0_hash 14dab9a942ab54a9661ded7397c3bf927274e7afa94494db0d75cfcbde02ca0a
%bcond check 0
%global debug_package %{nil}
%global crate gix-blame
Name:           rust-gix-blame0.13
Version:        0.13.0
Release:        1%{?dist}
Summary:        A crate of the gitoxide project dedicated to implementing a 'blame' a...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-blame
Source0:        https://static.crates.io/crates/gix-blame/gix-blame-%{version}.crate
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

%package     -n %{name}+sha1-devel
Summary:        A crate of the gitoxide project dedicated to implementing a 'blame' a...
BuildArch:      noarch
%description -n %{name}+sha1-devel

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

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
%files -n rust-gix-blame0.13-devel -f %{oreon_filedir}/rust-gix-blame0.13-devel.list

%changelog

%autochangelog
