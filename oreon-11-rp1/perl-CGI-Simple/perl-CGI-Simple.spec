%global source0_hash c57f0f3e32cdd80612645155c1b829b4ccbe4ced655de833ab93005989c27f2f

Name:           perl-CGI-Simple
Epoch:          1
Version:        1.282
Release:        2%{?dist}
Summary:        Simple totally OO CGI interface that is CGI.pm compliant
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-Simple
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MANWAR/CGI-Simple-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-doc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Pod::Perldoc)
BuildRequires:  perl(strict)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
# Optional tests
BuildRequires:  perl(HTTP::Request::Common)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Simple-%{version}
perldoc -t perlartistic > Artistic
perldoc -t perlgpl > COPYING

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license Artistic COPYING
%doc Changes README
%{perl_vendorlib}/CGI
%{_mandir}/man3/CGI::Simple*.3*

%changelog
%autochangelog
