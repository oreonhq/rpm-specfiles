%global source0_hash c7eebd7149b15e4d74d2dff9acd3137dc13eedf604adf1df2efa52d9f36fe0bb

# This library just contains the guest payload to be injected by libkrun into
# the VM's memory, so no useful debug info can be generated from it.
%global debug_package %{nil}

%global kernel linux-6.12.68

Name:           libkrunfw
Version:        5.2.1
Release:        1%{?dist}
Summary:        A dynamic library bundling the guest payload consumed by libkrun
License:        LGPL-2.1-only AND GPL-2.0-only
URL:            https://github.com/containers/libkrunfw
Source0:        https://github.com/containers/libkrunfw/archive/refs/tags/v%{version}.tar.gz
# This package bundles a customized Linux kernel in a format that can only be
# consumed by libkrun, which will run it in an isolated context using KVM
# Virtualization. This kernel can't be used for booting a physical machine
# and, by being bundled in a dynamic library, it can not be mistaken as a
# regular kernel.
#
# The convenience of distributing a kernel this way and for this purpose was
# discussed here:
# https://lists.fedorahosted.org/archives/list/kernel@lists.fedoraproject.org/thread/2TMXPCE2VWF7USZA7OHQ3P2SBJAEGCSX/
Source1:        https://www.kernel.org/pub/linux/kernel/v6.x/%{kernel}.tar.xz

# libkrunfw only provides configs for x86_64 and aarch64 as libkrun (the only
# consumer of this library) only supports those architectures.
ExclusiveArch:  x86_64 aarch64 riscv64

# libkrunfw + packaging requirements
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  python3-pyelftools
BuildRequires:  openssl-devel

# kernel build requirements
BuildRequires:  bc
BuildRequires:  bison
BuildRequires:  elfutils-devel
BuildRequires:  flex
%ifarch aarch64 riscv64
BuildRequires:  perl-interpreter
%endif

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
%endif

%files
%{_libdir}/libkrunfw.so.5
%{_libdir}/libkrunfw.so.%{version}

%files devel
%{_libdir}/libkrunfw.so

%ifarch x86_64
%files sev
%{_libdir}/libkrunfw-sev.so.5
%{_libdir}/libkrunfw-sev.so.%{version}
%{_bindir}/krunfw_measurement

%files sev-devel
%{_libdir}/libkrunfw-sev.so
%endif

%changelog
%autochangelog
