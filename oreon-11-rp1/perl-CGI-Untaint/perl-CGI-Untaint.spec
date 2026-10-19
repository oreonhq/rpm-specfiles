%global source0_hash 08e12a7ec938bc81899c02a6426777b9fe0e75da1161516416999d3052bc63b9
Name:           perl-CGI-Untaint
Version:        1.26
Release:        1%{?dist}
Summary:        Process CGI input parameters
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-Untaint
Source0:        https://cpan.metacpan.org/authors/id/T/TM/TMTM/CGI-Untaint-%{version}.tar.gz
BuildArch:      noarch
Requires:  perl(UNIVERSAL::require) >= 0.01
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(UNIVERSAL::require\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CGI)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Untaint-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
