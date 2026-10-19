%global source0_hash 74570005dc2be5a244436fa2b46a5f612be84c6843f881f0cb1e4c775f658aaa
%define lang bg
%define langrelease 0
Summary:        Bulgarian dictionaries for Aspell
Name: aspell-%{lang}
Epoch: 50
Version: 4.1
Release:        1%{?dist}
License: GPL-2.0-only
URL: http://aspell.net/
Source0:        http://prdownloads.sourceforge.net/%{lang}office/aspell6-%{lang}-%{version}-%{langrelease}.tar.bz2
Provides:  deprecated()
Requires: aspell >= 12:0.60
%define debug_package %{nil}
# oreon:deps
BuildRequires:  aspell
BuildRequires:  make
# /oreon:deps
%description
Provides the word list/dictionaries for the following: Bulgarian

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n aspell6-%{lang}-%{version}-%{langrelease}

%build

./configure 
make %{?_smp_mflags}
iconv -f windows-1251 -t utf-8 <bg_phonet.dat >bg_phonet.dat.tmp
mv bg_phonet.dat.tmp bg_phonet.dat
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
