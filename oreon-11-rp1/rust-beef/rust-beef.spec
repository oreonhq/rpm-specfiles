%global source0_hash 3a8241f3ebb85c056b509d4327ad0358fbbba6ffb340bf388f26350aeda225b1
%bcond check 0
%global debug_package %{nil}
%global crate beef
Name:           rust-beef
Version:        0.5.2
Release:        1%{?dist}
Summary:        More compact Cow
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/beef
Source0:        https://static.crates.io/crates/beef/beef-%{version}.crate
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
Summary:        More compact Cow
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+const_fn-devel
Summary:        More compact Cow
BuildArch:      noarch
%description -n %{name}+const_fn-devel

This package contains library source intended for building other packages which
use the "const_fn" feature of the "%{crate}" crate.

%package     -n %{name}+impl_serde-devel
Summary:        More compact Cow
BuildArch:      noarch
%description -n %{name}+impl_serde-devel

This package contains library source intended for building other packages which
use the "impl_serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        More compact Cow
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-beef-devel -f %{oreon_filedir}/rust-beef-devel.list

%changelog

%autochangelog
