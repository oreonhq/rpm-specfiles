%global source0_hash 058ed274caafc1f60c4997b5fc07bf7dc7cca454af7c6e81edffe5f33f70dace
%bcond check 0
%global debug_package %{nil}
%global crate crossbeam-epoch
Name:           rust-crossbeam-epoch0.8
Version:        0.8.2
Release:        1%{?dist}
Summary:        Epoch-based garbage collection
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/crossbeam-epoch
Source0:        https://static.crates.io/crates/crossbeam-epoch/crossbeam-epoch-%{version}.crate
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
Summary:        Epoch-based garbage collection
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Epoch-based garbage collection
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+lazy_static-devel
Summary:        Epoch-based garbage collection
BuildArch:      noarch
%description -n %{name}+lazy_static-devel

This package contains library source intended for building other packages which
use the "lazy_static" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Epoch-based garbage collection
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+sanitize-devel
Summary:        Epoch-based garbage collection
BuildArch:      noarch
%description -n %{name}+sanitize-devel

This package contains library source intended for building other packages which
use the "sanitize" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Epoch-based garbage collection
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
%files -n rust-crossbeam-epoch0.8-devel -f %{oreon_filedir}/rust-crossbeam-epoch0.8-devel.list

%changelog

%autochangelog
