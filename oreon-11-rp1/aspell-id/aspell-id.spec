%global source0_hash 523912082848d891746dbb233f2ddb2cdbab6750dc76c38b3f6e000c9eb37308
%define lang id
%define langrelease 0
%define aspellversion 5
Summary:        Indonesian dictionaries for Aspell
Name: aspell-%{lang}
Epoch: 50
Version: 1.2
Release:        1%{?dist}
License: GPL-2.0-only
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
Provides the word list/dictionaries for the following: Indonesian

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n aspell%{aspellversion}-%{lang}-%{version}-%{langrelease}

%build

./configure
make
%install
rm -rf $RPM_BUILD_ROOT
make install  DESTDIR=$RPM_BUILD_ROOT
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
