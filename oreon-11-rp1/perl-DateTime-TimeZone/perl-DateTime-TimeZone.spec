%global source0_hash 1c1285d911027d276f235b32a888ee7425c9ab356ee62cd126c4b3ee3ea659b3
%global source1_hash 114543d9f19a6bfeb5bca43686aea173d38755a3db1f2eec112647ae92c6f544

# Run optional test
%bcond_without perl_DateTime_TimeZone_enables_optional_test

# Regenerate Perl library code from upstream Olson database of this date
%global tzversion 2026b

Name:           perl-DateTime-TimeZone
Version:        2.68
Release:        1%{?dist}
Summary:        Time zone object base class and factory
# tzdata%%{tzversion}.tar.gz archive:   LicenseRef-Public-Domain
# other files:                          GPL-1.0-or-later OR Artistic-1.0-Perl
# Some other files are generated from tzdata%%{tzversion}.tar.gz content by
# upstream or locally:                  LicenseRef-Public-Domain
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Public-Domain
URL:            https://metacpan.org/release/DateTime-TimeZone
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-TimeZone-%{version}.tar.gz
%if %{defined tzversion}
Source1:        https://data.iana.org/time-zones/releases/tzdata%{tzversion}.tar.gz
%endif
# Parse local time zone definition from /etc/localtime as before giving up,
# bug #1135981, CPAN RT#55029
Patch0:         DateTime-TimeZone-2.04-Parse-etc-localtime-by-DateTime-TimeZone-Tzfile.patch
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
%if !%{defined perl_bootstrap} && %{defined tzversion}
# Avoid circular dependencies - perl-DateTime strictly requires DateTime::TimeZone
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(integer)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Locale::Country) >= 3.11
BuildRequires:  perl(Parallel::ForkManager)
BuildRequires:  sed
%endif
# Runtime
BuildRequires:  perl(Class::Singleton) >= 1.03
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd) >= 3
%if !%{defined perl_bootstrap}
BuildRequires:  perl(DateTime::Duration)
%endif
# Unused BuildRequires:  perl(DateTime::TimeZone::Tzfile)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Params::ValidationCompiler) >= 0.13
BuildRequires:  perl(parent)
BuildRequires:  perl(Specio::Library::Builtins)
BuildRequires:  perl(Specio::Library::String)
BuildRequires:  perl(Try::Tiny)
# Tests only
BuildRequires:  perl(base)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::Fatal)
# Test::Mojibake not used
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
%if %{with perl_DateTime_TimeZone_enables_optional_test}
# Optional tests
%if !%{defined perl_bootstrap}
BuildRequires:  perl(DateTime) >= 0.1501
%endif
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Taint)
%endif
Requires:       perl(File::Basename)
Requires:       perl(File::Compare)
Requires:       perl(File::Find)
# Require optional DateTime::TimeZone::Tzfile to work in mock after tzdata
# upgrade, bug #1135981
Requires:       perl(DateTime::TimeZone::Tzfile)
%if !%{defined perl_bootstrap} && %{defined tzversion}
Provides:       bundled(tzdata) = %{tzversion}
%else
Provides:       bundled(tzdata)
%endif

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Class::Singleton\\)$

# Avoid circular dependencies - perl-DateTime strictly requires DateTime::TimeZone
%if 0%{?perl_bootstrap}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DateTime::Duration\\)
%endif

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(T::RequireDateTime\\)

Provides:       perl(DateTime::TimeZone)
%description
This class is the base class for all time zone objects. A time zone is
represented internally as a set of observances, each of which describes the
offset from GMT for a given time period.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_DateTime_TimeZone_enables_optional_test}
Requires:       perl(Test::Output)
Requires:       perl(Test::Taint)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%if !%{defined perl_bootstrap} && %{defined tzversion}
%setup -q -T -a 1 -c -n tzdata-%{tzversion}
%endif
%setup -q -T -b 0 -n DateTime-TimeZone-%{version}
%patch -P0 -p1

# Help generators to recognize Perl scripts
for F in t/*.t t/*.pl; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
%if !%{defined perl_bootstrap} && %{defined tzversion}
JOBS=$(printf '%%s' "%{?_smp_mflags}" | sed 's/.*-j\([0-9][0-9]*\).*/\1/')
perl tools/parse_olson --dir ../tzdata-%{tzversion} --version %{tzversion} \
    --jobs $JOBS --clean
%endif
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
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.68-1
- Import
