%global source0_hash 2c97ca2be3b859e4a3bc35d706da9829a30aead0206e43f00d0136d995ae783c

Name:           perl-Ace
Version:        1.92
Release:        50%{?dist}
Summary:        Perl module for interfacing with ACE bioinformatics databases
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/AcePerl
Source0:        https://cpan.metacpan.org/modules/by-module/Ace/AcePerl-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Pod::Html)
BuildRequires:  sed

%description
AcePerl is a Perl interface for the ACEDB object-oriented database.
Designed specifically for use in genome sequencing projects, ACEDB
provides powerful modeling and management services for biological and
laboratory data.

%global __requires_exclude %{?__requires_exclude:__requires_exclude|}perl\\(Ace::Browser::LocalSiteDefs\\)$
%{?perl_default_filter}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n AcePerl-%{version}
# remove all execute bits from the doc stuff and fix interpreter
# so that dependency generator doesn't try to fulfill deps
find examples -type f -exec chmod -x {} 2>/dev/null ';'
find examples -type f -exec sed -i 's#/usr/local/bin/perl#/usr/bin/perl#' {} 2>/dev/null ';'

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1 << EOF
1
n
EOF
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

## disable tests because they require network access
%check
%{?_with_check:make test || :}

%files
%doc examples
%doc ChangeLog DISCLAIMER.txt README README.ACEBROWSER
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
