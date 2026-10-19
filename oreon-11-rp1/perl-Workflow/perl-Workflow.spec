%global source0_hash 590a07acdacf6faecdb784ac596c0ab54e2d010855d74af657b83bb74dd6c78b
Name:           perl-Workflow
Version:        2.09
Release:        1%{?dist}
Summary:        Simple, flexible system to implement work-flows
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Workflow
Source0:        https://cpan.metacpan.org/authors/id/J/JO/JONASBN/Workflow-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude}|perl\\(DBI\\)
%global __requires_exclude %{?__requires_exclude}|perl\\(Data::UUID\\)
%global __requires_exclude %{?__requires_exclude}|perl\\(File::Spec::Functions\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Class::Factory)
BuildRequires:  perl(DBD::Mock)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::Strptime)
BuildRequires:  perl(English)
BuildRequires:  perl(Env)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Mock::MonkeyPatch)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Syntax::Keyword::Try)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Kwalitee)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(YAML)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The 'Workflow' Perl module implements a standalone work-flow system. It
aims to be simple but flexible and therefore powerful. Each piece of
the work-flow system has a direct and easily stated job, and hopefully
you'll find that you can put the pieces together to create very useful
systems.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Workflow-%{version}

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
/usr/bin/perl -pi -e 's/^#!\/usr\/bin\/env\ perl$/#!\/usr\/bin\/perl/' t/*.t
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
