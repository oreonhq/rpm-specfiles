%global source0_hash fd87e0aba7e43ae054837afd6cd4db03a3f2693deb3619085e6ed9d8d9604ad8
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: gperf
Version: 3.3
Release: 1%{?dist}
Summary: Perfect hash function generator
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/gperf/
Source0: https://ftp.gnu.org/gnu/gperf/gperf-%{version}.tar.gz
Source1: gperf-%{version}.tar.gz.sig
Source2: gperf-key.asc

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: make
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: patchelf
%endif

%description
gperf generates perfect hash functions for a set of keywords, as C or
C++ source.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n gperf-%{version} -p1

%build
%oreon_configure
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
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING
