%global source0_hash 5e267a4d7620b368481204c88ea2044b8b2a58ff8b05577f2717b2754c0414ce
Name:           perl-Role-HasMessage
Version:        0.007
Release:        1%{?dist}
Summary:        Thing with a message method
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Role-HasMessage
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Role-HasMessage-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(String::Errf)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(blib)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is another extremely simple role. A class that includes
Role::HasMessage is promising to provide a message method that returns a
string summarizing the message or event represented by the object. It does
not provide any actual behavior.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Role-HasMessage-%{version}

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

RELEASE_TESTING=1 %{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
