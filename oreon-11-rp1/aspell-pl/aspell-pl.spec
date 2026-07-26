%global source0_hash 017741fcb70a885d718c534160c9de06b03cc72f352879bd106be165e024574d

%define lang pl
%define langrelease 0
%define aspellversion 6
Summary: Polish dictionaries for Aspell
Name: aspell-%{lang}
Epoch: 50
Version: 6.0_20061121
Release: 37%{?dist}
# List of all licences each with file containing the licence text, the list can be also found in the Copyright file
# CC-SA-1.0             /doc/CC-SA-1.0
# LGPL-2.0-or-later     /doc/GPL
# LGPL-2.1-or-later     /doc/LGPL
# MPL-1.1               /doc/MPL-1.1.txt
License: CC-SA-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND MPL-1.1
URL: http://aspell.net/
Source: ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell%{aspellversion}-%{lang}-%{version}-%{langrelease}.tar.bz2

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
Provides the word list/dictionaries for the following: Polish

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n aspell%{aspellversion}-%{lang}-%{version}-%{langrelease}

%build
./configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc Copyright
%{_libdir}/aspell-0.60/*

%changelog
%autochangelog
