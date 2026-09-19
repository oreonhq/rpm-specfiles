%global source0_hash ef71a04826d1362b2b76ecb21ce173c37d38a47a9fec283aa982435890f4f1b1

Name:           perl-Tie-Sub
Version:        1.001
Release:        28%{?dist}
Summary:        Tying a subroutine, function or method to a hash
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tie-Sub
Source0:        https://cpan.metacpan.org/authors/id/S/ST/STEFFENW/Tie-Sub-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
# Optional tests only
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tie-Sub-%{version}
perl -pi -e 's|\r||g' Changes README example/*
perl -pi -e 's|^#!perl|#!/usr/bin/perl|' example/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes example README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
