%global source0_hash ebcbec2b9a580ddee352ac38523d2ecd4dcaad53532957034394556909e27f4b
%bcond check 1
%global debug_package %{nil}
%global crate dircpy
Name:           rust-dircpy
Version:        0.3.20
Release:        1%{?dist}
Summary:        Copy directories recursively with flexible options
License:        MIT
URL:            https://crates.io/crates/dircpy
Source0:        https://static.crates.io/crates/dircpy/dircpy-%{version}.crate
Patch:          dircpy-fix-metadata.diff
Patch2:         0001-drop-a-test-that-requires-internet-connectivity.patch
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
Summary:        Copy directories recursively with flexible options
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+jwalk-devel
Summary:        Copy directories recursively with flexible options
BuildArch:      noarch
%description -n %{name}+jwalk-devel

This package contains library source intended for building other packages which
use the "jwalk" feature of the "%{crate}" crate.

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
%files -n rust-dircpy-devel -f %{oreon_filedir}/rust-dircpy-devel.list

%changelog

%autochangelog
