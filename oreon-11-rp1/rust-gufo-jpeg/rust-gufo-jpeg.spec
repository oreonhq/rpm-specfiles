%global source0_hash 383907a5c532bff484b2914d649e368e98ce6426829458353fe40070225b07a5
%bcond check 1
%global debug_package %{nil}
%global crate gufo-jpeg
Name:           rust-gufo-jpeg
Version:        0.5.1
Release:        1%{?dist}
Summary:        Inspect JPEG image structure
License:        MPL-2.0 OR LGPL-2.1-or-later
URL:            https://crates.io/crates/gufo-jpeg
Source0:        https://static.crates.io/crates/gufo-jpeg/gufo-jpeg-%{version}.crate
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
Summary:        Inspect JPEG image structure
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+encoder-devel
Summary:        Inspect JPEG image structure
BuildArch:      noarch
%description -n %{name}+encoder-devel

This package contains library source intended for building other packages which
use the "encoder" feature of the "%{crate}" crate.

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
%files -n rust-gufo-jpeg-devel -f %{oreon_filedir}/rust-gufo-jpeg-devel.list

%changelog

%autochangelog
