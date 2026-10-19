%global source0_hash 7a05827e52ab5a1dde2ea5c712927b1e58c8d251664d966627adf9dd30ec0512
Name:           perl-MooX-Locale-Passthrough
Version:        0.001
Release:        1%{?dist}
Summary:        Provide API used in translator modules without translating
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooX-Locale-Passthrough
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/MooX-Locale-Passthrough-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Moo::Role) >= 1.003
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Moo::Role\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
MooX::Locale::Passthrough is made to allow CPAN modules use translator API
without adding heavy dependencies (external software) or requirements
(operating resulting solution).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooX-Locale-Passthrough-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
