%global source0_hash e5c5b08ab8f70026ee20a48f38b851ecbc8508bdc17be69f0d0a645d4670d77f

Name:           perl-Pod-Xhtml
Version:        1.61
Release:        46%{?dist}
Summary:        Generate well-formed XHTML documents from POD format documentation
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Pod-Xhtml
Source0:        https://cpan.metacpan.org/authors/id/B/BB/BBC/Pod-Xhtml-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
# Getopt::Long not used at tests
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(Pod::ParseUtils)
# Pod::Usage not used at tests
BuildRequires:  perl(strict)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(lib)
# Log::Trace not used
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Assertions::TestScript)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00

%{?perl_default_filter}

%description
This module parses files containing POD content and generates well-formed
XHTML documents from it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Pod-Xhtml-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes COPYING README
%{perl_vendorlib}/*
%{_bindir}/pod2xhtml
%{_mandir}/man1/pod2xhtml.1.gz
%{_mandir}/man3/*

%changelog
%autochangelog
