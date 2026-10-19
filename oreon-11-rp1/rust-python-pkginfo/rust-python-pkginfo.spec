%global source0_hash 229fe47647d6602b9b0934b21fab8aece1c5a5aeb0a934196a14355fec656623
%bcond check 1
%global debug_package %{nil}
%global crate python-pkginfo
Name:           rust-python-pkginfo
Version:        0.6.8
Release:        1%{?dist}
Summary:        Parse Python package metadata from sdist and bdists and etc
License:        MIT
URL:            https://crates.io/crates/python-pkginfo
Source0:        https://static.crates.io/crates/python-pkginfo/python-pkginfo-%{version}.crate
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
Summary:        Parse Python package metadata from sdist and bdists and etc
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bzip2-devel
Summary:        Parse Python package metadata from sdist and bdists and etc
BuildArch:      noarch
%description -n %{name}+bzip2-devel

This package contains library source intended for building other packages which
use the "bzip2" feature of the "%{crate}" crate.

%package     -n %{name}+deprecated-formats-devel
Summary:        Parse Python package metadata from sdist and bdists and etc
BuildArch:      noarch
%description -n %{name}+deprecated-formats-devel

This package contains library source intended for building other packages which
use the "deprecated-formats" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Parse Python package metadata from sdist and bdists and etc
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+xz-devel
Summary:        Parse Python package metadata from sdist and bdists and etc
BuildArch:      noarch
%description -n %{name}+xz-devel

This package contains library source intended for building other packages which
use the "xz" feature of the "%{crate}" crate.

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
%files -n rust-python-pkginfo-devel -f %{oreon_filedir}/rust-python-pkginfo-devel.list

%changelog

%autochangelog
