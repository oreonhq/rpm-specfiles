%global source0_hash 955397052af296dd69d605bd4dd7cd100727d62e771f77527c3aa76286016791

Name:           perl-Log-Dispatchouli
Version:        3.013
Release:        2%{?dist}
Summary:        Simple wrapper around Log::Dispatch
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Log-Dispatchouli
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Log-Dispatchouli-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(:VERSION) >= 5.20
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(experimental)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Log::Dispatch)
BuildRequires:  perl(Log::Dispatch::Array)
BuildRequires:  perl(Log::Dispatch::File)
BuildRequires:  perl(Log::Dispatch::Screen)
BuildRequires:  perl(Log::Dispatch::Syslog)
BuildRequires:  perl(overload)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(String::Flogger)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Exporter::GlobExporter) >= 0.002
BuildRequires:  perl(Try::Tiny) >= 0.04
# Tests only
BuildRequires:  perl(base)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(utf8)
Requires:       perl(Log::Dispatch::Array)
Requires:       perl(Log::Dispatch::File)
Requires:       perl(Log::Dispatch::Screen)
Requires:       perl(Log::Dispatch::Syslog)

%{?perl_default_filter}

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(DDR.*\\)
%global __requires_exclude %{__requires_exclude}|perl\\(SDR.*\\)

%description
Log::Dispatchouli is a thin layer above Log::Dispatch and meant to make it
dead simple to add logging to a program without having to think much about
categories, facilities, levels, or things like that. It is meant to make
logging just configurable enough that you can find the logs you want and
just easy enough that you will actually log things.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Log-Dispatchouli-%{version}

# Help file to recognise the Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
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
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Log*
%{_mandir}/man3/Log::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
