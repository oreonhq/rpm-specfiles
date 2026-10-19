%global source0_hash 2285ddfe3054097ef4b2fe909ef8c3bcd1ea52a8f0d274416caebeef39f04a65
%bcond check 0
%global debug_package %{nil}
%global crate io-extras
Name:           rust-io-extras
Version:        0.18.4
Release:        1%{?dist}
Summary:        File/socket handle/descriptor utilities
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://crates.io/crates/io-extras
Source0:        https://static.crates.io/crates/io-extras/io-extras-%{version}.crate
Patch:          io-extras-fix-metadata-auto.diff
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
Summary:        File/socket handle/descriptor utilities
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-std-devel
Summary:        File/socket handle/descriptor utilities
BuildArch:      noarch
%description -n %{name}+async-std-devel

This package contains library source intended for building other packages which
use the "async-std" feature of the "%{crate}" crate.

%package     -n %{name}+mio-devel
Summary:        File/socket handle/descriptor utilities
BuildArch:      noarch
%description -n %{name}+mio-devel

This package contains library source intended for building other packages which
use the "mio" feature of the "%{crate}" crate.

%package     -n %{name}+os_pipe-devel
Summary:        File/socket handle/descriptor utilities
BuildArch:      noarch
%description -n %{name}+os_pipe-devel

This package contains library source intended for building other packages which
use the "os_pipe" feature of the "%{crate}" crate.

%package     -n %{name}+socket2-devel
Summary:        File/socket handle/descriptor utilities
BuildArch:      noarch
%description -n %{name}+socket2-devel

This package contains library source intended for building other packages which
use the "socket2" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        File/socket handle/descriptor utilities
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+use_async_std-devel
Summary:        File/socket handle/descriptor utilities
BuildArch:      noarch
%description -n %{name}+use_async_std-devel

This package contains library source intended for building other packages which
use the "use_async_std" feature of the "%{crate}" crate.

%package     -n %{name}+use_mio_net-devel
Summary:        File/socket handle/descriptor utilities
BuildArch:      noarch
%description -n %{name}+use_mio_net-devel

This package contains library source intended for building other packages which
use the "use_mio_net" feature of the "%{crate}" crate.

%package     -n %{name}+use_mio_os_ext-devel
Summary:        File/socket handle/descriptor utilities
BuildArch:      noarch
%description -n %{name}+use_mio_os_ext-devel

This package contains library source intended for building other packages which
use the "use_mio_os_ext" feature of the "%{crate}" crate.

%package     -n %{name}+use_os_pipe-devel
Summary:        File/socket handle/descriptor utilities
BuildArch:      noarch
%description -n %{name}+use_os_pipe-devel

This package contains library source intended for building other packages which
use the "use_os_pipe" feature of the "%{crate}" crate.

%package     -n %{name}+use_socket2-devel
Summary:        File/socket handle/descriptor utilities
BuildArch:      noarch
%description -n %{name}+use_socket2-devel

This package contains library source intended for building other packages which
use the "use_socket2" feature of the "%{crate}" crate.

%package     -n %{name}+use_tokio-devel
Summary:        File/socket handle/descriptor utilities
BuildArch:      noarch
%description -n %{name}+use_tokio-devel

This package contains library source intended for building other packages which
use the "use_tokio" feature of the "%{crate}" crate.

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
%files -n rust-io-extras-devel -f %{oreon_filedir}/rust-io-extras-devel.list

%changelog

%autochangelog
