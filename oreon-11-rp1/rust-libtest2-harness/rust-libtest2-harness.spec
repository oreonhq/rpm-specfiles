%global source0_hash 1ca907aef7f70aceecb01e88588062946dd0af0727d80a68d9a1e928dacf07c9
%bcond check 0
%global debug_package %{nil}
%global crate libtest2-harness
Name:           rust-libtest2-harness
Version:        0.0.3
Release:        1%{?dist}
Summary:        An experimental replacement for the core of libtest
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/libtest2-harness
Source0:        https://static.crates.io/crates/libtest2-harness/libtest2-harness-%{version}.crate
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
Summary:        An experimental replacement for the core of libtest
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+color-devel
Summary:        An experimental replacement for the core of libtest
BuildArch:      noarch
%description -n %{name}+color-devel

This package contains library source intended for building other packages which
use the "color" feature of the "%{crate}" crate.

%package     -n %{name}+threads-devel
Summary:        An experimental replacement for the core of libtest
BuildArch:      noarch
%description -n %{name}+threads-devel

This package contains library source intended for building other packages which
use the "threads" feature of the "%{crate}" crate.

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
%files -n rust-libtest2-harness-devel -f %{oreon_filedir}/rust-libtest2-harness-devel.list

%changelog

%autochangelog
