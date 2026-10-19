%global source0_hash 45b60258a35dc3cb8a16890b8fd6723349bfa458d7960e25e633f1b1c19d7b5e
%bcond check 0
%global debug_package %{nil}
%global crate simple_logger
Name:           rust-simple_logger1
Version:        1.16.0
Release:        1%{?dist}
Summary:        Logger that prints all messages with a readable output format
License:        MIT
URL:            https://crates.io/crates/simple_logger
Source0:        https://static.crates.io/crates/simple_logger/simple_logger-%{version}.crate
Patch:          simple_logger-fix-metadata-auto.diff
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
Summary:        Logger that prints all messages with a readable output format
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+colored-devel
Summary:        Logger that prints all messages with a readable output format
BuildArch:      noarch
%description -n %{name}+colored-devel

This package contains library source intended for building other packages which
use the "colored" feature of the "%{crate}" crate.

%package     -n %{name}+colors-devel
Summary:        Logger that prints all messages with a readable output format
BuildArch:      noarch
%description -n %{name}+colors-devel

This package contains library source intended for building other packages which
use the "colors" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Logger that prints all messages with a readable output format
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+stderr-devel
Summary:        Logger that prints all messages with a readable output format
BuildArch:      noarch
%description -n %{name}+stderr-devel

This package contains library source intended for building other packages which
use the "stderr" feature of the "%{crate}" crate.

%package     -n %{name}+threads-devel
Summary:        Logger that prints all messages with a readable output format
BuildArch:      noarch
%description -n %{name}+threads-devel

This package contains library source intended for building other packages which
use the "threads" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        Logger that prints all messages with a readable output format
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+timestamps-devel
Summary:        Logger that prints all messages with a readable output format
BuildArch:      noarch
%description -n %{name}+timestamps-devel

This package contains library source intended for building other packages which
use the "timestamps" feature of the "%{crate}" crate.

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
%files -n rust-simple_logger1-devel -f %{oreon_filedir}/rust-simple_logger1-devel.list

%changelog

%autochangelog
