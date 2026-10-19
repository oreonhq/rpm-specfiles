%global source0_hash 0f056c8559e3757392c8d091e796416e4649d8e49e88b8d76df6c002f05027fd
%bcond check 1
%global debug_package %{nil}
%global crate http-serde
Name:           rust-http-serde
Version:        2.1.1
Release:        1%{?dist}
Summary:        Serde support for the http crate
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/http-serde
Source0:        https://static.crates.io/crates/http-serde/http-serde-%{version}.crate
Patch2:         https://gitlab.com/kornelski/http-serde/-/merge_requests/6.patch#/http-serde-2.1.1-license-files.patch
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
Summary:        Serde support for the http crate
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
%files -n rust-http-serde-devel -f %{oreon_filedir}/rust-http-serde-devel.list

%changelog

%autochangelog
