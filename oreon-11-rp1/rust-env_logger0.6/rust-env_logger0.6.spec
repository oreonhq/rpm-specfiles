%global source0_hash aafcde04e90a5226a6443b7aabdb016ba2f8307c847d524724bd9b346dd1a2d3
%bcond check 0
%global debug_package %{nil}
%global crate env_logger
Name:           rust-env_logger0.6
Version:        0.6.2
Release:        1%{?dist}
Summary:        A logging implementation for `log` which is configured via an environ...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/env_logger
Source0:        https://static.crates.io/crates/env_logger/env_logger-%{version}.crate
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
Summary:        A logging implementation for `log` which is configured via an environ...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+atty-devel
Summary:        A logging implementation for `log` which is configured via an environ...
BuildArch:      noarch
%description -n %{name}+atty-devel

This package contains library source intended for building other packages which
use the "atty" feature of the "%{crate}" crate.

%package     -n %{name}+humantime-devel
Summary:        A logging implementation for `log` which is configured via an environ...
BuildArch:      noarch
%description -n %{name}+humantime-devel

This package contains library source intended for building other packages which
use the "humantime" feature of the "%{crate}" crate.

%package     -n %{name}+regex-devel
Summary:        A logging implementation for `log` which is configured via an environ...
BuildArch:      noarch
%description -n %{name}+regex-devel

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%package     -n %{name}+termcolor-devel
Summary:        A logging implementation for `log` which is configured via an environ...
BuildArch:      noarch
%description -n %{name}+termcolor-devel

This package contains library source intended for building other packages which
use the "termcolor" feature of the "%{crate}" crate.

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
%files -n rust-env_logger0.6-devel -f %{oreon_filedir}/rust-env_logger0.6-devel.list

%changelog

%autochangelog
