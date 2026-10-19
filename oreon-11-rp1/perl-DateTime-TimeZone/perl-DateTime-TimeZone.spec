%global source0_hash c617009adefecbe14cf1c757bd6a964acb23943431fb3a047bdbd87c07c67174
%global source1_hash 114543d9f19a6bfeb5bca43686aea173d38755a3db1f2eec112647ae92c6f544
%bcond_without perl_DateTime_TimeZone_enables_optional_test
%global tzversion 2026b
Name:           perl-DateTime-TimeZone
Version:        2.71
Release:        1%{?dist}
Summary:        Time zone object base class and factory
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Public-Domain
URL:            https://metacpan.org/release/DateTime-TimeZone
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-TimeZone-%{version}.tar.gz
%if %{defined tzversion}
Source1:        https://data.iana.org/time-zones/releases/tzdata%{tzversion}.tar.gz
%endif
Patch0:         DateTime-TimeZone-2.04-Parse-etc-localtime-by-DateTime-TimeZone-Tzfile.patch
BuildArch:      noarch
%if !%{defined perl_bootstrap} && %{defined tzversion}
%endif
%if !%{defined perl_bootstrap}
%endif
%if %{with perl_DateTime_TimeZone_enables_optional_test}
%if !%{defined perl_bootstrap}
%endif
%endif
Requires:       perl(File::Basename)
Requires:       perl(File::Compare)
Requires:       perl(File::Find)
Requires:       perl(DateTime::TimeZone::Tzfile)
%if !%{defined perl_bootstrap} && %{defined tzversion}
Provides:       bundled(tzdata) = %{tzversion}
%else
Provides:       bundled(tzdata)
%endif
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Class::Singleton\\)$
%if 0%{?perl_bootstrap}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DateTime::Duration\\)
%endif
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(T::RequireDateTime\\)
Provides:       perl(DateTime::TimeZone)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Class::Singleton)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Duration)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Locale::Country)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Parallel::ForkManager)
BuildRequires:  perl(Params::ValidationCompiler)
BuildRequires:  perl(Specio::Library::Builtins)
BuildRequires:  perl(Specio::Library::String)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::Taint)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(integer)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-DateTime-TimeZone-tests -f %{oreon_filedir}/perl-DateTime-TimeZone-tests.list

%changelog

%autochangelog
