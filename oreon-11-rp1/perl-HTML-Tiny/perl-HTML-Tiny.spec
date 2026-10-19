%global source0_hash 0f01df0c9fc80b3d9da288baabf8c0a53747444f7ae1eb9600e7afc4a3dcfeb5
Name:           perl-HTML-Tiny
Version:        1.08
Release:        9%{?dist}
Summary:        Lightweight, dependency free HTML/XML generation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-Tiny
Source0:        https://cpan.metacpan.org/authors/id/A/AR/ARISTOTLE/HTML-Tiny-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(warnings)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
HTML::Tiny is a simple, dependency free module for generating HTML (and
XML). It concentrates on generating syntactically correct XHTML using a
simple Perl notation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-Tiny-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
