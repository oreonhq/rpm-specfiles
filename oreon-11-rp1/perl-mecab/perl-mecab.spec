%global source0_hash 71fe5559c5bd2a13ea9929190a8f9f5ee4c63987108081bd7332ca1bbbb616c9
%define		mainver		0.996
%define		baserelease	10
%define		srcname		mecab-perl
Name:		perl-mecab
Version:	%{mainver}
Release:        10%{?dist}
Summary:        Perl binding for MeCab
License:	BSD-3-Clause OR LGPL-2.1-or-later OR GPL-2.0-or-later
URL:		http://mecab.sourceforge.net/
Source0:        http://mecab.googlecode.com/files/%{srcname}-%{version}.tar.gz
Requires:	mecab = %{version}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  mecab-devel
BuildRequires:  mecab-jumandic
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}-%{mainver}%{?betaver}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="${RPM_OPT_FLAGS}"
sed -i.rpath \
	-e 's|LD_RUN_PATH=[^ ][^ ]*||' Makefile
%{__make} %{?_smp_mflags}
%install
%{__make} pure_install \
	PERL_INSTALL_ROOT=$RPM_BUILD_ROOT \
	INSTALL="%{__install} -c -p"
find $RPM_BUILD_ROOT -type f -name .packlist | xargs %{__rm} -f
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 | xargs %{__rm} -f
find $RPM_BUILD_ROOT -depth -type d | xargs rmdir 2>/dev/null || :
%{__chmod} -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{__perl} test.pl
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
