%global source0_hash f9c1efd5bebbe37fc6e1063db7473ce8df1e3e0be4ff0f43ce04fce57e9c5dd9
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: groff
Version: 1.24.2
Release: 1%{?dist}
Summary: Document formatting system
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/groff/
Source0: https://ftp.gnu.org/gnu/groff/groff-%{version}.tar.gz
Source1: groff-%{version}.tar.gz.sig
Source2: groff-key.asc
Provides: groff-base = %{version}-%{release}
Requires: perl

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: gcc-c++
BuildRequires: perl
BuildRequires: texinfo
BuildRequires: bison
%endif

%description
Groff is a typesetting system that reads plain text mixed with formatting
commands and produces formatted output, including man pages.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n groff-%{version} -p1

%build
%oreon_configure --without-x --with-doc=no --without-gs --without-uchardet
%oreon_make

%install
%oreon_make_install
rm -rf %{buildroot}%{_docdir}/groff-%{version}
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
