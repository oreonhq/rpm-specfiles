%global source0_hash 3b573f68e7b3a36a87c860be258599330fac248b518854dfb5657ac483dca565

Name:           perl-Menlo
Version:        1.9019
Release:        24%{?dist}
Summary:        A CPAN client
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Menlo
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Menlo-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Runtime
# BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Tiny) >= 1.001
BuildRequires:  perl(constant)
# BuildRequires:  perl(CPAN::Common::Index) >= 0.006
# BuildRequires:  perl(CPAN::Common::Index::Mirror)
# BuildRequires:  perl(CPAN::Meta) >= 2.132830
BuildRequires:  perl(CPAN::Meta::Requirements)
# BuildRequires:  perl(CPAN::Meta::YAML)
BuildRequires:  perl(Exporter)
# BuildRequires:  perl(ExtUtils::Config) >= 0.003
# BuildRequires:  perl(ExtUtils::Helpers) >= 1.020
# BuildRequires:  perl(ExtUtils::Install)
# BuildRequires:  perl(ExtUtils::InstallPaths) >= 0.002
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
# BuildRequires:  perl(File::pushd)
BuildRequires:  perl(File::Spec)
# BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Getopt::Long) >= 2.36
# BuildRequires:  perl(HTTP::Tiny) >= 0.054
# BuildRequires:  perl(HTTP::Tinyish) >= 0.04
# BuildRequires:  perl(IO::Uncompress::Gunzip)
# BuildRequires:  perl(JSON::PP) >= 2
# BuildRequires:  perl(parent)
# BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(String::ShellQuote)
# BuildRequires:  perl(TAP::Harness::Env)
# BuildRequires:  perl(Time::Local)
# BuildRequires:  perl(URI)
# Tests only
BuildRequires:  perl(Test::More)
Requires:       git
Requires:       perl(Class::Tiny) >= 1.001
Requires:       perl(CPAN::Common::Index) >= 0.006
Requires:       perl(CPAN::Meta) >= 2.132830
Requires:       perl(File::pushd)
Requires:       perl(HTTP::Tiny) >= 0.054
Requires:       perl(HTTP::Tinyish) >= 0.04
Requires:       perl(Pod::Man)
Requires:       perl(String::ShellQuote)
Requires:       perl(TAP::Harness::Env)

%{?perl_default_filter}

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(CPAN::Common::Index\\)$
%global __requires_exclude :%__requires_exclude|^perl\\(CPAN::Meta\\)$
%global __requires_exclude :%__requires_exclude|^perl\\(Class::Tiny\\)$
%global __requires_exclude :%__requires_exclude|^perl\\(HTTP::Tiny\\)$

%description
Menlo is a code name for cpanm 2.0, developed with the goal to
replace cpanm and its back-end with a more flexible, extensible and
easier to use APIs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Menlo-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
