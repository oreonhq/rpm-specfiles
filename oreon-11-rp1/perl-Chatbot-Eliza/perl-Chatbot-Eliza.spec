%global source0_hash 1fca6db94b1426c6f5c532e45dbb27104ca81659f99f8addf6fe497eab7163c5

Name:           perl-Chatbot-Eliza
Version:        1.08
Release:        26%{?dist}
Summary:        Implementation of the Eliza algorithm
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Chatbot-Eliza
Source0:        https://cpan.metacpan.org/authors/id/G/GR/GRANTG/Chatbot-Eliza-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
# Tests:
BuildRequires:  perl(Test::More)

%description
This module implements the classic Eliza algorithm. The original Eliza
program was written by Joseph Weizenbaum and described in the
Communications of the ACM in 1966. Eliza is a mock Rogerian
psychotherapist. It prompts for user input, and uses a simple
transformation algorithm to change user input into a follow-up question.
The program is designed to give the appearance of understanding.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Chatbot-Eliza-%{version}
cd examples
find . -type f -exec chmod a-x {} +
for i in *; do
    iconv -f latin1 -t utf8 $i > $i.utf8 && \
    touch -r $i $i.utf8 && \
    mv $i.utf8 $i
done
cd ..

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
