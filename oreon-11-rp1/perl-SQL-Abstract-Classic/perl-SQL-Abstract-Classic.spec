%global source0_hash 4e3d1dfd095b2123268586bb06b86929ea571388d4e941acccbdcda1e108ef28

Name:           perl-SQL-Abstract-Classic
Version:        1.91
Release:        18%{?dist}
Summary:        Generate SQL from Perl data structures
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/SQL-Abstract-Classic/
Source0:        https://cpan.metacpan.org/authors/id/R/RI/RIBASUSHI/SQL-Abstract-Classic-%{version}.tar.gz
# Inhibit installing dependencies from CPAN, bug #1873016
Patch0:         SQL-Abstract-Classic-1.91-Inhibit-installing-dependencies-from-CPAN.patch
BuildArch:      noarch
# Build
BuildRequires: make
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.0
BuildRequires:  perl(inc::Module::Install) >= 1.06
BuildRequires:  perl(Module::Install::Makefile)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(List::Util)
BuildRequires:  perl(mro)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Text::Balanced) >= 2.00
# Tests
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(SQL::Abstract::Test)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Exception) >= 0.31
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warn)
Requires:       perl(Exporter) >= 5.57
Requires:       perl(mro)
Requires:       perl(Text::Balanced) >= 2.00

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Exporter\\)

%description
This module was inspired by the excellent DBIx::Abstract. However, in using
that module I found that what I really wanted to do was generate SQL, but
still retain complete control over my statement handles and use the DBI
interface. So, I set out to create an abstract SQL generation module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n SQL-Abstract-Classic-%{version}
%patch -P0 -p1
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
