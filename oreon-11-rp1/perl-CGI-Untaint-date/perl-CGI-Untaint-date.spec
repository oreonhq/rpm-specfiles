%global source0_hash e635500cbdd56c7251ce61199c3f4d60508273ac07b3a6752347e65ca765c16c
Name:           perl-CGI-Untaint-date
Version:        1.00
Release:        56%{?dist}
Summary:        Validate a date
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-Untaint-date
Source0:        https://cpan.metacpan.org/authors/id/T/TM/TMTM/CGI-Untaint-date-%{version}.tar.gz
BuildArch:      noarch
Requires:	perl(Date::Manip) >= 5.00
Requires:	perl(Date::Simple) >= 0.01
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Date::Manip|Date::Simple)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Untaint)
BuildRequires:  perl(CGI::Untaint::printable)
BuildRequires:  perl(Date::Manip)
BuildRequires:  perl(Date::Simple)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl-Pod-Perldoc
BuildRequires:  perl-doc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Untaint-date-%{version}
perldoc -t perlgpl > COPYING
perldoc -t perlartistic > Artistic

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

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
