%global source1_hash d367c7504bd4da520dd01eb08125d2d0ac088bc8af4cd56d236f2074dd4225b7
%global source0_hash c7eebd7149b15e4d74d2dff9acd3137dc13eedf604adf1df2efa52d9f36fe0bb
%global debug_package %{nil}
%global kernel linux-6.12.68
Name:           libkrunfw
Version:        5.2.1
Release:        1%{?dist}
Summary:        A dynamic library bundling the guest payload consumed by libkrun
License:        LGPL-2.1-only AND GPL-2.0-only
URL:            https://github.com/containers/libkrunfw
Source0:        https://github.com/containers/libkrunfw/archive/refs/tags/v%{version}.tar.gz
Source1:        https://www.kernel.org/pub/linux/kernel/v6.x/%{kernel}.tar.xz
ExclusiveArch:  x86_64 aarch64 riscv64
%ifarch aarch64 riscv64
%endif
# oreon:deps
BuildRequires:  bc
BuildRequires:  bison
BuildRequires:  elfutils-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  python3-pyelftools
# /oreon:deps
%description
%{summary}

%package devel
Summary: Header files and libraries for libkrunfw development
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The libkrunfw-devel package contains the libraries needed to develop
programs that consume the guest payload integrated in libkrunfw.

# SEV is a feature provided by AMD EPYC processors, so only it's only
# available on x86_64.
%ifarch x86_64
%package sev
Summary: A dynamic library bundling the guest payload consumed by libkrun-sev
%description sev
The libkrunfw-sev package contains the library bundling the guest
payload consumed by libkrun-sev.

%package sev-devel
Summary: Header files and libraries for libkrunfw-sev development
Requires: %{name}-sev%{?_isa} = %{version}-%{release}
%description sev-devel
The libkrunfw-sev-devel package contains the libraries needed to develop
programs that consume the guest payload integrated in libkrunfw-sev.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git
mkdir tarballs
cp %{SOURCE1} tarballs/

%build

%{make_build}
%ifarch x86_64
    rm -fr %{kernel}
    rm kernel.c
    %{make_build} SEV=1
    pushd utils
    make
    popd
%endif
%install
%{make_install} PREFIX=%{_prefix}
%ifarch x86_64
    %{make_install} SEV=1 PREFIX=%{_prefix}
    install -D -p -m 0755 utils/krunfw_measurement %{buildroot}%{_bindir}/krunfw_measurement
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n libkrunfw-devel -f %{oreon_filedir}/libkrunfw-devel.list

%changelog

%autochangelog
