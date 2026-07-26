%global source0_hash 794e6833e326b10d24369f9cdbfc1667105ef6591e8f41e561a3d41a7027a809

Name:           perl-HTTP-Parser-XS
Summary:        A fast, primitive HTTP request parser
Version:        0.17
Release:        37%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZUHO/HTTP-Parser-XS-%{version}.tar.gz 
URL:            https://metacpan.org/release/HTTP-Parser-XS

BuildRequires: make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::ReadmeFromPod)
BuildRequires:  perl(Module::Install::TestTarget)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(XSLoader)

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
HTTP::Parser::XS is a fast, primitive HTTP request parser that can
be used either for writing a synchronous HTTP server or an event-
driven server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Parser-XS-%{version}
/usr/bin/rm -r inc/*
/usr/bin/perl -pi -e '/^inc\//d' MANIFEST

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto
%{_mandir}/man3/*.3*

%changelog
%autochangelog
