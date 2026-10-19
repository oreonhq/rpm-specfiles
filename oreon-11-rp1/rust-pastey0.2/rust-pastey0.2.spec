%global source0_hash 2ee67f1008b1ba2321834326597b8e186293b049a023cdef258527550b9935b4
%bcond check 0
%global debug_package %{nil}
%global crate pastey
Name:           rust-pastey0.2
Version:        0.2.3
Release:        1%{?dist}
Summary:        Macros for all your token pasting needs. Successor of paste
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pastey
Source0:        https://static.crates.io/crates/pastey/pastey-%{version}.crate
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
Summary:        Macros for all your token pasting needs. Successor of paste
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
%files -n rust-pastey0.2-devel -f %{oreon_filedir}/rust-pastey0.2-devel.list

%changelog

%autochangelog
