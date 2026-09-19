%global source0_hash 14cb899797212615b4e93f916dcbdafb48d01c5eaab2038fe6cb179bf95c6feb

Name:           perl-Redis
Version:        2.000
Release:        10%{?dist}
Summary:        Perl binding for Redis database
License:        Apache-2.0
URL:            https://metacpan.org/release/Redis
Source0:        https://cpan.metacpan.org/modules/by-module/Redis/Redis-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
# Module
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(IO::Socket::Timeout) >= 0.29
BuildRequires:  perl(IO::Socket::UNIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::StdHash)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(blib)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Net::EmptyPort)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::SharedFork)
BuildRequires:  perl(Test::TCP) >= 1.19
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10
BuildRequires:  valkey
%else
BuildRequires:  redis
%endif
# Author Tests (not run)
#BuildRequires:  perl(Pod::Coverage::TrustPod)
#BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
# Release Tests
BuildRequires:  perl(Test::CPAN::Meta)
# Dependencies
Requires:       perl(IO::Socket::SSL)
Requires:       perl(IO::Socket::Timeout) >= 0.29
Requires:       perl(Time::HiRes)

%description
Pure perl bindings for http://redis.io/

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Redis-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
unset AUTHOR_TESTING PERL_COMPILE_TEST_DEBUG REDIS_DEBUG REDIS_SERVER REDIS_SERVER_PATH
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10
set REDIS_SERVER_PATH=/usr/bin/valkey-server
%endif
RELEASE_TESTING=1 ./Build test

%files
%license LICENSE
%doc Changes README scripts/ tools/
%{perl_vendorlib}/Redis.pm
%{perl_vendorlib}/Redis/
%{_mandir}/man3/Redis.3*
%{_mandir}/man3/Redis::Hash.3*
%{_mandir}/man3/Redis::List.3*
%{_mandir}/man3/Redis::Sentinel.3*

%changelog
%autochangelog
