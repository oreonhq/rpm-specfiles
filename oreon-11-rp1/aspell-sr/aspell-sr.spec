%global source0_hash 705e58fb390633c89c4cb224a1cfb34e67e09496448f7adc6500494b6e009289

%define lang sr
%define langrelease 0
Summary: Serbian dictionaries for Aspell
Name: aspell-%{lang}
Epoch: 50
Version: 0.02
Release: 38%{?dist}
License: LGPL-2.1-only
URL: http://aspell.net/
Source: ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell6-%{lang}-%{version}.tar.bz2
Patch0: aspell6-sr-0.02-time.patch

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
Provides the word list/dictionaries for the following: Serbian

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n aspell6-%{lang}-%{version}
%patch -P0 -p1 -b .time

%build
./configure
make

%install
rm -rf $RPM_BUILD_ROOT  
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc COPYING
%defattr(-,root,root,-)
%{_libdir}/aspell-0.60/*

%changelog
%autochangelog
