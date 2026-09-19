%global source0_hash d486b048d1c3056d3a555744584a81873a63ecd4641f04e8b7bf9910b98d2985

%global lang la
%global langrelease 0

Summary: Latin dictionaries for Aspell
Name: aspell-%{lang}
Version: 20020503
Release: 29%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: http://aspell.net
Source: http://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell6-%{lang}-%{version}-%{langrelease}.tar.bz2
Buildrequires: aspell >= 12:0.60
BuildRequires: make
Requires: aspell >= 12:0.60
# IMPORTANT
# This package has been deprecated since Fedora 39
# The reason behind this is that upstream has been inactive for more than 4 years
# and there are other variants like hunspell or enchant which has active upstream
# FESCo approval is located here: https://pagure.io/fesco/issue/3009
# Change proposal is located here: https://fedoraproject.org/wiki/Changes/AspellDeprecation
Provides:  deprecated()

%define debug_package %{nil}

%description
Provides the word list/dictionaries for the following: Latin

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n aspell6-%{lang}-%{version}-%{langrelease}

%build
./configure 
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc COPYING Copyright
%{_libdir}/aspell-0.60/*

%changelog
%autochangelog
