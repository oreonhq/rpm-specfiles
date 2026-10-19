%global source0_hash cab834c73d247e67f4fae452806d17d3c7501756d98c8808d7c9c7aa7d18f973
%bcond check 0
%global debug_package %{nil}
%global crate regex-lite
Name:           rust-regex-lite
Version:        0.1.9
Release:        1%{?dist}
Summary:        Lightweight regex engine that optimizes for binary size and compilation time
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/regex-lite
Source0:        https://static.crates.io/crates/regex-lite/regex-lite-%{version}.crate
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
Summary:        Lightweight regex engine that optimizes for binary size and compilation time
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Lightweight regex engine that optimizes for binary size and compilation time
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+string-devel
Summary:        Lightweight regex engine that optimizes for binary size and compilation time
BuildArch:      noarch
%description -n %{name}+string-devel

This package contains library source intended for building other packages which
use the "string" feature of the "%{crate}" crate.

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

%cargo_test -- --lib
%cargo_test -- --doc
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-regex-lite-devel -f %{oreon_filedir}/rust-regex-lite-devel.list

%changelog

%autochangelog
