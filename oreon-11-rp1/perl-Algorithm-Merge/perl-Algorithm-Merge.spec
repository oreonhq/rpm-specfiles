%global source0_hash 9c0688258a1dc4b83988053b9f9a98e7728cdb9b69a5008dcbd251d0f80816cf
Name:           perl-Algorithm-Merge
Version:        0.08
Release:        46%{?dist}
Summary:        Three-way merge and diff
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Algorithm-Merge
Source0:        https://cpan.metacpan.org/authors/id/J/JS/JSMITH/Algorithm-Merge-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Algorithm::Diff) >= 1
Requires:       perl(Exporter)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Algorithm::Diff\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Algorithm::Diff)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module complements Algorithm::Diff by providing three-way merge and diff
functions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Algorithm-Merge-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
