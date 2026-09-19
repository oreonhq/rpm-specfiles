%global source0_hash 600da9292b22193f8b72d1b8dbf0af13d201edcc73a8292882461550e8db5221

Name:           perl-App-Cmd
Summary:        Write command line apps with less suffering
Version:        0.338
Release:        2%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/App-Cmd-%{version}.tar.gz 
Patch0:         App-Cmd-support-blib.patch
URL:            https://metacpan.org/release/App-Cmd
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-interpreter >= 5.20.0
BuildRequires:  perl-generators
BuildRequires:  perl(parent)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Load) >= 0.06
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::OptList)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Getopt::Long::Descriptive) >= 0.084
BuildRequires:  perl(IO::TieCombine) >= 1
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Module::Pluggable::Object)
BuildRequires:  perl(String::RewritePrefix)
BuildRequires:  perl(Sub::Exporter) >= 0.975
BuildRequires:  perl(Sub::Exporter::Util)
BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Text::Abbrev)
BuildRequires:  perl(experimental)

Requires:       perl(Getopt::Long::Descriptive) >= 0.084
Requires:       perl(IO::TieCombine) >= 1
Requires:       perl(Sub::Exporter) >= 0.975

%{?perl_default_filter}

%description
App::Cmd is intended to make it easy to write complex command-line
applications without having to think about most of the annoying things
usually involved.

For information on how to start using App::Cmd, see App::Cmd::Tutorial.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n App-Cmd-%{version}
%patch 0
/usr/bin/perl -pi -e 's|^#!perl|#!/usr/bin/perl|' t/*.t t/*.pl

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/App*
%{_mandir}/man3/App*.3*

%changelog
%autochangelog
