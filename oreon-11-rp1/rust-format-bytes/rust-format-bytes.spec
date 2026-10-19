%global source0_hash 48942366ef93975da38e175ac9e10068c6fc08ca9e85930d4f098f4d5b14c2fd
%bcond check 0
%global debug_package %{nil}
%global crate format-bytes
Name:           rust-format-bytes
Version:        0.3.0
Release:        1%{?dist}
Summary:        Macro to format bytestrings
License:        MIT
URL:            https://crates.io/crates/format-bytes
Source0:        https://static.crates.io/crates/format-bytes/format-bytes-%{version}.crate
Patch:          format-bytes-fix-metadata.diff
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
Summary:        Macro to format bytestrings
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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

export TRYBUILD=overwrite
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-format-bytes-devel -f %{oreon_filedir}/rust-format-bytes-devel.list

%changelog

%autochangelog
