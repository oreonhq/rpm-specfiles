%global source0_hash 440e0b7df8c5903d728221fe4ba88a74658ce14c8bb04b290c41402dfd41cb39
%define lang nl
%define langrelease 2
Summary:        Dutch dictionaries for Aspell
Name: aspell-%{lang}
Epoch: 51
Version: 0.50
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: http://aspell.net/
Source0:        https://ftp.gnu.org/gnu/aspell/dict/%{lang}/%{name}-%{version}-%{langrelease}.tar.bz%{langrelease}
Provides:  deprecated()
Requires: aspell >= 12:0.60
%define debug_package %{nil} 
# oreon:deps
BuildRequires:  aspell
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
