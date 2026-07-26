%global source0_hash 201935f92dac94f39c35de73661e8b252439e496f228657db85ff93257c3268f

# Perform tests that use a MongoDB server
%if !(0%{?fedora} < 30)
%bcond_with perl_MongoDB_enables_server_test
%else
%bcond_without perl_MongoDB_enables_server_test
%endif

Name:           perl-MongoDB
Version:        2.2.2
Release:        16%{?dist}
Summary:        MongoDB driver for Perl
## Installed:
# lib/MongoDB/_Link.pm:             Apache-2.0 AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
# Other files:                      Apache-2.0
## Not used:
# inc/CheckJiraInChanges.pm:        Apache-2.0
# inc/ExtUtils/HasCompiler.pm:      GPL-1.0-or-later OR Artistic-1.0-Perl
License:        Apache-2.0 AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/MongoDB
Source0:        https://cpan.metacpan.org/authors/id/M/MO/MONGODB/MongoDB-v%{version}.tar.gz
# Revert "localhost is IPv4 only" <https://jira.mongodb.org/browse/PERL-715>
Patch0:         MongoDB-v2.2.0-Revert-PERL-715-Force-localhost-to-connect-via-IPv4.patch
# Remove useless dependency on ExtUtils::HasCompiler
Patch1:         MongoDB-v2.0.0-Remove-build-dependency-on-ExtUtils-HasCompiler.patch
# Skip tests on an unreachable server immediately
Patch2:         MongoDB-v2.2.0-Disable-retrying-connect-in-tests.patch
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(warnings)
# Runtime:
# Authen::SASL::SASLprep not used at tests
# Authen::SCRAM::Client 0.011 not used at tests
BuildRequires:  perl(boolean) >= 0.25
BuildRequires:  perl(BSON) >= 1.12.0
BuildRequires:  perl(BSON::Bytes)
BuildRequires:  perl(BSON::Code)
BuildRequires:  perl(BSON::DBRef)
BuildRequires:  perl(BSON::OID)
BuildRequires:  perl(BSON::Raw)
BuildRequires:  perl(BSON::Regex)
BuildRequires:  perl(BSON::Time)
BuildRequires:  perl(BSON::Timestamp)
BuildRequires:  perl(BSON::Types)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(if)
BuildRequires:  perl(IO::Socket)
# Prefer IO::Socket::IP over IO::Socket::INET
BuildRequires:  perl(IO::Socket::IP) >= 0.32
# IO::Socket::SSL 1.42 not used at tests
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Moo) >= 2
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(namespace::clean)
# Net::DNS not used at tests
# Net::SSLeay 1.49 not used at tests
BuildRequires:  perl(overload)
# re used only with perl 5.10.0
BuildRequires:  perl(Safe::Isa) >= 1.000007
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Sub::Defer)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Type::Library)
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(UUID::URandom)
BuildRequires:  perl(version)
# Optional runtime:
# Authen::SASL not used at tests
# Mozilla::CA no used at tests
# Tests only:
%if %{with perl_MongoDB_enables_server_test}
BuildRequires:  mongodb-server
%endif
BuildRequires:  perl(BSON::Decimal128) >= 1
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(JSON::MaybeXS)
# Log::Any::Adapter used only if MONGOVERBOSE environment variable is true
BuildRequires:  perl(Path::Tiny) >= 0.058
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Deep) >= 0.111
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(utf8)
# Optional tests:
# CPAN::Meta not useful
BuildRequires:  perl(Cpanel::JSON::XS)
BuildRequires:  perl(JSON::Tiny)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Test::Harness) >= 3.31
BuildRequires:  perl(Time::Moment) >= 0.22
BuildRequires:  perl(Types::Serialiser)
Suggests:       perl(Authen::SASL)
Requires:       perl(Authen::SASL::SASLprep)
Requires:       perl(Authen::SCRAM::Client) >= 0.011
Requires:       perl(BSON) >= 1.12.0
Requires:       perl(BSON::Code)
Requires:       perl(BSON::DBRef)
Requires:       perl(BSON::Regex)
# Prefer IO::Socket::IP over IO::Socket::INET
Requires:       perl(IO::Socket::IP) >= 0.32
Requires:       perl(IO::Socket::SSL) >= 1.42
Requires:       perl(Moo) >= 2
# Hard-require Mozilla::CA to becase we hard-require IO::Socket::SSL
Requires:       perl(Mozilla::CA)
Requires:       perl(Net::DNS)
Requires:       perl(Net::SSLeay) >= 1.49

# Mongodb must run on a 32-bit little-endian or 64-bit any-endian CPU
# (see bug #630898)
ExcludeArch:    ppc %{sparc} s390

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((boolean|Moo)\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(BSON\\)

%description
This is a Perl client for accessing MongoDB servers.

Upstream claims it will drop support for this code on 2020-08-13.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n MongoDB-v%{version}
# Remove bundled modules
rm -r inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
%if %{with perl_MongoDB_enables_server_test}
mkdir test_db
mongod --fork --logpath $PWD/mongod.log --pidfilepath $PWD/mongod.pid \
    --dbpath $PWD/test_db/ --smallfiles || test_rc=$?
if [ -n "$test_rc" ]; then
    printf "Error: Could not start mongod server\n"
    cat mongod.log
    exit 1
fi
unset MONGOD MONGOVERBOSE TEST_MONGO_SOCKET_HOST
export FAILPOINT_TESTING=1
%else
export FAILPOINT_TESTING=0
%endif
make test || test_rc=$?
%if %{with perl_MongoDB_enables_server_test}
kill `cat mongod.pid`
cat mongod.log
%endif
exit $test_rc

%files
%license LICENSE
%doc Changes CONTRIBUTING.md README
%{perl_vendorlib}/MongoDB
%{perl_vendorlib}/MongoDB.pm
%{_mandir}/man3/MongoDB.*
%{_mandir}/man3/MongoDB::*

%changelog
%autochangelog
