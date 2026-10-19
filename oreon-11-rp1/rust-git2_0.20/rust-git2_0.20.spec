%global source0_hash 7b88256088d75a56f8ecfa070513a775dd9107f6530ef14919dac831af9cfe2b
%bcond check 1
%global debug_package %{nil}
%global crate git2
Name:           rust-git2_0.20
Version:        0.20.4
Release:        1%{?dist}
Summary:        Bindings to libgit2 for interoperating with git repositories
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/git2
Source0:        https://static.crates.io/crates/git2/git2-%{version}.crate
Patch:          0001-Adapt-tests-for-relativeworktrees-extension-added-in.patch
%if %{with check}
%endif
# oreon:deps
BuildRequires:  /usr/bin/git
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
Summary:        Bindings to libgit2 for interoperating with git repositories
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+https-devel
Summary:        Bindings to libgit2 for interoperating with git repositories
BuildArch:      noarch
%description -n %{name}+https-devel

This package contains library source intended for building other packages which
use the "https" feature of the "%{crate}" crate.

%package     -n %{name}+openssl-probe-devel
Summary:        Bindings to libgit2 for interoperating with git repositories
BuildArch:      noarch
%description -n %{name}+openssl-probe-devel

This package contains library source intended for building other packages which
use the "openssl-probe" feature of the "%{crate}" crate.

%package     -n %{name}+openssl-sys-devel
Summary:        Bindings to libgit2 for interoperating with git repositories
BuildArch:      noarch
%description -n %{name}+openssl-sys-devel

This package contains library source intended for building other packages which
use the "openssl-sys" feature of the "%{crate}" crate.

%package     -n %{name}+ssh-devel
Summary:        Bindings to libgit2 for interoperating with git repositories
BuildArch:      noarch
%description -n %{name}+ssh-devel

This package contains library source intended for building other packages which
use the "ssh" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Bindings to libgit2 for interoperating with git repositories
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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
%files -n rust-git2_0.20-devel -f %{oreon_filedir}/rust-git2_0.20-devel.list

%changelog

%autochangelog
