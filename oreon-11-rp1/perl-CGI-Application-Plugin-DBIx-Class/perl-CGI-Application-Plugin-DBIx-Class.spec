%global source0_hash 7ad37eb997042d40b3bf22b7a62be1856a8d9e5855a81314aab026d335b2cb3c
Name:           perl-CGI-Application-Plugin-DBIx-Class
Version:        1.000101
Release:        1%{?dist}
Summary:        Access a DBIx::Class Schema from a CGI::Application
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-Application-Plugin-DBIx-Class
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FREW/CGI-Application-Plugin-DBIx-Class-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(SQL::Translator)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(parent)
BuildRequires:  perl-generators
# /oreon:deps
%description
This module helps you to map various DBIx::Class features to CGI
parameters. For the most part that means it will help you search, sort, and
paginate with a minimum of effort and thought. Currently it uses the
connection from CGI::Application::Plugin::DBH.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-DBIx-Class-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
