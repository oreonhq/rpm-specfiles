%global source0_hash a2619add8d42d3209809f1aeeae79ae046ce86c18738adece635d21afc0540a2

%global cpan_name MogileFS-Utils

Name:           perl-%{cpan_name}
Version:        2.30
Release:        25%{?dist}
Summary:        Utilities for MogileFS
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DORMANDO/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# These listed in META.yml are needed at run-time only, but no test loads them:
# perl(MogileFS::Client) >= 1.16
# perl(Compress::Zlib)
# perl(LWP::Simple)
Requires:       perl(MogileFS::Client) >= 1.16

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(MogileFS::Client\\)$

%description
Utilities for the MogileFS distributed storage system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make %{?_smp_mflags} pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make %{?_smp_mflags} test

%files
%doc Changes
%{perl_vendorlib}/MogileFS
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
