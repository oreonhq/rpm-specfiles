%global source1_hash 8b1ef5e462f88986263c73e31cf888f9bbc0211026c3354aa05847a3b7a93b6f
%global source0_hash 2a197e44322788858682406c74b0b59bf8d9b4954fe1f224d9a25147f1880bba
%bcond check 0
%global debug_package %{nil}
%global crate maxminddb
%global testdata_commit a8ae5b4ac0aa730e2783f708cdaa208aca20e9ec
%global testdata_short  %(c=%{testdata_commit}; echo ${c:0:7})
Name:           rust-maxminddb
Version:        0.26.0
Release:        1%{?dist}
Summary:        Library for reading MaxMind DB format used by GeoIP2 and GeoLite2
License:        ISC
URL:            https://crates.io/crates/maxminddb
Source0:        https://static.crates.io/crates/maxminddb/maxminddb-%{version}.crate
Source1:        https://github.com/maxmind/MaxMind-DB/archive/%{testdata_commit}/test-data-%{testdata_short}.tar.gz
Patch:          maxminddb-fix-metadata.diff
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
Summary:        Library for reading MaxMind DB format used by GeoIP2 and GeoLite2
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+memmap2-devel
Summary:        Library for reading MaxMind DB format used by GeoIP2 and GeoLite2
BuildArch:      noarch
%description -n %{name}+memmap2-devel

This package contains library source intended for building other packages which
use the "memmap2" feature of the "%{crate}" crate.

%package     -n %{name}+mmap-devel
Summary:        Library for reading MaxMind DB format used by GeoIP2 and GeoLite2
BuildArch:      noarch
%description -n %{name}+mmap-devel

This package contains library source intended for building other packages which
use the "mmap" feature of the "%{crate}" crate.

%package     -n %{name}+simdutf8-devel
Summary:        Library for reading MaxMind DB format used by GeoIP2 and GeoLite2
BuildArch:      noarch
%description -n %{name}+simdutf8-devel

This package contains library source intended for building other packages which
use the "simdutf8" feature of the "%{crate}" crate.

%package     -n %{name}+unsafe-str-decode-devel
Summary:        Library for reading MaxMind DB format used by GeoIP2 and GeoLite2
BuildArch:      noarch
%description -n %{name}+unsafe-str-decode-devel

This package contains library source intended for building other packages which
use the "unsafe-str-decode" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1 -a1
mv MaxMind-DB-%{testdata_commit} test-data
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
%files -n rust-maxminddb-devel -f %{oreon_filedir}/rust-maxminddb-devel.list

%changelog

%autochangelog
