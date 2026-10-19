%global source0_hash 72753e0008ea87963d2f0770042d0df7abe51fafbb8dcaf618ac440f2f1fec0a
%bcond check 1
%global debug_package %{nil}
%global crate libdeflate-sys
Name:           rust-libdeflate-sys
Version:        1.25.2
Release:        1%{?dist}
Summary:        Bindings to libdeflate for DEFLATE
License:        Apache-2.0
URL:            https://crates.io/crates/libdeflate-sys
Source0:        https://static.crates.io/crates/libdeflate-sys/libdeflate-sys-%{version}.crate
Patch:          libdeflate-sys-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(libdeflate)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libdeflate)
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Bindings to libdeflate for DEFLATE
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+dynamic-devel
Summary:        Bindings to libdeflate for DEFLATE
BuildArch:      noarch
%description -n %{name}+dynamic-devel

This package contains library source intended for building other packages which
use the "dynamic" feature of the "%{crate}" crate.

%package     -n %{name}+freestanding-devel
Summary:        Bindings to libdeflate for DEFLATE
BuildArch:      noarch
%description -n %{name}+freestanding-devel

This package contains library source intended for building other packages which
use the "freestanding" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -rv libdeflate
sed -r -i 's@^([[:blank:]]*)(#\[cfg\(feature *= *"dynamic"\)\])@\1// \2@' build.rs
sed -r -i 's@^([[:blank:]]*)(\.exactly_version\()@\1// \2@' build.rs
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
%files -n rust-libdeflate-sys-devel -f %{oreon_filedir}/rust-libdeflate-sys-devel.list

%changelog

%autochangelog
