%global source10_hash 789e1850d5464e4b6f2e360eb4a95be932a358de624f63bc2f84a9fbf4faee3f
%global source0_hash 7ab9a05148c7b3e85c17806fef4b2889c44f1a60575c5da9e9be80ce13227185
%bcond check 1
%global debug_package %{nil}
%global crate astral_async_http_range_reader
Name:           rust-astral_async_http_range_reader
Version:        0.10.0
Release:        1%{?dist}
Summary:        Library for streaming reading of files over HTTP using range requests
License:        MIT
URL:            https://crates.io/crates/astral_async_http_range_reader
Source0:        https://static.crates.io/crates/astral_async_http_range_reader/astral_async_http_range_reader-%{version}.crate
Source10:       https://github.com/astral-sh/async_http_range_reader/raw/deca957f19041364b13c6a8dd477fe204f11fe8d/test-data/andes-1.8.3-pyhd8ed1ab_0.conda
Patch:          astral_async_http_range_reader-fix-metadata.diff
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
Summary:        Library for streaming reading of files over HTTP using range requests
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

install -t test-data -D -m 0644 -p '%{SOURCE10}'
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-astral_async_http_range_reader-devel -f %{oreon_filedir}/rust-astral_async_http_range_reader-devel.list

%changelog

%autochangelog
