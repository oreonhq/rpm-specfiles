%global source0_hash 77fc554aa9bbd5f4a87b58edf0d128838e92e4db6299904bb9360bf753a709f8

%define lang pt_BR
%define langrelease 0
Summary: Brazilian Portuguese dictionaries for Aspell
Name: aspell-%{lang}
Epoch: 50
Version: 20090702
Release: 33%{?dist}
License: LGPL-2.1-or-later
URL: http://aspell.net/
Source: ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell6-%{lang}-%{version}-%{langrelease}.tar.bz2

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
Obsoletes: aspell-pt <= 50:0.50

%define debug_package %{nil}

%description
Provides the word list/dictionaries for the following: Brazilian Portuguese

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n aspell6-%{lang}-%{version}-%{langrelease}

%build
./configure
make

%install
rm -rf $RPM_BUILD_ROOT 
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc COPYING Copyright
%{_libdir}/aspell-0.60/*

%changelog
%autochangelog
