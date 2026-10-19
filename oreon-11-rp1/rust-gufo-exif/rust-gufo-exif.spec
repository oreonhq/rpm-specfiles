%global source0_hash e99100988e312c22c6f209663b289e727db3918d06fbcbbc2315149457b42b75
%bcond check 0
%global debug_package %{nil}
%global crate gufo-exif
Name:           rust-gufo-exif
Version:        0.5.0
Release:        1%{?dist}
Summary:        Exif loading and editing
License:        MPL-2.0 OR LGPL-2.1-or-later
URL:            https://crates.io/crates/gufo-exif
Source0:        https://static.crates.io/crates/gufo-exif/gufo-exif-%{version}.crate
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
Summary:        Exif loading and editing
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Exif loading and editing
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

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
%files -n rust-gufo-exif-devel -f %{oreon_filedir}/rust-gufo-exif-devel.list

%changelog

%autochangelog
