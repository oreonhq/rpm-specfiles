%global source0_hash 280ac87370f553e5fa5dd60e3b5433108b471064a7ee0df784b909a5f2b862c7
%global base_version 2.77
%bcond_without perl_Net_Ping_enables_optional_test
Name:           perl-Net-Ping
Version:        2.77
Release:        1%{?dist}
Summary:        Check a remote host for reachability
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Ping/
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Net-Ping-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Net_Ping_enables_optional_test}
%endif
Requires:       perl(IO::Socket::INET)
Suggests:       perl(Net::Ping::External)
Conflicts:      perl < 4:5.22.0-350
Provides:       perl(Net::Ping)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Net-Ping-%{base_version}
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
unset AUTHOR_TESTING IS_MAINTAINER NET_PING_FAIL_IP PERL_TEST_Net_Ping \
    TEST_PING_HOST TEST_PING6_HOST
export NO_NETWORK_TESTING=1
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset AUTHOR_TESTING IS_MAINTAINER NET_PING_FAIL_IP PERL_TEST_Net_Ping \
    TEST_PING_HOST TEST_PING6_HOST
export NO_NETWORK_TESTING=1
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Net-Ping-tests -f %{oreon_filedir}/perl-Net-Ping-tests.list

%changelog

%autochangelog
