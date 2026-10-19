%global source0_hash 72c2a5956e1ecf108b6646fd5dd4a033809a044964133057333eaa675fbbbe04
%global cassandra_available 0
Name:           perl-Cassandra-Client
Version:        0.21
Release:        4%{?dist}
Summary:        Perl library for accessing Cassandra using its binary network protocol
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Cassandra-Client
Source0:        https://cpan.metacpan.org/authors/id/T/TV/TVDW/Cassandra-Client-%{version}.tar.gz
Patch0:         https://sources.debian.org/data/main/libc/libcassandra-client-perl/0.20-1~bpo12%2B1/debian/patches/remove-Sub%3A%3ACurrent.patch
%if 0%{cassandra_available}
%endif
Requires:       perl(AnyEvent)
Requires:       perl(EV) >= 4
Requires:       perl(Math::BigInt)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(AnyEvent::XSPromises)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Devel::GlobalDestruction)
BuildRequires:  perl(EV)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::INET6)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Net::SSLeay)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(constant)
BuildRequires:  perl(feature)
BuildRequires:  perl(if)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Cassandra::Client is a Perl library giving its users access to the
Cassandra database, through the native protocol. Both synchronous and
asynchronous querying is supported, through various common calling styles.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Cassandra-Client-%{version}
%patch -P0 -p1

# All these tests require a cassandra server
%if ! 0%{cassandra_available}
rm \
  t/01-connect.t \
  t/02-sync-basic-crud.t \
  t/04-batch.t \
  t/05-no-metadata.t \
  t/07-named-parameters.t \
  t/08-retries.t \
  t/10-queue.t \
  t/20-memleak.t \
  t/40-multiple-async-queries-response.t \
  t/50-bench.t \
  t/99-long-loop.t
%endif

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

unset AUTHOR_TESTING
unset BENCHMARK
unset CASSANDRA_HOST
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
