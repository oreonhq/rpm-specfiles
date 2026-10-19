%global source0_hash f093b3db6fd194718dcdeea6bd8c829417deae904e3fcc7732dabcd4416d25d8
%bcond check 0
%global debug_package %{nil}
%global crate ndarray-rand
Name:           rust-ndarray-rand
Version:        0.15.0
Release:        1%{?dist}
Summary:        Constructors for randomized arrays. rand integration for ndarray
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ndarray-rand
Source0:        https://static.crates.io/crates/ndarray-rand/ndarray-rand-%{version}.crate
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
Summary:        Constructors for randomized arrays. rand integration for ndarray
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+quickcheck-devel
Summary:        Constructors for randomized arrays. rand integration for ndarray
BuildArch:      noarch
%description -n %{name}+quickcheck-devel

This package contains library source intended for building other packages which
use the "quickcheck" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -a
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-ndarray-rand-devel -f %{oreon_filedir}/rust-ndarray-rand-devel.list

%changelog

%autochangelog
