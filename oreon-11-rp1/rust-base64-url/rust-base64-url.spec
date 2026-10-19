%global source0_hash d3b761ea69df72d0cc9591ea39adfb0e3b922a27dc535227d7ffbed5702e8809
%bcond check 1
%global debug_package %{nil}
%global crate base64-url
Name:           rust-base64-url
Version:        3.0.3
Release:        1%{?dist}
Summary:        Base64 encode, decode, escape and unescape for URL applications
License:        MIT
URL:            https://crates.io/crates/base64-url
Source0:        https://static.crates.io/crates/base64-url/base64-url-%{version}.crate
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
Summary:        Base64 encode, decode, escape and unescape for URL applications
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Base64 encode, decode, escape and unescape for URL applications
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-base64-url-devel -f %{oreon_filedir}/rust-base64-url-devel.list

%changelog

%autochangelog
