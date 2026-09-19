%global source0_hash 809884b151b9f867c35d277f7cc77a040eb28faf0b368cd91a39f555c44e082d

Name:           perl-Data-Properties
Version:        1.07
Release:        13%{?dist}
Summary:        Flexible properties handling 
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0

URL:            https://metacpan.org/release/Data-Properties
Source0:        https://cpan.metacpan.org/authors/id/J/JV/JV/Data-Properties-%{version}.tar.gz
BuildArch:      noarch
# build requirements
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# runtime requirements
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
# test requirements
BuildRequires:  perl(Test)

%{?perl_default_filter}

%description
Data-Properties is a Perl version of Java's java.util.Properties and aims to be
format-compatible with that class.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Properties-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes
%license LICENSE
%{perl_vendorlib}/Data*
%{_mandir}/man3/Data*

%changelog
%autochangelog
