%global source0_hash b91aa448ca50d7e79433bdf3ee8d99215430d2ec02ade5aefab2a073a1822e8a
%bcond check 0
%global debug_package %{nil}
%global crate fs-err
Name:           rust-fs-err
Version:        3.3.1
Release:        1%{?dist}
Summary:        Drop-in replacement for std::fs with more helpful error messages
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/fs-err
Source0:        https://static.crates.io/crates/fs-err/fs-err-%{version}.crate
Patch:          fs-err-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  dos2unix
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
Summary:        Drop-in replacement for std::fs with more helpful error messages
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+expose_original_error-devel
Summary:        Drop-in replacement for std::fs with more helpful error messages
BuildArch:      noarch
%description -n %{name}+expose_original_error-devel

This package contains library source intended for building other packages which
use the "expose_original_error" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Drop-in replacement for std::fs with more helpful error messages
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
find . -type f \( -name 'LICENSE*' -o -name '*.md' -o -name '*.rs' \) \
-exec dos2unix --keepdate '{}' '+'
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
%files -n rust-fs-err-devel -f %{oreon_filedir}/rust-fs-err-devel.list

%changelog

%autochangelog
