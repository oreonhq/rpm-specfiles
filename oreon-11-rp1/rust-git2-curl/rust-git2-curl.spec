%global source0_hash 1f1f6fe01327a2f7a1d6ee519c14651f79530aa4d64e870f4cf672efe697bea5
%bcond check 0
%global debug_package %{nil}
%global crate git2-curl
Name:           rust-git2-curl
Version:        0.22.0
Release:        1%{?dist}
Summary:        Backend for an HTTP transport in libgit2 powered by libcurl.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/git2-curl
Source0:        https://static.crates.io/crates/git2-curl/git2-curl-%{version}.crate
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

%package     -n %{name}+zlib-ng-compat-devel
Summary:        Backend for an HTTP transport in libgit2 powered by libcurl.
BuildArch:      noarch
%description -n %{name}+zlib-ng-compat-devel

This package contains library source intended for building other packages which
use the "zlib-ng-compat" feature of the "%{crate}" crate.

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
%files -n rust-git2-curl-devel -f %{oreon_filedir}/rust-git2-curl-devel.list

%changelog

%autochangelog
