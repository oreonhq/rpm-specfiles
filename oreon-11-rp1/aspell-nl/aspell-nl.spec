%global source0_hash 440e0b7df8c5903d728221fe4ba88a74658ce14c8bb04b290c41402dfd41cb39

%define lang nl
%define langrelease 2
Summary: Dutch dictionaries for Aspell
Name: aspell-%{lang}
# Have to bump this to make it newer than the old, bad version.
Epoch: 51
Version: 0.50
Release: 30%{?dist}
License: GPL-2.0-or-later
URL: http://aspell.net/
Source0: ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell-%{lang}-%{version}-%{langrelease}.tar.bz2

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
Provides the word list/dictionaries for the following: Dutch

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n aspell-%{lang}-%{version}-%{langrelease}

%build
./configure prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT libdir=%{_libdir}

%files
%doc Copyright README
%{_libdir}/aspell-0.60/*

%changelog
%autochangelog
