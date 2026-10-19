%global source0_hash ebdae47edf87357a4df137dd754737e6417452540cb1ed34b545ccfd66f165b9
%define lang ca
%define langrelease 1
Summary:        Catalan dictionaries for Aspell
Name: aspell-%{lang}
Epoch: 51
Version: 2.1.5
Release:        1%{?dist}
License: GPL-2.0-only
URL: http://aspell.net/
Source0:        https://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell6-%{lang}-%{version}-%{langrelease}.tar.bz2
Provides:  deprecated()
Requires: aspell >= 12:0.60
%define debug_package %{nil}
# oreon:deps
BuildRequires:  aspell
BuildRequires:  make
# /oreon:deps
%description
Provides the word list/dictionaries for the following: Catalan

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n aspell6-%{lang}-%{version}-%{langrelease}
iconv -f windows-1252 -t utf-8 Copyright > Copyright.aux
mv Copyright.aux Copyright

%build

./configure 
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR="$RPM_BUILD_ROOT"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
