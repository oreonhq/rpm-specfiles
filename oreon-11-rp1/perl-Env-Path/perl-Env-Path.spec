%global source0_hash 244bf093798832a7d841d9ee5b4b0e6b489996eef63541e505091aa34a9015e2

Name:           perl-Env-Path
Version:        0.19
Release:        34%{?dist}
Summary:        Advanced operations on path variables
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Env-Path
Source0:        https://cpan.metacpan.org/authors/id/D/DS/DSB/Env-Path-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  sed

%{?perl_default_filter}

%description
Env::Path presents an object-oriented interface to path variables, defined
as that subclass of environment variables which name an ordered list of
filesystem elements separated by a platform-standard separator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Env-Path-%{version}

chmod 0644 examples/Whence
sed -i '1s,#!.*,%(perl -MConfig -e 'print $Config{startperl}'),' examples/Whence

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README examples/Whence
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/*

%changelog
%autochangelog
