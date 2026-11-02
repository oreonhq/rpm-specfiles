%global source0_hash bf149d01a2b9fcc0e4589b8ae8697d3d5c557ea48ed95a3fa55dd3b1187e6039
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: gnupg2
Version: 2.5.24
Release: 2%{?dist}
Summary: OpenPGP and S/MIME encryption and signing tool
License: GPL-3.0-or-later
URL: https://gnupg.org/
Source0: https://gnupg.org/ftp/gcrypt/gnupg/gnupg-%{version}.tar.bz2
Source1: gnupg-%{version}.tar.bz2.sig
Source2: gnupg-signing-keys.asc

Provides: gnupg = %{version}-%{release}
Provides: gpg = %{version}-%{release}

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: libgpg-error-devel
BuildRequires: libgcrypt-devel
BuildRequires: libassuan-devel >= 3.0.0
BuildRequires: libksba-devel
BuildRequires: npth-devel
BuildRequires: zlib-devel
BuildRequires: bzip2-devel
BuildRequires: readline-devel
BuildRequires: sqlite-devel
BuildRequires: gnutls-devel
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gnupg2
%endif

%description
GnuPG is a complete implementation of the OpenPGP standard. It encrypts
and signs data and manages keys for rpm, dnf and the build tooling.

%prep
%oreon_sha256
%if %{without bootstrap} && !0%{?bootstrap}
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%endif
%autosetup -n gnupg-%{version} -p1

%build
%oreon_configure --disable-doc --disable-ldap --disable-ntbtls --disable-rpath
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
ln -sf gpg %{buildroot}%{_bindir}/gpg2
ln -sf gpgv %{buildroot}%{_bindir}/gpgv2
rm -rf %{buildroot}%{_datadir}/doc/gnupg
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
