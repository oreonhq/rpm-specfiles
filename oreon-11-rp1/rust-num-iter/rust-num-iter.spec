%global source0_hash c92800bd69a1eac91786bcfe9da64a897eb72911b8dc3095decbd07429e8048b
%bcond check 0
%global debug_package %{nil}
%global crate num-iter
Name:           rust-num-iter
Version:        0.1.46
Release:        1%{?dist}
Summary:        External iterators for generic mathematics
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/num-iter
Source0:        https://static.crates.io/crates/num-iter/num-iter-%{version}.crate
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
Summary:        External iterators for generic mathematics
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+i128-devel
Summary:        External iterators for generic mathematics
BuildArch:      noarch
%description -n %{name}+i128-devel

This package contains library source intended for building other packages which
use the "i128" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        External iterators for generic mathematics
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
%files -n rust-num-iter-devel -f %{oreon_filedir}/rust-num-iter-devel.list

%changelog

%autochangelog
