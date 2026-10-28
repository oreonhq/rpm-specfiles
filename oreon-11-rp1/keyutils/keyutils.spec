%global source0_hash b431f6e3c1a29fa9394143885edb7b013510f103f0870f45be4b8a7aade91961
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: keyutils
Version: 1.6.3
Release: 2%{?dist}
Provides: keyutils-libs = %{version}-%{release}
Provides: keyutils-libs%{_isa} = %{version}-%{release}
Obsoletes: keyutils-libs < 1.6.4
Summary: Linux key management library
License: GPL-2.0-or-later AND LGPL-2.1-or-later
URL: https://git.kernel.org/pub/scm/linux/kernel/git/dhowells/keyutils.git
Source0: https://git.kernel.org/pub/scm/linux/kernel/git/dhowells/keyutils.git/snapshot/v%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
%endif

%description
keyutils is the Linux key management library.

%package devel
Summary: Linux key management library
Requires: keyutils%{?_isa} = %{version}-%{release}

%description devel
keyutils is the Linux key management library.

%prep
%oreon_sha256
%autosetup -n v%{version} -p1

%build
make %{?_smp_mflags} NO_ARLIB=1 LIBDIR=%{_libdir} USRLIBDIR=%{_libdir} CFLAGS="%{_oreon_cflags} -fPIC"

%install
make install DESTDIR=%{buildroot} NO_ARLIB=1 LIBDIR=%{_libdir} USRLIBDIR=%{_libdir}
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license LICENCE.LGPL

%files devel -f %{_builddir}/%{name}-devel.files
