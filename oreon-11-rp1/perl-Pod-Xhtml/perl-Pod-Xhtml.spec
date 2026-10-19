%global source0_hash e5c5b08ab8f70026ee20a48f38b851ecbc8508bdc17be69f0d0a645d4670d77f
Name:           perl-Pod-Xhtml
Version:        1.61
Release:        46%{?dist}
Summary:        Generate well-formed XHTML documents from POD format documentation
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Pod-Xhtml
Source0:        https://cpan.metacpan.org/authors/id/B/BB/BBC/Pod-Xhtml-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(Pod::ParseUtils)
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Assertions::TestScript)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
