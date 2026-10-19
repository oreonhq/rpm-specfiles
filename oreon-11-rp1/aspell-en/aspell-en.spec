%global source0_hash 77a5cb437c45d1115f3b593802c20651d8c93803ed1073278dc1a1240016f10d
%define lang en
%define langrelease 0
%define aspellversion 6
Summary:        English dictionaries for Aspell
Name: aspell-%{lang}
Epoch: 50
Version: 2026.02.25
Release:        1%{?dist}
License: LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL: http://aspell.net/
Source0:        https://mirrors.kernel.org/gnu/aspell/dict/%{lang}/aspell%{aspellversion}-%{lang}-%{version}-%{langrelease}.tar.bz2
Provides:  deprecated()
Requires: aspell >= 12:0.60
Obsoletes: aspell-en-gb <= 0.33.7.1
Obsoletes: aspell-en-ca <= 0.33.7.1
Supplements: (aspell and langpacks-en)
Supplements: (aspell and langpacks-en_GB)
%define debug_package %{nil}
# oreon:deps
BuildRequires:  aspell
BuildRequires:  make
# /oreon:deps
%description
Provides the word list/dictionaries for the following: English, Canadian
English, British English

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
