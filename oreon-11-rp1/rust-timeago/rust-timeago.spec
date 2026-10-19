%global source0_hash a1710e589de0a76aaf295cd47a6699f6405737dbfd3cf2b75c92d000b548d0e6
%bcond check 0
%global debug_package %{nil}
%global crate timeago
Name:           rust-timeago
Version:        0.4.2
Release:        1%{?dist}
Summary:        Given a Duration, lossily format it like in 'N days ago'
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/timeago
Source0:        https://static.crates.io/crates/timeago/timeago-%{version}.crate
Patch:          timeago-fix-metadata.diff
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
Summary:        Given a Duration, lossily format it like in 'N days ago'
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Given a Duration, lossily format it like in 'N days ago'
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+translations-devel
Summary:        Given a Duration, lossily format it like in 'N days ago'
BuildArch:      noarch
%description -n %{name}+translations-devel

This package contains library source intended for building other packages which
use the "translations" feature of the "%{crate}" crate.

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
%files -n rust-timeago-devel -f %{oreon_filedir}/rust-timeago-devel.list

%changelog

%autochangelog
