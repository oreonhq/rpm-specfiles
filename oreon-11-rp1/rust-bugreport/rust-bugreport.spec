%global source0_hash f280f65ce85b880919349bbfcb204930291251eedcb2e5f84ce2f51df969c162
%bcond check 1
%global debug_package %{nil}
%global crate bugreport
Name:           rust-bugreport
Version:        0.5.1
Release:        1%{?dist}
Summary:        Collect system and environment information for bug reports
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/bugreport
Source0:        https://static.crates.io/crates/bugreport/bugreport-%{version}.crate
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
Summary:        Collect system and environment information for bug reports
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+collector_operating_system-devel
Summary:        Collect system and environment information for bug reports
BuildArch:      noarch
%description -n %{name}+collector_operating_system-devel

This package contains library source intended for building other packages which
use the "collector_operating_system" feature of the "%{crate}" crate.

%package     -n %{name}+format_markdown-devel
Summary:        Collect system and environment information for bug reports
BuildArch:      noarch
%description -n %{name}+format_markdown-devel

This package contains library source intended for building other packages which
use the "format_markdown" feature of the "%{crate}" crate.

%package     -n %{name}+format_plaintext-devel
Summary:        Collect system and environment information for bug reports
BuildArch:      noarch
%description -n %{name}+format_plaintext-devel

This package contains library source intended for building other packages which
use the "format_plaintext" feature of the "%{crate}" crate.

%package     -n %{name}+git-version-devel
Summary:        Collect system and environment information for bug reports
BuildArch:      noarch
%description -n %{name}+git-version-devel

This package contains library source intended for building other packages which
use the "git-version" feature of the "%{crate}" crate.

%package     -n %{name}+git_hash-devel
Summary:        Collect system and environment information for bug reports
BuildArch:      noarch
%description -n %{name}+git_hash-devel

This package contains library source intended for building other packages which
use the "git_hash" feature of the "%{crate}" crate.

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
%files -n rust-bugreport-devel -f %{oreon_filedir}/rust-bugreport-devel.list

%changelog

%autochangelog
