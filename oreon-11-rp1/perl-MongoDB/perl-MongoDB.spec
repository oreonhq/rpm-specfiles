%global source0_hash 201935f92dac94f39c35de73661e8b252439e496f228657db85ff93257c3268f
%bcond_without perl_MongoDB_enables_server_test
Name:           perl-MongoDB
Version:        2.2.2
Release:        1%{?dist}
Summary:        MongoDB driver for Perl
License:        Apache-2.0 AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/MongoDB
Source0:        https://cpan.metacpan.org/authors/id/M/MO/MONGODB/MongoDB-v%{version}.tar.gz
Patch0:         MongoDB-v2.2.0-Revert-PERL-715-Force-localhost-to-connect-via-IPv4.patch
Patch1:         MongoDB-v2.0.0-Remove-build-dependency-on-ExtUtils-HasCompiler.patch
Patch2:         MongoDB-v2.2.0-Disable-retrying-connect-in-tests.patch
BuildArch:      noarch
%if %{with perl_MongoDB_enables_server_test}
%endif
Suggests:       perl(Authen::SASL)
Requires:       perl(Authen::SASL::SASLprep)
Requires:       perl(Authen::SCRAM::Client) >= 0.011
Requires:       perl(BSON) >= 1.12.0
Requires:       perl(BSON::Code)
Requires:       perl(BSON::DBRef)
Requires:       perl(BSON::Regex)
Requires:       perl(IO::Socket::IP) >= 0.32
Requires:       perl(IO::Socket::SSL) >= 1.42
Requires:       perl(Moo) >= 2
Requires:       perl(Mozilla::CA)
Requires:       perl(Net::DNS)
Requires:       perl(Net::SSLeay) >= 1.49
ExcludeArch:    ppc %{sparc} s390
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((boolean|Moo)\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(BSON\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  mongodb-server
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(BSON)
BuildRequires:  perl(BSON::Bytes)
BuildRequires:  perl(BSON::Code)
BuildRequires:  perl(BSON::DBRef)
BuildRequires:  perl(BSON::Decimal128)
BuildRequires:  perl(BSON::OID)
BuildRequires:  perl(BSON::Raw)
BuildRequires:  perl(BSON::Regex)
BuildRequires:  perl(BSON::Time)
BuildRequires:  perl(BSON::Timestamp)
BuildRequires:  perl(BSON::Types)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cpanel::JSON::XS)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(JSON::Tiny)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sub::Defer)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Time::Moment)
BuildRequires:  perl(Type::Library)
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(Types::Serialiser)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(UUID::URandom)
BuildRequires:  perl(boolean)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

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
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
