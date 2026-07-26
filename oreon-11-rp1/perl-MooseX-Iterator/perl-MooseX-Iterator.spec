%global source0_hash 1be558d13c8c940e94a263ac95f707f9d7f3e407602024085ef0b79f9b282efe

Name:           perl-MooseX-Iterator
Version:        0.11
Release:        48%{?dist}
Summary:        Iterate over collections
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/dist/MooseX-Iterator
Source0:        https://cpan.metacpan.org/authors/id/R/RL/RLB/MooseX-Iterator-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Moose) >= 0.86
BuildRequires:  perl(Test::More) >= 0.42

%{?perl_default_filter}

# Filter requires
%global __requires_exclude ^perl\\(MooseX::Iterator::(Array|Hash|Meta::Iterable)\\)$

%description
This is an attempt to add Smalltalk-like streams to Moose. It currently
works with ArrayRefs and HashRefs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Iterator-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc
%{perl_vendorlib}/Moose*
%{_mandir}/man3/Moose*

%changelog
%autochangelog
