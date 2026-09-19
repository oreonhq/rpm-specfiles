%global source0_hash 3035bd29dad929ce66e6acdc7c29670df458e0d13fe178241b212f481111e3d6

%define lang is
%define langrelease 0
%define aspellrelease 0.60
Summary: Icelandic dictionaries for Aspell
Name: aspell-%{lang}
Epoch: 50
Version: 0.51.1
Release: 39%{?dist}
License: GPL-2.0-or-later
URL: http://aspell.net/
Source: ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell-%{lang}-%{version}-%{langrelease}.tar.bz2

# IMPORTANT
# This package has been deprecated since Fedora 39
# The reason behind this is that upstream has been inactive for more than 4 years
# and there are other variants like hunspell or enchant which has active upstream
# FESCo approval is located here: https://pagure.io/fesco/issue/3009
# Change proposal is located here: https://fedoraproject.org/wiki/Changes/AspellDeprecation
Provides:  deprecated()

Buildrequires: aspell >= 12:%{aspellrelease}
BuildRequires: make
Requires: aspell >= 12:%{aspellrelease}

%define debug_package %{nil}

%description
Provides the word list/dictionaries for the following: Icelandic

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n aspell-%{lang}-%{version}-%{langrelease}
iconv -f windows-1252 -t utf8 Copyright >Copyright.aux
mv Copyright.aux Copyright

%build
./configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/%{_libdir}/aspell-%{aspellrelease}/*slenska.alias $RPM_BUILD_ROOT/%{_libdir}/aspell-%{aspellrelease}/íslenska.alias

%files
%doc COPYING Copyright
%{_libdir}/aspell-%{aspellrelease}/*

%changelog
%autochangelog
