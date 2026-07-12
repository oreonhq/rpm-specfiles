%global source0_hash 1900cc58acd29f93bf933b9d6c96cfc4896da95f34225a8643917993377f57fa

Name:           perl-Locale-US
Version:        3.04
Release:        31%{?dist}
Summary:        Two letter codes for state identification in the United States and vice versa
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Locale-US
Source0:        https://cpan.metacpan.org/modules/by-module/Locale/Locale-US-%{version}.tar.gz
Patch1:         Locale-US-2.112140-rt56989.patch
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(Data::Section::Simple)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Test)
# Dependencies
# (none)

Provides:       perl(Locale::US)
Provides:       perl(Locale::US)
%description
Map from United States two-letter identification codes to states and vice versa.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Locale-US-%{version}

# Add regression test for CPAN RT#56989
%patch -P 1 -p1

# Doesn't actually use Data::Dumper
sed -i -e '/use Data::Dumper/d' lib/Locale/US.pm t/1.t

# Script should be executable
chmod -c +x kruft2codes.pl

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README codes.dat kruft.txt
%{perl_vendorlib}/Locale/
%{_mandir}/man3/Locale::US*.3*

%changelog
%autochangelog
