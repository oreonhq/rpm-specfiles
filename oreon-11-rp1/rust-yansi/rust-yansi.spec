%global source0_hash cfe53a6657fd280eaa890a3bc59152892ffa3e30101319d168b781ed6529b049
%bcond_without check
%global debug_package %{nil}
%global crate yansi
Name:           rust-yansi
Version:        1.0.1
Release:        1%{?dist}
Summary:        Dead simple ANSI terminal color painting library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/yansi
Source0:        https://static.crates.io/crates/yansi/yansi-%{version}.crate
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
Summary:        Dead simple ANSI terminal color painting library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Dead simple ANSI terminal color painting library
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+detect-env-devel
Summary:        Dead simple ANSI terminal color painting library
BuildArch:      noarch
%description -n %{name}+detect-env-devel

This package contains library source intended for building other packages which
use the "detect-env" feature of the "%{crate}" crate.

%package     -n %{name}+detect-tty-devel
Summary:        Dead simple ANSI terminal color painting library
BuildArch:      noarch
%description -n %{name}+detect-tty-devel

This package contains library source intended for building other packages which
use the "detect-tty" feature of the "%{crate}" crate.

%package     -n %{name}+hyperlink-devel
Summary:        Dead simple ANSI terminal color painting library
BuildArch:      noarch
%description -n %{name}+hyperlink-devel

This package contains library source intended for building other packages which
use the "hyperlink" feature of the "%{crate}" crate.

%package     -n %{name}+is-terminal-devel
Summary:        Dead simple ANSI terminal color painting library
BuildArch:      noarch
%description -n %{name}+is-terminal-devel

This package contains library source intended for building other packages which
use the "is-terminal" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Dead simple ANSI terminal color painting library
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-yansi-devel -f %{oreon_filedir}/rust-yansi-devel.list

%changelog

%autochangelog
