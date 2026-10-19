%global source0_hash ad367fa1e7069c72eb7ae37e4d39c30a44d32a6aa73cedccbd0d06a69018afcc
%define lang es
%define langrelease 2
Summary:        Spanish dictionaries for Aspell
Name: aspell-%{lang}
Epoch: 50
Version: 1.11
Release:        1%{?dist}
License: GPL-2.0-only
URL: http://aspell.net/
Source0:        https://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell6-%{lang}-%{version}-%{langrelease}.tar.bz%{langrelease}
Provides:  deprecated()
Requires: aspell >= 12:0.60
%define debug_package %{nil}
# oreon:deps
BuildRequires:  aspell
BuildRequires:  make
# /oreon:deps
%description
Provides the word list/dictionaries for the following: Spanish

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n aspell6-%{lang}-%{version}-%{langrelease}
iconv -f windows-1252 -t utf-8 Copyright > Copyright.aux
mv Copyright.aux Copyright

%build

./configure
make
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
