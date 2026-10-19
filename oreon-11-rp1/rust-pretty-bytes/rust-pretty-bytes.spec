%global source0_hash 009d6edd2c1dbf2e1c0cd48a2f7766e03498d49ada7109a01c6911815c685316
%bcond check 1
%global crate pretty-bytes
Name:           rust-pretty-bytes
Version:        0.2.2
Release:        1%{?dist}
Summary:        Convert bytes to a human readable string
License:        MIT
URL:            https://crates.io/crates/pretty-bytes
Source0:        https://static.crates.io/crates/pretty-bytes/pretty-bytes-%{version}.crate
Patch:          pretty-bytes-fix-metadata.diff
Patch10:        https://github.com/banyan/rust-pretty-bytes/pull/9.patch#/%{crate}-add-license.diff
Patch11:        pretty-bytes-0.2.2-no-atty.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Convert bytes to a human readable string
License:        MIT AND (MIT OR Apache-2.0)
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Convert bytes to a human readable string
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
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n pretty-bytes -f %{oreon_filedir}/pretty-bytes.list
%files -n rust-pretty-bytes-devel -f %{oreon_filedir}/rust-pretty-bytes-devel.list

%changelog

%autochangelog
