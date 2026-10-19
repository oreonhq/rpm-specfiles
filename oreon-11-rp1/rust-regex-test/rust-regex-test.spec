%global source0_hash da40f0939bc4c598b4326abdbb363a8987aa43d0526e5624aefcf3ed90344e62
%bcond_without check
%global debug_package %{nil}
%global crate regex-test
Name:           rust-regex-test
Version:        0.1.1
Release:        1%{?dist}
Summary:        Infrastructure for testing regexes
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/regex-test
Source0:        https://static.crates.io/crates/regex-test/regex-test-%{version}.crate
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
Summary:        Infrastructure for testing regexes
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
%files -n rust-regex-test-devel -f %{oreon_filedir}/rust-regex-test-devel.list

%changelog

%autochangelog
