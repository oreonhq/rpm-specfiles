%global source0_hash 9607db14aa4f61581350668a2c541e03727fbbc573c223d0e237c72ddf09092c

Name:           perl-Palm-PDB
Version:        1.400
Release:        32%{?dist}
Summary:        Parse Palm database files
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Palm-PDB
Source0:        https://cpan.metacpan.org/authors/id/C/CJ/CJM/Palm-PDB-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(constant) >= 1.03
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
The Palm::PDB module provides a framework for reading and writing database
files for use on PalmOS devices such as the PalmPilot. It can read and
write both Palm Database (.pdb) and Palm Resource (.prc) files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Palm-PDB-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Palm*
%{_mandir}/man3/Palm*

%changelog
%autochangelog
