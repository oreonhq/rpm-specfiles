%global source0_hash 05327530d346b80a61a6e943fbd749986bdca89211a4eb301c08c2d179314e11

Name:           perl-Test-LWP-UserAgent
Version:        0.036
Release:        12%{?dist}
Summary:        LWP::UserAgent suitable for simulating and testing network calls
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-LWP-UserAgent
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Test-LWP-UserAgent-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(namespace::clean) >= 0.19
BuildRequires:  perl(parent)
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI)
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Message::PSGI)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(if)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(lib)
BuildRequires:  perl(Moose)
BuildRequires:  perl(overload)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::Deep) >= 0.110
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::Warnings) >= 0.009
# Optional tests
BuildRequires:  perl(Module::Runtime::Conflicts)
BuildRequires:  perl(Moose::Conflicts)
# Test::RequiresInternet - Optional for tests

%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(MyApp::Client\\)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(MyApp::Client\\)

%description
This module is a subclass of LWP::UserAgent which overrides a few key low-
level methods that are concerned with actually sending your request over
the network, allowing an interception of that request and simulating a
particular response. This greatly facilitates testing of client networking
code where the server follows a known protocol.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(HTTP::Message::PSGI)
Requires:       perl(Module::Runtime::Conflicts)
Requires:       perl(Moose::Conflicts)
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-LWP-UserAgent-%{version}

# Help generators to recognize Perl scripts
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
mkdir %{buildroot}%{_libexecdir}/%{name}/examples
cp -a examples/MyApp %{buildroot}%{_libexecdir}/%{name}/examples
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
NO_NETWORK_TESTING=1 make test

%files
%license LICENCE
%doc Changes CONTRIBUTING docs examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
