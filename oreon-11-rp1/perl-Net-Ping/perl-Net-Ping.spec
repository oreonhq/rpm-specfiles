# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 b47df3cfd9692ccd0071ad39fe74718ebc32f59701556a604fd15a09f09e0d74
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global base_version 2.75
# Perform optional tests
%bcond_without perl_Net_Ping_enables_optional_test

Name:           perl-Net-Ping
Version:        2.76
Release:        521%{?dist}
Summary:        Check a remote host for reachability
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Ping/
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Net-Ping-%{base_version}.tar.gz
# Unbundled from perl 5.37.11
Patch0:         Net-Ping-2.75-Upgrade-to-2.76.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.2
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IO::Socket::INET)
# Net::Ping::External not used at tests
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket) >= 2.007
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
# Win32 not used on Linux
# Tests:
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
# sudo not used
%if %{with perl_Net_Ping_enables_optional_test}
# Optional tests:
BuildRequires:  perl(:VERSION) >= 5.6
# Class::XSAccessor not used
BuildRequires:  perl(IO::Socket)
# List::MoreUtils not used
# Module::CPANTS::Kwalitee::Uses not used
# Text::CSV_XS not used
# Test::CPAN::Meta not used
# Test::Kwalitee not used
BuildRequires:  perl(Test::Pod) >= 1.22
# Test::Pod::Coverage not used
%endif
Requires:       perl(IO::Socket::INET)
# Keep Net::Ping::External optional
Suggests:       perl(Net::Ping::External)
Conflicts:      perl < 4:5.22.0-350

%description
Net::Ping module contains methods to test the reachability of remote hosts on
a network.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Socket)
Requires:       perl(IO::Socket)
Requires:       perl(IO::Socket::INET)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%oreon_verify_sources
%setup -q -n Net-Ping-%{base_version}
%patch -P0 -p1
# Remove author tests
rm t/6*.t
# Remove appveyor script
rm t/appveyor-test.bat
# Remove removed files from MANIFEST file
perl -i -ne 'print $_ unless m{^(?:t/6.*\.t|appveyor-test\.bat)}' MANIFEST
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
unset PERL_CORE
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset AUTHOR_TESTING IS_MAINTAINER NET_PING_FAIL_IP PERL_TEST_Net_Ping \
    TEST_PING_HOST TEST_PING6_HOST
export NO_NETWORK_TESTING=1
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
unset AUTHOR_TESTING IS_MAINTAINER NET_PING_FAIL_IP PERL_TEST_Net_Ping \
    TEST_PING_HOST TEST_PING6_HOST
export NO_NETWORK_TESTING=1
make test

%files
%doc Changes README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.76-521
- Prepare for Oreon 11 (RP1)
