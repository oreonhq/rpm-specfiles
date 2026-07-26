%global source0_hash bdccba1fa8e4c1cf3189c5e5a3529a6693a648aa5282b597538c7aaddce6d9c9

Name:           perl-CDDB_get
Version:        2.28
Release:        37%{?dist}
Summary:        Read the CDDB entry for an audio CD in your drive
# Artistic:     Artistic-1.0-Perl text
# cddb.pl:          "same conditions as Perl, i.e. GPL-2.0-only OR Artistic-1.0-Perl"
# CDDB_cache.pm:    "same conditions as Perl, i.e. GPL-2.0-only OR Artistic-1.0-Perl"
# CDDB_get.pm:      "same conditions as Perl, i.e. GPL-2.0-only OR Artistic-1.0-Perl"
# Copying:      GPL-2.0 text
# README:       "same conditions as Perl, i.e. GPL-2.0-only OR Artistic-1.0-Perl"
## Author mistook GPL versions, without a clear resolution, CPAN RT#132515.
License:        GPL-2.0-only
URL:            https://metacpan.org/release/CDDB_get
Source0:        https://cpan.metacpan.org/authors/id/F/FO/FONKIE/CDDB_get-%{version}.tar.gz
# Submitted to upstream, RT #79646
Patch0:         CDDB_get-2.28-Do-not-include-current-directory.patch
# Submitted to upstream, RT #79647
Patch1:         CDDB_get-2.28-cddb.pl-is-not-a-library.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.36
# Run-time:
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(MIME::Base64)
# Tests:
BuildRequires:  perl(Test::More)
Requires:       perl(DBI)

%description
This module/script gets the CDDB data for an audio CD. You need a CD-ROM drive
and an active Internet connection in order to do that.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n CDDB_get-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} "$RPM_BUILD_ROOT"/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I .
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
make test

%files
%license Artistic Copying
%doc Changes DATABASE README
%{_bindir}/cddb.pl
%{perl_vendorlib}/auto/CDDB_cache
%{perl_vendorlib}/auto/CDDB_get
%{perl_vendorlib}/CDDB_cache.pm
%{perl_vendorlib}/CDDB_get.pm
%{_mandir}/man3/CDDB_get.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
