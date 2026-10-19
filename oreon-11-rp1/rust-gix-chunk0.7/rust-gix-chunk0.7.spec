%global source0_hash b2a871e5cab12ba568845714473505deefffb3c04eb47f4708ce344cd459c1cc
%bcond check 0
%global debug_package %{nil}
%global crate gix-chunk
Name:           rust-gix-chunk0.7
Version:        0.7.3
Release:        1%{?dist}
Summary:        Interact with the git chunk file format used in multi-pack index and...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-chunk
Source0:        https://static.crates.io/crates/gix-chunk/gix-chunk-%{version}.crate
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
Summary:        Interact with the git chunk file format used in multi-pack index and...
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
%files -n rust-gix-chunk0.7-devel -f %{oreon_filedir}/rust-gix-chunk0.7-devel.list

%changelog

%autochangelog
