%global source0_hash fabe6324e908f85a1c52063ce7aa26b68dcb7eb6dbc83a2d148403c9bc3eba50
%bcond check 1
%global debug_package %{nil}
%global crate zip
Name:           rust-zip2
Version:        2.4.2
Release:        1%{?dist}
Summary:        Library to support the reading and writing of zip files
License:        MIT
URL:            https://crates.io/crates/zip
Source0:        https://static.crates.io/crates/zip/zip-%{version}.crate
Source10:       zip2-%{version}-filtered.tar.gz
Source11:       get_test_data.sh
Patch:          zip-fix-metadata-auto.diff
Patch:          zip-fix-metadata.diff
Patch10:        zip-2.1.4-omitted-test-files.patch
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
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+_all-features-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+_all-features-devel

This package contains library source intended for building other packages which
use the "_all-features" feature of the "%{crate}" crate.

%package     -n %{name}+_deflate-any-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+_deflate-any-devel

This package contains library source intended for building other packages which
use the "_deflate-any" feature of the "%{crate}" crate.

%package     -n %{name}+aes-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+aes-devel

This package contains library source intended for building other packages which
use the "aes" feature of the "%{crate}" crate.

%package     -n %{name}+aes-crypto-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+aes-crypto-devel

This package contains library source intended for building other packages which
use the "aes-crypto" feature of the "%{crate}" crate.

%package     -n %{name}+bzip2-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+bzip2-devel

This package contains library source intended for building other packages which
use the "bzip2" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+constant_time_eq-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+constant_time_eq-devel

This package contains library source intended for building other packages which
use the "constant_time_eq" feature of the "%{crate}" crate.

%package     -n %{name}+deflate-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+deflate-devel

This package contains library source intended for building other packages which
use the "deflate" feature of the "%{crate}" crate.

%package     -n %{name}+deflate-flate2-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+deflate-flate2-devel

This package contains library source intended for building other packages which
use the "deflate-flate2" feature of the "%{crate}" crate.

%package     -n %{name}+deflate-miniz-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+deflate-miniz-devel

This package contains library source intended for building other packages which
use the "deflate-miniz" feature of the "%{crate}" crate.

%package     -n %{name}+deflate-zlib-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+deflate-zlib-devel

This package contains library source intended for building other packages which
use the "deflate-zlib" feature of the "%{crate}" crate.

%package     -n %{name}+deflate-zlib-ng-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+deflate-zlib-ng-devel

This package contains library source intended for building other packages which
use the "deflate-zlib-ng" feature of the "%{crate}" crate.

%package     -n %{name}+deflate-zopfli-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+deflate-zopfli-devel

This package contains library source intended for building other packages which
use the "deflate-zopfli" feature of the "%{crate}" crate.

%package     -n %{name}+deflate64-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+deflate64-devel

This package contains library source intended for building other packages which
use the "deflate64" feature of the "%{crate}" crate.

%package     -n %{name}+flate2-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+flate2-devel

This package contains library source intended for building other packages which
use the "flate2" feature of the "%{crate}" crate.

%package     -n %{name}+getrandom-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+getrandom-devel

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%package     -n %{name}+hmac-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+hmac-devel

This package contains library source intended for building other packages which
use the "hmac" feature of the "%{crate}" crate.

%package     -n %{name}+lzma-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+lzma-devel

This package contains library source intended for building other packages which
use the "lzma" feature of the "%{crate}" crate.

%package     -n %{name}+lzma-rs-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+lzma-rs-devel

This package contains library source intended for building other packages which
use the "lzma-rs" feature of the "%{crate}" crate.

%package     -n %{name}+pbkdf2-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+pbkdf2-devel

This package contains library source intended for building other packages which
use the "pbkdf2" feature of the "%{crate}" crate.

%package     -n %{name}+sha1-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+sha1-devel

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+unreserved-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+unreserved-devel

This package contains library source intended for building other packages which
use the "unreserved" feature of the "%{crate}" crate.

%package     -n %{name}+xz-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+xz-devel

This package contains library source intended for building other packages which
use the "xz" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+zeroize-devel

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

%package     -n %{name}+zopfli-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+zopfli-devel

This package contains library source intended for building other packages which
use the "zopfli" feature of the "%{crate}" crate.

%package     -n %{name}+zstd-devel
Summary:        Library to support the reading and writing of zip files
BuildArch:      noarch
%description -n %{name}+zstd-devel

This package contains library source intended for building other packages which
use the "zstd" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

tar -xzvf '%{SOURCE10}' --strip-components=1 'zip2-%{version}/tests/data/'
cp -vp '%{SOURCE11}' tests/data/
%cargo_test -a
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-zip2-devel -f %{oreon_filedir}/rust-zip2-devel.list

%changelog

%autochangelog
