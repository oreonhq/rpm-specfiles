%global source0_hash 32824fab5e16e6c4d86dc1ba84489390419a39f97699852b66480bb87d297ed8
%bcond check 1
%global debug_package %{nil}
%global crate shellexpand
Name:           rust-shellexpand
Version:        3.1.2
Release:        1%{?dist}
Summary:        Shell-like expansions in strings
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/shellexpand
Source0:        https://static.crates.io/crates/shellexpand/shellexpand-%{version}.crate
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
Summary:        Shell-like expansions in strings
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+base-0-devel
Summary:        Shell-like expansions in strings
BuildArch:      noarch
%description -n %{name}+base-0-devel

This package contains library source intended for building other packages which
use the "base-0" feature of the "%{crate}" crate.

%package     -n %{name}+bstr-devel
Summary:        Shell-like expansions in strings
BuildArch:      noarch
%description -n %{name}+bstr-devel

This package contains library source intended for building other packages which
use the "bstr" feature of the "%{crate}" crate.

%package     -n %{name}+dirs-devel
Summary:        Shell-like expansions in strings
BuildArch:      noarch
%description -n %{name}+dirs-devel

This package contains library source intended for building other packages which
use the "dirs" feature of the "%{crate}" crate.

%package     -n %{name}+full-devel
Summary:        Shell-like expansions in strings
BuildArch:      noarch
%description -n %{name}+full-devel

This package contains library source intended for building other packages which
use the "full" feature of the "%{crate}" crate.

%package     -n %{name}+full-msrv-1-31-devel
Summary:        Shell-like expansions in strings
BuildArch:      noarch
%description -n %{name}+full-msrv-1-31-devel

This package contains library source intended for building other packages which
use the "full-msrv-1-31" feature of the "%{crate}" crate.

%package     -n %{name}+full-msrv-1-51-devel
Summary:        Shell-like expansions in strings
BuildArch:      noarch
%description -n %{name}+full-msrv-1-51-devel

This package contains library source intended for building other packages which
use the "full-msrv-1-51" feature of the "%{crate}" crate.

%package     -n %{name}+os_str_bytes-devel
Summary:        Shell-like expansions in strings
BuildArch:      noarch
%description -n %{name}+os_str_bytes-devel

This package contains library source intended for building other packages which
use the "os_str_bytes" feature of the "%{crate}" crate.

%package     -n %{name}+path-devel
Summary:        Shell-like expansions in strings
BuildArch:      noarch
%description -n %{name}+path-devel

This package contains library source intended for building other packages which
use the "path" feature of the "%{crate}" crate.

%package     -n %{name}+tilde-devel
Summary:        Shell-like expansions in strings
BuildArch:      noarch
%description -n %{name}+tilde-devel

This package contains library source intended for building other packages which
use the "tilde" feature of the "%{crate}" crate.

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
%files -n rust-shellexpand-devel -f %{oreon_filedir}/rust-shellexpand-devel.list

%changelog

%autochangelog
