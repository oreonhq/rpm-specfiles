%global source0_hash 05327530d346b80a61a6e943fbd749986bdca89211a4eb301c08c2d179314e11
Name:           perl-Test-LWP-UserAgent
Version:        0.036
Release:        12%{?dist}
Summary:        LWP::UserAgent suitable for simulating and testing network calls
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-LWP-UserAgent
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Test-LWP-UserAgent-%{version}.tar.gz
BuildArch:      noarch
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(MyApp::Client\\)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(MyApp::Client\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Message::PSGI)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Runtime::Conflicts)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Conflicts)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
mkdir %{buildroot}%{_libexecdir}/%{name}/examples
cp -a examples/MyApp %{buildroot}%{_libexecdir}/%{name}/examples
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

NO_NETWORK_TESTING=1 make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Test-LWP-UserAgent-tests -f %{oreon_filedir}/perl-Test-LWP-UserAgent-tests.list

%changelog

%autochangelog
