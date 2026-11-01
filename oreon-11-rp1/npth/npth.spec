%global source0_hash 8bd24b4f23a3065d6e5b26e98aba9ce783ea4fd781069c1b35d149694e90ca3e
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: npth
Version: 1.8
Release: 1%{?dist}
Summary: New portable threads library
License: LGPL-2.1-or-later
URL: https://gnupg.org/software/npth/
Source0: https://gnupg.org/ftp/gcrypt/npth/npth-%{version}.tar.bz2
Source1: npth-%{version}.tar.bz2.sig
Source2: gnupg-signing-keys.asc

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gnupg2
%endif

%description
nPth is a non-preemptive thread library used by GnuPG.

%package devel
Summary: Development files for npth
Requires: npth%{?_isa} = %{version}-%{release}

%description devel
Headers, libraries and pkg-config files for building against npth.

%prep
%oreon_sha256
%if %{without bootstrap} && !0%{?bootstrap}
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%endif
%autosetup -n npth-%{version} -p1

%build
%oreon_configure --disable-static
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
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
%license COPYING.LIB

%files devel -f %{_builddir}/%{name}-devel.files
