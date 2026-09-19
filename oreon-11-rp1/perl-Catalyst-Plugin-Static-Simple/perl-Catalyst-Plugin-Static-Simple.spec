%global source0_hash 5a4d85a3588cd4e83f1b002581412e7d71b7d57f66056e5d87a36f93d89c9e7c

Name:           perl-Catalyst-Plugin-Static-Simple
Version:        0.37
Release:        15%{?dist}
Summary:        Make serving static pages painless
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Catalyst-Plugin-Static-Simple
Source0:        https://cpan.metacpan.org/authors/id/I/IL/ILMARI/Catalyst-Plugin-Static-Simple-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Catalyst) >= 5.30
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Log)
BuildRequires:  perl(Catalyst::Plugin::SubRequest)
BuildRequires:  perl(Catalyst::Runtime) >= 5.80008
BuildRequires:  perl(Catalyst::Test)
BuildRequires:  perl(Catalyst::Utils)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
BuildRequires:  perl(MIME::Types) >= 1.25
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoTabs)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(warnings)

Requires:       perl(Catalyst) >= 5.30
Requires:       perl(Catalyst::Runtime) >= 5.80008
Requires:       perl(MIME::Types) >= 1.25
Requires:       perl(MRO::Compat)
Requires:       perl(Moose)

%{?perl_default_filter}

%description
The Static::Simple plugin is designed to make serving static content in
your application during development quick and easy, without requiring a
single line of code from you.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Plugin-Static-Simple-%{version}

for file in t/07mime_types.t t/lib/IncTestApp/Controller/Root.pm \
            t/lib/TestApp.pm t/lib/TestApp/Controller/Root.pm; do
    /usr/bin/perl -pi -e 's/\r$/\n/' $file;
done

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
TEST_POD=1 %{make_build} test

%files
%doc Changes t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
