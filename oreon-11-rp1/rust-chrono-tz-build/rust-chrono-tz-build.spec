%global source0_hash c7d8d1efd5109b9c1cd3b7966bd071cdfb53bb6eb0b22a473a68c2f70a11a1eb
%bcond check 0
%global debug_package %{nil}
%global crate chrono-tz-build
Name:           rust-chrono-tz-build
Version:        0.5.0
Release:        1%{?dist}
Summary:        internal build script for chrono-tz
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/chrono-tz-build
Source0:        https://static.crates.io/crates/chrono-tz-build/chrono-tz-build-%{version}.crate
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

%package     -n %{name}+case-insensitive-devel
Summary:        internal build script for chrono-tz
BuildArch:      noarch
%description -n %{name}+case-insensitive-devel

This package contains library source intended for building other packages which
use the "case-insensitive" feature of the "%{crate}" crate.

%package     -n %{name}+filter-by-regex-devel
Summary:        internal build script for chrono-tz
BuildArch:      noarch
%description -n %{name}+filter-by-regex-devel

This package contains library source intended for building other packages which
use the "filter-by-regex" feature of the "%{crate}" crate.

%package     -n %{name}+phf_shared-devel
Summary:        internal build script for chrono-tz
BuildArch:      noarch
%description -n %{name}+phf_shared-devel

This package contains library source intended for building other packages which
use the "phf_shared" feature of the "%{crate}" crate.

%package     -n %{name}+regex-devel
Summary:        internal build script for chrono-tz
BuildArch:      noarch
%description -n %{name}+regex-devel

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%package     -n %{name}+uncased-devel
Summary:        internal build script for chrono-tz
BuildArch:      noarch
%description -n %{name}+uncased-devel

This package contains library source intended for building other packages which
use the "uncased" feature of the "%{crate}" crate.

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
%files -n rust-chrono-tz-build-devel -f %{oreon_filedir}/rust-chrono-tz-build-devel.list

%changelog

%autochangelog
