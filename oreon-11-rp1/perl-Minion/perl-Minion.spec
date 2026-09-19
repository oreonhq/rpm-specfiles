%global source0_hash f84ef5ab2d6cb94b32efde8331553b925343a900707355d18205dc2a3dacf3ac

Name:           perl-Minion
Version:        11.0
Release:        2%{?dist}
Summary:        High performance job queue for the Perl programming language
# Minion itself is Artistic-2.0
# Minion Artwork is CC-SA License, Version 4.0
# Bootstrap is licensed under the MIT License
# D3.js is licensed under the ISC License
# epoch.js is licensed under the MIT License
# Font Awesome is licensed under the MIT License and the SIL OFL 1.1
# moment.js is licensed under the MIT License
License:        Artistic-2.0 AND CC-BY-SA-4.0 AND MIT AND ISC

URL:            https://metacpan.org/release/Minion
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SRI/Minion-%{version}.tar.gz

BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::Date)
BuildRequires:  perl(Mojo::EventEmitter)
BuildRequires:  perl(Mojo::File)
BuildRequires:  perl(Mojo::IOLoop)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Mojo::Loader)
BuildRequires:  perl(Mojo::Pg)
BuildRequires:  perl(Mojo::Server)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(Mojolicious::Command)
BuildRequires:  perl(Mojolicious::Commands)
BuildRequires:  perl(Mojolicious::Plugin)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(YAML::XS) >= 0.67
# Tests
BuildRequires:  perl(Mojolicious::Lite)
BuildRequires:  perl(Test::Mojo)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)

%{?perl_default_filter}

%description
Minion is a high performance job queue for the Perl programming language,
with support for multiple named queues, priorities, delayed jobs, job
dependencies, job progress, job results, retries with back-off, rate
limiting, unique jobs, statistics, distributed workers, parallel
processing, auto-scaling, remote control, Mojolicious admin UI, resource
leak protection and multiple backends (such as PostgreSQL).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Minion-%{version}
chmod -x lib/Mojolicious/Plugin/Minion/resources/public/minion/epoch/*

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/Minion*
%{perl_vendorlib}/Mojolicious/Plugin/Minion*
%{_mandir}/man3/Minion*
%{_mandir}/man3/Mojolicious::Plugin::Minion*

%changelog
%autochangelog
