%global source0_hash 5c29b6ccce57bc3f7c4fb0510d330446b9c769e59c92bdfede27333808b6e646
%global lang ru
%global langrelease 1
%global aspellversion 6
%global debug_package %{nil}
Summary:        Russian dictionaries for Aspell
Name: aspell-%{lang}
Epoch: 50
Version: 0.99f7
Release:        1%{?dist}
License: ARL
URL: https://ftp.gnu.org/gnu/aspell/dict/0index.html#0.60
Source0:        https://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell%{aspellversion}-%{lang}-%{version}-%{langrelease}.tar.bz2
Source1: russian.alias
Provides:  deprecated()
Requires: aspell >= 12:0.60
# oreon:deps
BuildRequires:  aspell
BuildRequires:  make
# /oreon:deps
%description
Provides the word list/dictionaries for the following: Russian

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n aspell%{aspellversion}-%{lang}-%{version}-%{langrelease}

%build

./configure
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
%{__install} -p %{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/aspell-0.60/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
