%global source0_hash 0fbc8f9818a6fad141d85993777ba298ee52c80a09bd23d45dda461a6b7c83cb
%bcond check 0
%global debug_package %{nil}
%global crate sequoia-openpgp
Name:           rust-sequoia-openpgp
Version:        2.4.1
Release:        1%{?dist}
Summary:        OpenPGP data types and associated machinery
License:        LGPL-2.0-or-later
URL:            https://crates.io/crates/sequoia-openpgp
Source0:        https://static.crates.io/crates/sequoia-openpgp/sequoia-openpgp-%{version}.crate
Patch:          sequoia-openpgp-fix-metadata-auto.diff
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
Summary:        OpenPGP data types and associated machinery
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__implicit-crypto-backend-for-tests-devel
Summary:        OpenPGP data types and associated machinery
BuildArch:      noarch
%description -n %{name}+__implicit-crypto-backend-for-tests-devel

This package contains library source intended for building other packages which
use the "__implicit-crypto-backend-for-tests" feature of the "%{crate}" crate.

%package     -n %{name}+allow-experimental-crypto-devel
Summary:        OpenPGP data types and associated machinery
BuildArch:      noarch
%description -n %{name}+allow-experimental-crypto-devel

This package contains library source intended for building other packages which
use the "allow-experimental-crypto" feature of the "%{crate}" crate.

%package     -n %{name}+allow-variable-time-crypto-devel
Summary:        OpenPGP data types and associated machinery
BuildArch:      noarch
%description -n %{name}+allow-variable-time-crypto-devel

This package contains library source intended for building other packages which
use the "allow-variable-time-crypto" feature of the "%{crate}" crate.

%package     -n %{name}+compression-devel
Summary:        OpenPGP data types and associated machinery
BuildArch:      noarch
%description -n %{name}+compression-devel

This package contains library source intended for building other packages which
use the "compression" feature of the "%{crate}" crate.

%package     -n %{name}+compression-bzip2-devel
Summary:        OpenPGP data types and associated machinery
BuildArch:      noarch
%description -n %{name}+compression-bzip2-devel

This package contains library source intended for building other packages which
use the "compression-bzip2" feature of the "%{crate}" crate.

%package     -n %{name}+compression-deflate-devel
Summary:        OpenPGP data types and associated machinery
BuildArch:      noarch
%description -n %{name}+compression-deflate-devel

This package contains library source intended for building other packages which
use the "compression-deflate" feature of the "%{crate}" crate.

%package     -n %{name}+crypto-botan-devel
Summary:        OpenPGP data types and associated machinery
BuildArch:      noarch
%description -n %{name}+crypto-botan-devel

This package contains library source intended for building other packages which
use the "crypto-botan" feature of the "%{crate}" crate.

%package     -n %{name}+crypto-botan2-devel
Summary:        OpenPGP data types and associated machinery
BuildArch:      noarch
%description -n %{name}+crypto-botan2-devel

This package contains library source intended for building other packages which
use the "crypto-botan2" feature of the "%{crate}" crate.

%package     -n %{name}+crypto-cng-devel
Summary:        OpenPGP data types and associated machinery
BuildArch:      noarch
%description -n %{name}+crypto-cng-devel

This package contains library source intended for building other packages which
use the "crypto-cng" feature of the "%{crate}" crate.

%package     -n %{name}+crypto-fuzzing-devel
Summary:        OpenPGP data types and associated machinery
BuildArch:      noarch
%description -n %{name}+crypto-fuzzing-devel

This package contains library source intended for building other packages which
use the "crypto-fuzzing" feature of the "%{crate}" crate.

%package     -n %{name}+crypto-nettle-devel
Summary:        OpenPGP data types and associated machinery
BuildArch:      noarch
%description -n %{name}+crypto-nettle-devel

This package contains library source intended for building other packages which
use the "crypto-nettle" feature of the "%{crate}" crate.

%package     -n %{name}+crypto-openssl-devel
Summary:        OpenPGP data types and associated machinery
BuildArch:      noarch
%description -n %{name}+crypto-openssl-devel

This package contains library source intended for building other packages which
use the "crypto-openssl" feature of the "%{crate}" crate.

%package     -n %{name}+crypto-rust-devel
Summary:        OpenPGP data types and associated machinery
BuildArch:      noarch
%description -n %{name}+crypto-rust-devel

This package contains library source intended for building other packages which
use the "crypto-rust" feature of the "%{crate}" crate.

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
%files -n rust-sequoia-openpgp-devel -f %{oreon_filedir}/rust-sequoia-openpgp-devel.list

%changelog

%autochangelog
