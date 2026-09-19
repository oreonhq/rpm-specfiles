%global source0_hash 50f07ac938bfa1e1c28ec95af39fd12569d761f9abcd9ee3f2299bf577a18a42

# Enable integration with Mojo
%bcond_without perl_LWP_ConsoleLogger_enables_mojo

Name:           perl-LWP-ConsoleLogger
%define cpan_version 1.000001
Version:        1.0.1
Release:        8%{?dist}
Summary:        LWP tracing and debugging
License:        Artistic-2.0
URL:            https://metacpan.org/release/LWP-ConsoleLogger
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/LWP-ConsoleLogger-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.16
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(Data::Printer) >= 0.36
BuildRequires:  perl(DateTime)
BuildRequires:  perl(HTML::Restrict)
BuildRequires:  perl(HTTP::Body)
BuildRequires:  perl(HTTP::CookieMonster)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(JSON::MaybeXS) >= 1.003005
BuildRequires:  perl(List::AllUtils)
BuildRequires:  perl(Log::Dispatch) >= 2.56
# LWP::ConsoleLogger::Everywhere tries loading LWP::UserAgent and
# Mojo::UserAgent to install logging hooks. There is no need to require them
# here. They will be pulled in by a third-party code.
BuildRequires:  perl(Module::Load::Conditional)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
BuildRequires:  perl(MooX::StrictConstructor)
BuildRequires:  perl(Parse::MIME)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(String::Trim)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Term::Size::Any)
BuildRequires:  perl(Text::SimpleTable::AutoWidth) >= 0.09
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Types::Common::Numeric)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(XML::Simple)
# Optional run-time:
BuildRequires:  perl(HTML::FormatText::Lynx) >= 23
%if %{with perl_LWP_ConsoleLogger_enables_mojo}
BuildRequires:  perl(Mojo::UserAgent)
%endif
# Tests:
# CPAN::Meta not helpful
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTML::FormatText::WithLinks)
BuildRequires:  perl(HTTP::CookieJar::LWP)
BuildRequires:  perl(Log::Dispatch::Array)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Plack::Handler::HTTP::Server::Simple)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Plack::Test::Agent)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::LWP::UserAgent)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(version)
BuildRequires:  perl(WWW::Mechanize)
%if %{with perl_LWP_ConsoleLogger_enables_mojo}
# Optional tests:
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojolicious) >= 7.13
%endif
Requires:       perl(Data::Printer) >= 0.36
Recommends:     perl(HTML::FormatText::Lynx) >= 23
Requires:       perl(JSON::MaybeXS) >= 1.003005
Requires:       perl(Log::Dispatch) >= 2.56
%if %{with perl_LWP_ConsoleLogger_enables_mojo}
Suggests:       perl(Mojo::UserAgent)
%endif

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Data::Printer|JSON::MaybeXS|Log::Dispatch)\\)$

%description
It can be hard (or at least tedious) to debug WWW::Mechanize scripts.
LWP::ConsoleLogger::Easy wrapper offers debug_ua() function that instantiates
LWP logging and also returns a LWP::ConsoleLogger object, which you may then
tweak to your heart's desire. If you need to tweak the settings that
LWP::ConsoleLogger::Easy chooses for you, please use LWP::ConsoleLogger. If
you're able to install HTML::FormatText::Lynx then you'll get highly readable
HTML to text conversions.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_LWP_ConsoleLogger_enables_mojo}
Requires:       perl(Mojo::Base)
Requires:       perl(Mojolicious) >= 7.13
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n LWP-ConsoleLogger-%{cpan_version}
# Correct shebangs
perl -i -MConfig -pe 's|#!/usr/bin/env perl|$Config{startperl}|' examples/*
# Help generators to recognize Perl scripts
for F in $(find t -name '*.t'); do
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
#!/bin/bash
unset LWPCL_LOGFILE
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset LWPCL_LOGFILE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes CONTRIBUTORS examples README.md
%dir %{perl_vendorlib}/LWP
%{perl_vendorlib}/LWP/ConsoleLogger
%{perl_vendorlib}/LWP/ConsoleLogger.pm
%{_mandir}/man3/LWP::ConsoleLogger.*
%{_mandir}/man3/LWP::ConsoleLogger::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
