%global source0_hash 0ac93834ee97cc71d86e2c4d2000abe7e47a38513ebb2f97320fe2b90e2d8da3

Name:           perl-Locale-SubCountry
Version:        2.07
Release:        13%{?dist}
Summary:        ISO 3166-2 two letter subcountry codes
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Locale-SubCountry
Source0:        https://cpan.metacpan.org/authors/id/K/KI/KIMRYAN/Locale-SubCountry-%{version}.tar.gz
# Normalize Changes encoding
Patch0:         Locale-SubCountry-2.04-Convert-to-UTF-8.patch
BuildArch:      noarch 
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(Exporter)
BuildRequires:  perl(JSON) >= 1
BuildRequires:  perl(locale) >= 1
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Test::More) >= 0.94
Requires:       perl(JSON) >= 1
Requires:       perl(locale) >= 1

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((JSON|locale|Test::More)\\)$

%description
This module allows you to convert the full name for a countries administrative
region to the code commonly used for postal addressing. The reverse look-up
can also be done. Sub country codes are defined in "ISO 3166-2:2007, Codes for
the representation of names of countries and their subdivisions".

Sub countries are termed as states in the US and Australia, provinces in
Canada and counties in the UK and Ireland.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.94

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Locale-SubCountry-%{version}
%patch -P0 -p1
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENCE
%doc Changes README examples/
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
