%global source0_hash e76160286bbfb0821602c6c0c3220ebcf366ad3246d3b9d0a0fbefcd35e86043
%global source1_hash f8139467f07a089c8d8eeaf6d69bd7e19380820cd8277c747d5cc6f87e96810d
%global source2_hash caf7cb1981e2f5fa5952c2f3a11f9247221d16df4d9111ce15164a64675fc452
%define libsepolver 3.11-1
%define libselinuxver 3.11-1
Summary:        SELinux binary policy manipulation library
Name: libsemanage
Version: 3.11
Release:        1%{?dist}
License: LGPL-2.1-or-later
Source0:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/libsemanage-%{version}.tar.gz
Source1: https://github.com/SELinuxProject/selinux/releases/download/%{version}/libsemanage-%{version}.tar.gz.asc
Source2: https://github.com/bachradsusi.gpg
Patch0001: 0001-libsemanage-optionally-sort-file_contexts.local-by-s.patch
Patch0002: 0002-libsemanage-genhomedircon-reject-users-with-a-relati.patch
URL: https://github.com/SELinuxProject/selinux/wiki
VCS: git:https://github.com/SELinuxProject/selinux.git
Source3: semanage.conf
Requires: bzip2-libs audit-libs
Requires: libselinux%{?_isa} >= %{libselinuxver}
Obsoletes: libsemanage-compat = 3.1-4
# oreon:deps
BuildRequires:  audit-libs-devel
BuildRequires:  bison
BuildRequires:  bzip2-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libselinux-devel
BuildRequires:  libsepol-devel
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  swig
# /oreon:deps
%description
Security-enhanced Linux is a feature of the Linux® kernel and a number
of utilities with enhanced security functionality designed to add
mandatory access controls to Linux.  The Security-enhanced Linux
kernel contains new architectural components originally developed to
improve the security of the Flask operating system. These
architectural components provide general support for the enforcement
of many kinds of mandatory access control policies, including those
based on the concepts of Type Enforcement®, Role-based Access
Control, and Multi-level Security.

libsemanage provides an API for the manipulation of SELinux binary policies.
It is used by checkpolicy (the policy compiler) and similar tools, as well
as by programs like load_policy that need to perform specific transformations
on binary policies such as customizing policy boolean settings.

%package static
Summary: Static library used to build policy manipulation tools
Requires: libsemanage-devel%{_isa} = %{version}-%{release}
%description static
The semanage-static package contains the static libraries 
needed for developing applications that manipulate binary policies. 

%package devel
Summary: Header files and libraries used to build policy manipulation tools
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The semanage-devel package contains the libraries and header files
needed for developing applications that manipulate binary policies. 

%package -n python3-libsemanage
Summary: semanage python 3 bindings for libsemanage
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libselinux-python3
%{?python_provide:%python_provide python3-libsemanage}
Provides: %{name}-python3 = %{version}-%{release}
Provides: %{name}-python3%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-python3 < %{version}-%{release}
%description -n python3-libsemanage
The libsemanage-python3 package contains the python 3 bindings for developing
SELinux management applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p 2 -n libsemanage-%{version}

%build

%set_build_flags
CFLAGS="$CFLAGS -fno-semantic-interposition"
BuildPythonWrapper() {
  BinaryName=$1
  make \
    PYTHON=$BinaryName \
    LIBDIR="%{_libdir}" SHLIBDIR="%{_lib}" \
    pywrap
}
make clean
make swigify
%make_build LIBDIR="%{_libdir}" SHLIBDIR="%{_lib}" all
BuildPythonWrapper \
  %{__python3}
%install
InstallPythonWrapper() {
  BinaryName=$1
  make \
    PYTHON=$BinaryName \
    DESTDIR="${RPM_BUILD_ROOT}" LIBDIR="%{_libdir}" SHLIBDIR="%{_libdir}" \
    install-pywrap
}
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}
mkdir -p ${RPM_BUILD_ROOT}%{_includedir} 
mkdir -p ${RPM_BUILD_ROOT}%{_sharedstatedir}/selinux
mkdir -p ${RPM_BUILD_ROOT}%{_sharedstatedir}/selinux/tmp
%make_install LIBDIR="%{_libdir}" SHLIBDIR="%{_libdir}"
InstallPythonWrapper \
  %{__python3} \
  $(python3-config --extension-suffix)
cp %{SOURCE3} ${RPM_BUILD_ROOT}%{_sysconfdir}/selinux/semanage.conf
%oreon_autofiles python3-libsemanage usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libsemanage-static -f %{oreon_filedir}/libsemanage-static.list
%files -n libsemanage-devel -f %{oreon_filedir}/libsemanage-devel.list
%files -n python3-libsemanage -f %{oreon_filedir}/python3-libsemanage.list

%changelog

%autochangelog
