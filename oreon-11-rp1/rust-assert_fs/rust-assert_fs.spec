%global source0_hash a652f6cb1f516886fcfee5e7a5c078b9ade62cfcb889524efe5a64d682dd27a9
%bcond check 1
%global debug_package %{nil}
%global crate assert_fs
Name:           rust-assert_fs
Version:        1.1.3
Release:        1%{?dist}
Summary:        Filesystem fixtures and assertions for testing
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/assert_fs
Source0:        https://static.crates.io/crates/assert_fs/assert_fs-%{version}.crate
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
Summary:        Filesystem fixtures and assertions for testing
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+color-devel
Summary:        Filesystem fixtures and assertions for testing
BuildArch:      noarch
%description -n %{name}+color-devel

This package contains library source intended for building other packages which
use the "color" feature of the "%{crate}" crate.

%package     -n %{name}+color-auto-devel
Summary:        Filesystem fixtures and assertions for testing
BuildArch:      noarch
%description -n %{name}+color-auto-devel

This package contains library source intended for building other packages which
use the "color-auto" feature of the "%{crate}" crate.

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

%cargo_test -- -- --skip assert::test::into_path_from_
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-assert_fs-devel -f %{oreon_filedir}/rust-assert_fs-devel.list

%changelog

%autochangelog
