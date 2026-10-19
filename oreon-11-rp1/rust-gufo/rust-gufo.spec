%global source0_hash 6a16d7faeeb03e2925ac6b0f40630b15b1992d08c50add402f35fde495e44f64
%bcond check 0
%global debug_package %{nil}
%global crate gufo
Name:           rust-gufo
Version:        0.5.0
Release:        1%{?dist}
Summary:        Gufo
License:        MPL-2.0 OR LGPL-2.1-or-later
URL:            https://crates.io/crates/gufo
Source0:        https://static.crates.io/crates/gufo/gufo-%{version}.crate
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
Summary:        Gufo
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+all-image-formats-devel
Summary:        Gufo
BuildArch:      noarch
%description -n %{name}+all-image-formats-devel

This package contains library source intended for building other packages which
use the "all-image-formats" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Gufo
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+jpeg-devel
Summary:        Gufo
BuildArch:      noarch
%description -n %{name}+jpeg-devel

This package contains library source intended for building other packages which
use the "jpeg" feature of the "%{crate}" crate.

%package     -n %{name}+png-devel
Summary:        Gufo
BuildArch:      noarch
%description -n %{name}+png-devel

This package contains library source intended for building other packages which
use the "png" feature of the "%{crate}" crate.

%package     -n %{name}+tiff-devel
Summary:        Gufo
BuildArch:      noarch
%description -n %{name}+tiff-devel

This package contains library source intended for building other packages which
use the "tiff" feature of the "%{crate}" crate.

%package     -n %{name}+webp-devel
Summary:        Gufo
BuildArch:      noarch
%description -n %{name}+webp-devel

This package contains library source intended for building other packages which
use the "webp" feature of the "%{crate}" crate.

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
%files -n rust-gufo-devel -f %{oreon_filedir}/rust-gufo-devel.list

%changelog

%autochangelog
