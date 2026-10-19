%global source0_hash cb7af949edc773f32dd45ff5a0692860b619b03d2fa3741c1db1acfd1db3a553
%bcond check 0
%global crate libopenraw
%global crate_version 0.4.0-alpha.12
Name:           rust-libopenraw
Version:        0.4.0~alpha.12
Release:        1%{?dist}
Summary:        Digital camera RAW file processing
License:        LGPL-3.0-or-later
URL:            https://crates.io/crates/libopenraw
Source0:        https://crates.io/api/v1/crates/%{crate}/%{crate_version}/download#/%{crate}-%{crate_version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Digital camera RAW file processing
License:        # FIXME
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Digital camera RAW file processing
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+3gpp-devel
Summary:        Digital camera RAW file processing
BuildArch:      noarch
%description -n %{name}+3gpp-devel

This package contains library source intended for building other packages which
use the "3gpp" feature of the "%{crate}" crate.

%package     -n %{name}+afl-devel
Summary:        Digital camera RAW file processing
BuildArch:      noarch
%description -n %{name}+afl-devel

This package contains library source intended for building other packages which
use the "afl" feature of the "%{crate}" crate.

%package     -n %{name}+bench-devel
Summary:        Digital camera RAW file processing
BuildArch:      noarch
%description -n %{name}+bench-devel

This package contains library source intended for building other packages which
use the "bench" feature of the "%{crate}" crate.

%package     -n %{name}+book-devel
Summary:        Digital camera RAW file processing
BuildArch:      noarch
%description -n %{name}+book-devel

This package contains library source intended for building other packages which
use the "book" feature of the "%{crate}" crate.

%package     -n %{name}+capi-devel
Summary:        Digital camera RAW file processing
BuildArch:      noarch
%description -n %{name}+capi-devel

This package contains library source intended for building other packages which
use the "capi" feature of the "%{crate}" crate.

%package     -n %{name}+dump-devel
Summary:        Digital camera RAW file processing
BuildArch:      noarch
%description -n %{name}+dump-devel

This package contains library source intended for building other packages which
use the "dump" feature of the "%{crate}" crate.

%package     -n %{name}+fuzzing-devel
Summary:        Digital camera RAW file processing
BuildArch:      noarch
%description -n %{name}+fuzzing-devel

This package contains library source intended for building other packages which
use the "fuzzing" feature of the "%{crate}" crate.

%package     -n %{name}+libc-devel
Summary:        Digital camera RAW file processing
BuildArch:      noarch
%description -n %{name}+libc-devel

This package contains library source intended for building other packages which
use the "libc" feature of the "%{crate}" crate.

%package     -n %{name}+meta-xml-devel
Summary:        Digital camera RAW file processing
BuildArch:      noarch
%description -n %{name}+meta-xml-devel

This package contains library source intended for building other packages which
use the "meta-xml" feature of the "%{crate}" crate.

%package     -n %{name}+missing-pixi-permitted-devel
Summary:        Digital camera RAW file processing
BuildArch:      noarch
%description -n %{name}+missing-pixi-permitted-devel

This package contains library source intended for building other packages which
use the "missing-pixi-permitted" feature of the "%{crate}" crate.

%package     -n %{name}+mp4v-devel
Summary:        Digital camera RAW file processing
BuildArch:      noarch
%description -n %{name}+mp4v-devel

This package contains library source intended for building other packages which
use the "mp4v" feature of the "%{crate}" crate.

%package     -n %{name}+multimap-devel
Summary:        Digital camera RAW file processing
BuildArch:      noarch
%description -n %{name}+multimap-devel

This package contains library source intended for building other packages which
use the "multimap" feature of the "%{crate}" crate.

%package     -n %{name}+probe-devel
Summary:        Digital camera RAW file processing
BuildArch:      noarch
%description -n %{name}+probe-devel

This package contains library source intended for building other packages which
use the "probe" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-api-devel
Summary:        Digital camera RAW file processing
BuildArch:      noarch
%description -n %{name}+unstable-api-devel

This package contains library source intended for building other packages which
use the "unstable-api" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{crate_version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f book,fuzzing
%{cargo_license_summary -f book,fuzzing}
%{cargo_license -f book,fuzzing} > LICENSE.dependencies
%install
%cargo_install -f book,fuzzing
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f book,fuzzing
%endif
%files -f %{oreon_filedir}/main.list
%files -n libopenraw -f %{oreon_filedir}/libopenraw.list
%files -n rust-libopenraw-devel -f %{oreon_filedir}/rust-libopenraw-devel.list

%changelog

%autochangelog
