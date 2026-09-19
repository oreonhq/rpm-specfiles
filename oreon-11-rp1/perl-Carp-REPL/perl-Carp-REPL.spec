%global source0_hash 78afef4ebdd3fd3848c60839cabe0766a8cbf419a29e6a80246c5752fb17d1a7

Name:           perl-Carp-REPL
Version:        0.18
Release:        31%{?dist}
Summary:        Read-eval-print-loop on die and/or warn
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Carp-REPL
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Carp-REPL-%{version}.tar.gz
# Do not use broken Data::Dump::Streamer, bug #1231297, CPAN RT#105016
Patch0:         Carp-REPL-0.18-Use-Data-Dumper-instead-of-Data-Dump-Streamer.patch
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::LexAlias)
BuildRequires:  perl(Devel::REPL::Plugin)
BuildRequires:  perl(Devel::REPL::Plugin::LexEnv)
# XXX: BuildRequires:  perl(Devel::REPL::Script)
BuildRequires:  perl(Devel::StackTrace::WithLexicals)
BuildRequires:  perl(namespace::autoclean)
# XXX: BuildRequires:  perl(Sub::Exporter)
# XXX: BuildRequires:  perl(Test::Builder)
# Tests only
BuildRequires:  perl(Devel::REPL)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Expect)
BuildRequires:  perl(Test::More)
Requires:       perl(Sub::Exporter)
Requires:       perl(Devel::REPL::Plugin::LexEnv)
Requires:       perl(Devel::REPL::Script)
Requires:       perl(Test::Builder)

%{?perl_default_filter}

%description
Carp-REPL is a debugging aid for Perl programs. When a program dies (or warns),
you get a REPL instead of dying or continuing blindly.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Carp-REPL-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
