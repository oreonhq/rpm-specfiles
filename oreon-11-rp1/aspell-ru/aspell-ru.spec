%global source0_hash 5c29b6ccce57bc3f7c4fb0510d330446b9c769e59c92bdfede27333808b6e646

%global lang ru
%global langrelease 1
%global aspellversion 6
%global debug_package %{nil}

Summary: Russian dictionaries for Aspell
Name: aspell-%{lang}
Epoch: 50
Version: 0.99f7
Release: 38%{?dist}
License: ARL
URL: ftp://ftp.gnu.org/gnu/aspell/dict/0index.html#0.60
Source0: ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell%{aspellversion}-%{lang}-%{version}-%{langrelease}.tar.bz2
Source1: russian.alias

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

%files
%doc Copyright
%{_libdir}/aspell-0.60/*

%changelog
%autochangelog
