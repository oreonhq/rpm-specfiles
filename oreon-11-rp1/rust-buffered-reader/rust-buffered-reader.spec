%global source0_hash c7531a07caf83a3fa3b47a233b437ee7910cccfb688555d224338295a0a64fcc
%bcond check 0
%global debug_package %{nil}
%global crate buffered-reader
Name:           rust-buffered-reader
Version:        1.4.1
Release:        1%{?dist}
Summary:        A super-powered Reader
License:        LGPL-2.0-or-later
URL:            https://crates.io/crates/buffered-reader
Source0:        https://static.crates.io/crates/buffered-reader/buffered-reader-%{version}.crate
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
Summary:        A super-powered Reader
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bzip2-devel
Summary:        A super-powered Reader
BuildArch:      noarch
%description -n %{name}+bzip2-devel

This package contains library source intended for building other packages which
use the "bzip2" feature of the "%{crate}" crate.

%package     -n %{name}+compression-devel
Summary:        A super-powered Reader
BuildArch:      noarch
%description -n %{name}+compression-devel

This package contains library source intended for building other packages which
use the "compression" feature of the "%{crate}" crate.

%package     -n %{name}+compression-bzip2-devel
Summary:        A super-powered Reader
BuildArch:      noarch
%description -n %{name}+compression-bzip2-devel

This package contains library source intended for building other packages which
use the "compression-bzip2" feature of the "%{crate}" crate.

%package     -n %{name}+compression-deflate-devel
Summary:        A super-powered Reader
BuildArch:      noarch
%description -n %{name}+compression-deflate-devel

This package contains library source intended for building other packages which
use the "compression-deflate" feature of the "%{crate}" crate.

%package     -n %{name}+flate2-devel
Summary:        A super-powered Reader
BuildArch:      noarch
%description -n %{name}+flate2-devel

This package contains library source intended for building other packages which
use the "flate2" feature of the "%{crate}" crate.

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
%files -n rust-buffered-reader-devel -f %{oreon_filedir}/rust-buffered-reader-devel.list

%changelog

%autochangelog
