%global source0_hash f4565cb622f8611e4ad2afde480c35980995cb064b7ec52f934ffcc04d83d5e2
Name:           perl-Redis-Fast
Version:        0.37
Release:        6%{?dist}
Summary:        Perl binding for Redis database
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Redis-Fast
Source0:        https://www.cpan.org/modules/by-module/Redis/Redis-Fast-%{version}.tar.gz
Patch0:         perl-Redis-Fast-0.37-unbundle_hiredis.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  hiredis-devel
BuildRequires:  openssl-devel
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(IO::Socket::UNIX)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Module::Build::XSUtil)
BuildRequires:  perl(Net::EmptyPort)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Parallel::ForkManager)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::SharedFork)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(Test::UNIXSock)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  valkey
# /oreon:deps
%description
Redis::Fast is a wrapper around Salvatore Sanfilippo's hiredis C client. It
is compatible with Redis.pm.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Redis-Fast-%{version}
# Drop bundled hiredis
%patch -P0 -p1
rm -vr deps/

%build

perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

unset REDIS_DEBUG
unset REDIS_SERVER
export REDIS_SERVER_PATH=/usr/bin/valkey-server
unset TEST_REDIS_SERVER_SOCK_PATH
unset USE_SSL
./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
