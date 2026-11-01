%global source0_hash 641cf30961525cbe3b340cc883436c8854e9f5032f459f444de4782b621e6572
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: lzip
Version: 1.26
Release: 1%{?dist}
Summary: LZMA lossless data compressor
License: GPL-2.0-or-later
URL: https://www.nongnu.org/lzip/lzip.html
Source0: https://download.savannah.gnu.org/releases/lzip/lzip-%{version}.tar.gz
Source1: lzip-%{version}.tar.gz.sig
Source2: lzip-key.asc

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: gcc-c++
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: patchelf
%endif

%description
Lzip is a lossless data compressor with a user interface similar to gzip or bzip2,
using the LZMA algorithm.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n lzip-%{version} -p1

%build
./configure --prefix=%{_prefix} --bindir=%{_bindir} --mandir=%{_mandir} --infodir=%{_infodir} CXXFLAGS="%{_oreon_cflags}" LDFLAGS="%{_oreon_ldflags}"
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f" 2>/dev/null || true)
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING
