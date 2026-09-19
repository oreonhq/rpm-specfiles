%global source0_hash 74570005dc2be5a244436fa2b46a5f612be84c6843f881f0cb1e4c775f658aaa

%define lang bg
%define langrelease 0
Summary: Bulgarian dictionaries for Aspell
Name: aspell-%{lang}
Epoch: 50
Version: 4.1
Release: 37%{?dist}
License: GPL-2.0-only
URL: http://aspell.net/
Source:   http://prdownloads.sourceforge.net/bgoffice/aspell6-%{lang}-%{version}-%{langrelease}.tar.bz2

# IMPORTANT
# This package has been deprecated since Fedora 39
# The reason behind this is that upstream has been inactive for more than 4 years
# and there are other variants like hunspell or enchant which has active upstream
# FESCo approval is located here: https://pagure.io/fesco/issue/3009
# Change proposal is located here: https://fedoraproject.org/wiki/Changes/AspellDeprecation
Provides:  deprecated()

Buildrequires: aspell >= 12:0.60
BuildRequires: make
Requires: aspell >= 12:0.60

%define debug_package %{nil}

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
%files
%doc COPYING Copyright
%{_libdir}/aspell-0.60/*

%changelog
%autochangelog
