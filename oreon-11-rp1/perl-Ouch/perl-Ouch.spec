%global source0_hash 66dc6b95ed2786be44ab129da9f4a4ce8e1e332f8312a2687a23ad8a3800eff4

Name:           perl-Ouch
Version:        0.0501
Release:        22%{?dist}
Summary:        Exceptions that don't hurt
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Ouch
Source0:        https://cpan.metacpan.org/authors/id/R/RI/RIZEN/Ouch-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
# Tests only
BuildRequires:  perl(lib)
# Pod::Coverage::TrustPod not used
BuildRequires:  perl(Test::More)
# Test::Pod 1.41 not used
# Test::Pod::Coverage 1.08 not used
BuildRequires:  perl(Test::Trap)

%description
Ouch provides a class for exception handling that doesn't require a
lot of boilerplate, nor any up front definition. If Exception::Class
is working for you, great! But if you want something that is faster,
easier to use, requires less typing, and has no prerequisites, but still
gives you much of that same functionality, then Ouch is for you.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Ouch-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
unset AUTHOR_TESTING
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
