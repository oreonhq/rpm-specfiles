%global source0_hash e093ef184d7f9a1b9797e2465296f55510adb6dab8842b0c3ed53329663096dc
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: perl
Version: 5.42.0
Release: 1%{?dist}
Summary: Perl interpreter
License: GPL-1.0-or-later OR Artistic-1.0-Perl
URL: https://www.perl.org/
Source0: https://www.cpan.org/src/5.0/perl-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
%endif

%description
Perl interpreter and modules.

%prep
%oreon_sha256
%autosetup -p1

%build
./Configure -des \
  -Dprefix=%{_prefix} \
  -Dvendorprefix=%{_prefix} \
  -Duseshrplib \
  -Dusethreads \
  -Dinc_version_list=none \
  -Dccflags="%{_oreon_cflags} -fPIC" \
  -Dldflags="%{_oreon_ldflags}" \
  -Dlddlflags="-shared %{_oreon_ldflags}"
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license Artistic Copying
