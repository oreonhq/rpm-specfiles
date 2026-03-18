# Perform optional tests
%{bcond_without perl_HTTP_Daemon_enables_optional_test}

Name:           perl-HTTP-Daemon
Version:        6.16
Release:        8%{?dist}
Summary:        Simple HTTP server class
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Daemon
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTTP-Daemon-%{version}.tar.gz
# Use Makefile.PL without unneeded dependencies
Patch0:         HTTP-Daemon-6.04-EU-MM-is-not-deprecated.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  findutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTTP::Date) >= 6
BuildRequires:  perl(HTTP::Request) >= 6
BuildRequires:  perl(HTTP::Response) >= 6
BuildRequires:  perl(HTTP::Status) >= 6
BuildRequires:  perl(IO::Socket::IP) >= 0.32
BuildRequires:  perl(LWP::MediaTypes) >= 6
BuildRequires:  perl(Socket)
BuildRequires:  perl(warnings)
# Tests only:
BuildRequires:  perl(lib)
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(URI)
# Optional tests:
%if %{with perl_HTTP_Daemon_enables_optional_test} && !%{defined %perl_bootstrap}
BuildRequires:  perl(LWP::RobotUA)
BuildRequires:  perl(LWP::UserAgent) >= 6.37
# CPAN::Meta not helpful
# CPAN::Meta::Prereqs not helpful
%endif
Requires:       perl(HTTP::Date) >= 6
Requires:       perl(HTTP::Request) >= 6
Requires:       perl(HTTP::Response) >= 6
Requires:       perl(HTTP::Status) >= 6
Requires:       perl(IO::Socket::IP) >= 0.32
Requires:       perl(LWP::MediaTypes) >= 6
Conflicts:      perl-libwww-perl < 6

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(HTTP::(Date|Request|Response|Status)|IO::Socket::IP|LWP::MediaTypes\\)$
# Remove private test modules
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(TestServer|TestServer::(BasicTests|Reflect)\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(TestServer|TestServer::(BasicTests|Reflect)\\)$

%description
Instances of the HTTP::Daemon class are HTTP/1.1 servers that listen on a
socket for incoming requests. The HTTP::Daemon is a subclass of
IO::Socket::IP, so you can perform socket operations directly on it too.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
# perl-generators doesn't detect 'use Test::Needs 'LWP::RobotUA';'
Requires:       perl(LWP::RobotUA)
# perl-generators doesn't detect 'use Test::Needs 'LWP::UserAgent';'
Requires:       perl(LWP::UserAgent) >= 6.37

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n HTTP-Daemon-%{version}
%patch -P0 -p1
# Help generators to recognize Perl scripts
for F in $(find t/ -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENCE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.16-8
- Prepare for Oreon 11 (RP1)
