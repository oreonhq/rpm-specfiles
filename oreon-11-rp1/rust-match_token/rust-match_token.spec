%global source3_hash 86dd7f026f916daf7511e39951ad8ea8cf55a8db67ae64060dacf829761c18f3
%global source2_hash a60eea817514531668d7e00765731449fe14d059d3249e0bc93b36de45f759f2
%global source0_hash ac84fd3f360fcc43dc5f5d186f02a94192761a080e8bc58621ad4d12296a58cf
%bcond check 1
%global debug_package %{nil}
%global crate match_token
Name:           rust-match_token
Version:        0.35.0
Release:        1%{?dist}
Summary:        Procedural macro for html5ever
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/match_token
Source0:        https://static.crates.io/crates/match_token/match_token-%{version}.crate
Source2:        https://github.com/servo/html5ever/raw/refs/tags/html5ever-v0.35.0/LICENSE-APACHE
Source3:        https://github.com/servo/html5ever/raw/refs/tags/html5ever-v0.35.0/LICENSE-MIT
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
Summary:        Procedural macro for html5ever
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE2} %{SOURCE3} .
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
%files -n rust-match_token-devel -f %{oreon_filedir}/rust-match_token-devel.list

%changelog

%autochangelog
