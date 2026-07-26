%global source0_hash 1dff8f812118d7320818832835707c99b6400e56982949bad8d152004072e8a4

Name:           perl-Affix-Infix2Postfix
Version:        0.03
Release:        48%{?dist}
Summary:        Perl extension for converting from infix notation to postfix notation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Affix-Infix2Postfix
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADDI/Affix-Infix2Postfix-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests only
# -

%description
Infix2Postfix as the name suggests converts from infix to postfix notation.
The reason why someone would like to do this is that postfix notation is
generally much easier to do in computers. For example take an expression
like: a+b+c*d. For us humans it's pretty easy to do that calculation. But
it's actually much better for computers to get a string of operations such
as: a b + c d * +, where the variable names mean put variable on stack.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Affix-Infix2Postfix-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
