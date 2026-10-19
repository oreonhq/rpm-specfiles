%global source0_hash 18f12cc9948ed9604230cdddc7c86e270f9401ccbe3c2e98a4378c5e7632212f
%bcond check 1
%global debug_package %{nil}
%global crate const-str
Name:           rust-const-str
Version:        1.1.0
Release:        1%{?dist}
Summary:        Compile-time string operations
License:        MIT
URL:            https://crates.io/crates/const-str
Source0:        https://static.crates.io/crates/const-str/const-str-%{version}.crate
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
Summary:        Compile-time string operations
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+all-devel
Summary:        Compile-time string operations
BuildArch:      noarch
%description -n %{name}+all-devel

This package contains library source intended for building other packages which
use the "all" feature of the "%{crate}" crate.

%package     -n %{name}+case-devel
Summary:        Compile-time string operations
BuildArch:      noarch
%description -n %{name}+case-devel

This package contains library source intended for building other packages which
use the "case" feature of the "%{crate}" crate.

%package     -n %{name}+http-devel
Summary:        Compile-time string operations
BuildArch:      noarch
%description -n %{name}+http-devel

This package contains library source intended for building other packages which
use the "http" feature of the "%{crate}" crate.

%package     -n %{name}+proc-devel
Summary:        Compile-time string operations
BuildArch:      noarch
%description -n %{name}+proc-devel

This package contains library source intended for building other packages which
use the "proc" feature of the "%{crate}" crate.

%package     -n %{name}+regex-devel
Summary:        Compile-time string operations
BuildArch:      noarch
%description -n %{name}+regex-devel

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Compile-time string operations
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Compile-time string operations
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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
%files -n rust-const-str-devel -f %{oreon_filedir}/rust-const-str-devel.list

%changelog

%autochangelog
