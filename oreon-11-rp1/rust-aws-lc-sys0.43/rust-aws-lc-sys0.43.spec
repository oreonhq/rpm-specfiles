%global source0_hash 43103168cc76fe62678a375e722fc9cb3a0146159ac5828bc4f0dfd755c2224c
%bcond check 0
%global debug_package %{nil}
%global crate aws-lc-sys
Name:           rust-aws-lc-sys0.43
Version:        0.43.0
Release:        1%{?dist}
Summary:        AWS-LC is a general-purpose cryptographic library maintained by the A...
License:        ISC AND (Apache-2.0 OR ISC) AND Apache-2.0 AND MIT AND BSD-3-Clause AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR ISC OR MIT-0)
URL:            https://crates.io/crates/aws-lc-sys
Source0:        https://static.crates.io/crates/aws-lc-sys/aws-lc-sys-%{version}.crate
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
Summary:        AWS-LC is a general-purpose cryptographic library maintained by the A...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+all-bindings-devel
Summary:        AWS-LC is a general-purpose cryptographic library maintained by the A...
BuildArch:      noarch
%description -n %{name}+all-bindings-devel

This package contains library source intended for building other packages which
use the "all-bindings" feature of the "%{crate}" crate.

%package     -n %{name}+asan-devel
Summary:        AWS-LC is a general-purpose cryptographic library maintained by the A...
BuildArch:      noarch
%description -n %{name}+asan-devel

This package contains library source intended for building other packages which
use the "asan" feature of the "%{crate}" crate.

%package     -n %{name}+bindgen-devel
Summary:        AWS-LC is a general-purpose cryptographic library maintained by the A...
BuildArch:      noarch
%description -n %{name}+bindgen-devel

This package contains library source intended for building other packages which
use the "bindgen" feature of the "%{crate}" crate.

%package     -n %{name}+disable-prebuilt-nasm-devel
Summary:        AWS-LC is a general-purpose cryptographic library maintained by the A...
BuildArch:      noarch
%description -n %{name}+disable-prebuilt-nasm-devel

This package contains library source intended for building other packages which
use the "disable-prebuilt-nasm" feature of the "%{crate}" crate.

%package     -n %{name}+fips-devel
Summary:        AWS-LC is a general-purpose cryptographic library maintained by the A...
BuildArch:      noarch
%description -n %{name}+fips-devel

This package contains library source intended for building other packages which
use the "fips" feature of the "%{crate}" crate.

%package     -n %{name}+prebuilt-nasm-devel
Summary:        AWS-LC is a general-purpose cryptographic library maintained by the A...
BuildArch:      noarch
%description -n %{name}+prebuilt-nasm-devel

This package contains library source intended for building other packages which
use the "prebuilt-nasm" feature of the "%{crate}" crate.

%package     -n %{name}+ssl-devel
Summary:        AWS-LC is a general-purpose cryptographic library maintained by the A...
BuildArch:      noarch
%description -n %{name}+ssl-devel

This package contains library source intended for building other packages which
use the "ssl" feature of the "%{crate}" crate.

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
%files -n rust-aws-lc-sys0.43-devel -f %{oreon_filedir}/rust-aws-lc-sys0.43-devel.list

%changelog

%autochangelog
