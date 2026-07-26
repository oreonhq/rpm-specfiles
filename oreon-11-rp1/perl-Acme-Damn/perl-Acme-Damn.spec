%global source0_hash 310d2d03ff912dcd42e4d946174099f41fe3a2dd57a497d6bd65baf1759b7e0e

Name:           perl-Acme-Damn
Version:        0.08
Release:        35%{?dist}
Summary:        Unbless Perl objects
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Acme-Damn
Source0:        https://cpan.metacpan.org/authors/id/I/IB/IBB/Acme-Damn-%{version}.tar.gz
# DynaLoader doesn't export anything. This causes errors in
# Perl versions 5.39.1 and higher. This patch removes the symbol import
# https://github.com/denormal/perl-Acme-Damn/pull/1
Patch0:         Acme-Damn-DynaLoader-autoload.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
Acme::Damn provides a single routine, damn(), which takes a blessed
reference (a Perl object), and unblesses it, to return the original
reference. I can't think of any reason why you might want to do this,
but just because it's of no use doesn't mean that you shouldn't be
able to do it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Acme-Damn-%{version}
%patch -P 0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 \
          NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Acme*
%{_mandir}/man3/*

%changelog
%autochangelog
