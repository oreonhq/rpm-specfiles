%global source0_hash 7ce137b2e797b7c0901f3adf1a05a19343356cd1f04676aa1c56a9f624f859ad

Name:           perl-Date-Calc
Version:        6.4
Release:        32%{?dist}
Summary:        Gregorian calendar date calculations
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Date-Calc
Source0:        https://cpan.metacpan.org/authors/id/S/ST/STBEY/Date-Calc-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Config)
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(Bit::Vector) >= 7.1
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp::Clan) >= 6.04
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(vars)
# Tests only
Requires:       perl(Bit::Vector) >= 7.1
Requires:       perl(Carp::Clan) >= 6.04

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Bit::Vector\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Carp::Clan\\)$
# Filter unwanted Provides:
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(Date::Calc\\)$

%description
The library provides all sorts of date calculations based on the
Gregorian calendar (the one used in all western countries today),
thereby complying with all relevant norms and standards: ISO/R
2015-1971, DIN 1355 and, to some extent, ISO 8601 (where applicable).

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Date-Calc-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*
for file in %{buildroot}%{_mandir}/man3/Date::Calc.3pm \
            CREDITS.txt; do
  iconv -f iso-8859-1 -t utf-8 < "$file" > "${file}_"
  mv -f "${file}_" "$file"
done

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license license/Artistic.txt license/GNU_GPL.txt license/GNU_LGPL.txt
%doc CHANGES.txt CREDITS.txt README.txt
%{perl_vendorlib}/Date/Calc*
%{perl_vendorlib}/Date/Calendar*
%{_mandir}/man3/Date::Calc*.3*
%{_mandir}/man3/Date::Calendar*.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.4-32
- Prepare for Oreon 11 (RP1)
