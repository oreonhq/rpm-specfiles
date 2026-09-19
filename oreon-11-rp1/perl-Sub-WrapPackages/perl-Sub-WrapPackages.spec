%global source0_hash 83c86be0c6260cab34564947c36005ecdb6925e6e0a57da482c70bce4cbccbd2

Name:           perl-Sub-WrapPackages
Version:        2.02
Release:        11%{?dist}
Summary:        Add wrappers around all the subroutines in packages
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Sub-WrapPackages
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/Sub-WrapPackages-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Caller::IgnoreNamespaces)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Hook::LexWrap)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
BuildRequires:  perl(Sub::Prototype)

%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude}|perl\\(lib\\)

%description
This is mostly a wrapper around Damian Conway's Hook::LexWrap module. This
module allows you to wrap function calls and exits with functions of your
choice.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Sub-WrapPackages-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
