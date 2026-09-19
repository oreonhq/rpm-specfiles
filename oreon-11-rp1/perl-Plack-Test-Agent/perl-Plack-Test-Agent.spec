%global source0_hash 42ca970fcc2762603808ec868a437b7862c78f0983ece6a2fddb990fbae9e080

# Perform an optional test
%bcond_without perl_Plack_Test_Agent_enables_optional_test

Name:           perl-Plack-Test-Agent
Version:        1.6
Release:        3%{?dist}
Summary:        Object-oriented interface for testing PSGI applications
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Plack-Test-Agent
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/Plack-Test-Agent-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Message::PSGI)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(parent)
BuildRequires:  perl(Plack::Loader)
BuildRequires:  perl(Plack::Util::Accessor)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(Test::WWW::Mechanize)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Server::Simple::PSGI)
BuildRequires:  perl(Modern::Perl)
BuildRequires:  perl(open)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(utf8)
%if %{with perl_Plack_Test_Agent_enables_optional_test}
# Optional tests:
# CPAN::Meta not helpful
# CPAN::Meta::Prereqs not helpful
BuildRequires:  perl(Test::Memory::Cycle)
%endif

%description
Plack::Test::Agent is an object-oriented interface to test PSGI applications.
It can perform GET and POST requests against PSGI applications either in
process or over HTTP through a Plack::Handler compatible backend.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Plack-Test-Agent-%{version}
%if %{without perl_Plack_Test_Agent_enables_optional_test}
rm t/cycle.t
perl -i -ne 'print $_ unless m{^t/cycle\.t}' MANIFEST
%endif
# Normalize shebangs
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset AUTHOR_TESTING http_proxy
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING http_proxy
make test

%files
%license LICENSE
%doc Changes README.md
%dir %{perl_vendorlib}/Plack
%dir %{perl_vendorlib}/Plack/Test
%{perl_vendorlib}/Plack/Test/Agent.pm
%{_mandir}/man3/Plack::Test::Agent.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
