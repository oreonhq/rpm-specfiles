%global source0_hash d486b048d1c3056d3a555744584a81873a63ecd4641f04e8b7bf9910b98d2985
%global lang la
%global langrelease 0
Summary:        Latin dictionaries for Aspell
Name: aspell-%{lang}
Version: 20020503
Release:        1%{?dist}
License: GPL-2.0-only
URL: http://aspell.net
Source0:        http://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell6-%{lang}-%{version}-%{langrelease}.tar.bz2
Requires: aspell >= 12:0.60
Provides:  deprecated()
%define debug_package %{nil}
# oreon:deps
BuildRequires:  aspell
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
