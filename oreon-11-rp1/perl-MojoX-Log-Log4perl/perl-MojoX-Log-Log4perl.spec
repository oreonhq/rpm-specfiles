%global source0_hash bb53e68f0ed0d54f6225ff15fa20c7476d1fee3c818ba90eff9ddcebdadcabd3
Name:           perl-MojoX-Log-Log4perl
Version:        0.12
Release:        17%{?dist}
Summary:        Log::Log4perl logging for Mojo/Mojolicious
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MojoX-Log-Log4perl
Source0:        https://cpan.metacpan.org/authors/id/G/GA/GARU/MojoX-Log-Log4perl-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Log::Log4perl::Level)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Log::Log4perl::Level)
BuildRequires:  perl(Mojo::Asset::File)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::EventEmitter)
BuildRequires:  perl(Mojolicious::Lite)
BuildRequires:  perl(Test::Mojo)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
MojoX::Log::Log4perl provides a Mojo::Log implementation that uses
Log::Log4perl as the underlying log mechanism. It provides all the
methods listed in Mojo::Log (and many more from Log4perl).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MojoX-Log-Log4perl-%{version}

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
