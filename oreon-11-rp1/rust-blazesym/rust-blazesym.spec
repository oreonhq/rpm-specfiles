%global source0_hash 519a0f9df086d6c4f44576558523a777c984454daeb124bee79bde69227360c4
%bcond check 0
%global debug_package %{nil}
%global crate blazesym
%global crate_version 0.2.0-rc.0
Name:           rust-blazesym
Version:        0.2.0~rc.0
Release:        1%{?dist}
Summary:        Library for address symbolization and related tasks
License:        BSD-3-Clause
URL:            https://crates.io/crates/blazesym
Source0:        https://crates.io/api/v1/crates/%{crate}/%{crate_version}/download#/%{crate}-%{crate_version}.crate
Patch:          blazesym-fix-metadata.diff
Patch10:        blazesym-0.2.0-rc.0-cpp_demangle-0.5.patch
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
Summary:        Library for address symbolization and related tasks
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+apk-devel
Summary:        Library for address symbolization and related tasks
BuildArch:      noarch
%description -n %{name}+apk-devel

This package contains library source intended for building other packages which
use the "apk" feature of the "%{crate}" crate.

%package     -n %{name}+backtrace-devel
Summary:        Library for address symbolization and related tasks
BuildArch:      noarch
%description -n %{name}+backtrace-devel

This package contains library source intended for building other packages which
use the "backtrace" feature of the "%{crate}" crate.

%package     -n %{name}+breakpad-devel
Summary:        Library for address symbolization and related tasks
BuildArch:      noarch
%description -n %{name}+breakpad-devel

This package contains library source intended for building other packages which
use the "breakpad" feature of the "%{crate}" crate.

%package     -n %{name}+demangle-devel
Summary:        Library for address symbolization and related tasks
BuildArch:      noarch
%description -n %{name}+demangle-devel

This package contains library source intended for building other packages which
use the "demangle" feature of the "%{crate}" crate.

%package     -n %{name}+dwarf-devel
Summary:        Library for address symbolization and related tasks
BuildArch:      noarch
%description -n %{name}+dwarf-devel

This package contains library source intended for building other packages which
use the "dwarf" feature of the "%{crate}" crate.

%package     -n %{name}+gsym-devel
Summary:        Library for address symbolization and related tasks
BuildArch:      noarch
%description -n %{name}+gsym-devel

This package contains library source intended for building other packages which
use the "gsym" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        Library for address symbolization and related tasks
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

%package     -n %{name}+zlib-devel
Summary:        Library for address symbolization and related tasks
BuildArch:      noarch
%description -n %{name}+zlib-devel

This package contains library source intended for building other packages which
use the "zlib" feature of the "%{crate}" crate.

%package     -n %{name}+zstd-devel
Summary:        Library for address symbolization and related tasks
BuildArch:      noarch
%description -n %{name}+zstd-devel

This package contains library source intended for building other packages which
use the "zstd" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{crate_version} -p1
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
%files -n rust-blazesym-devel -f %{oreon_filedir}/rust-blazesym-devel.list

%changelog

%autochangelog
