%global source0_hash e316a08a75da8a0d4d15eb892023073a971e0a326382a5532db29856768e0929
%define lang gd
%define langrelease 1
%define aspellversion 5
Summary:        Gaelic dictionaries for Aspell
Name: aspell-%{lang}
Epoch: 51
Version: 0.1.1
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: http://aspell.net/
Source0:        https://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell%{aspellversion}-%{lang}-%{version}-%{langrelease}.tar.bz2
Provides:  deprecated()
Requires: aspell >= 12:0.60
%define debug_package %{nil}
# oreon:deps
BuildRequires:  aspell
BuildRequires:  make
# /oreon:deps
%description
Provides the word list/dictionaries for the following: Gaelic, Scots Gaelic

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n aspell%{aspellversion}-%{lang}-%{version}-%{langrelease}

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
