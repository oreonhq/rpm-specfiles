%global source0_hash f8d7f07b4511e606eb56392ddaa76fd29918006331795e5942ad11b510d0a51d
%global lang fi
%global langrelease 0
Summary:        Finnish dictionaries for Aspell
Name: aspell-%{lang}
Version: 0.7
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
Provides the word list/dictionaries for the following: Finnish

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
