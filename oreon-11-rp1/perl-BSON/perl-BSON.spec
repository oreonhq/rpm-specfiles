%global source0_hash f4612c0c354310741b99ab6d26451226823150ca27109b1b391232d5cfdda6db
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond_without perl_BSON_enables_optional_test
Name:           perl-BSON
Version:        1.12.2
Release:        19%{?dist}
Summary:        BSON serialization and deserialization
License:        Apache-2.0
URL:            https://metacpan.org/release/BSON
Source0:        https://cpan.metacpan.org/authors/id/M/MO/MONGODB/BSON-v%{version}.tar.gz
Patch0:         BSON-v1.12.2-Fix-an-operator-preference.patch
Patch1:         BSON-v1.12.2-Adapt-tests-to-perl-5.41.7.patch
BuildArch:      noarch
%if %{with perl_BSON_enables_optional_test}
%if !%{defined perl_bootstrap}
%endif
%endif
Requires:       perl(DateTime)
Requires:       perl(DateTime::Tiny)
Suggests:       perl(Mango::BSON::Time)
Requires:       perl(re)
Requires:       perl(Time::Local)
Requires:       perl(Time::Moment)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((CleanEnv|CorpusTest|TestTie|TestUtils)\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((CleanEnv|PPSubclass)\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Tiny)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Math::Int64)
BuildRequires:  perl(MongoDB)
BuildRequires:  perl(MongoDB::BSON::Binary)
BuildRequires:  perl(MongoDB::BSON::Regexp)
BuildRequires:  perl(MongoDB::Code)
BuildRequires:  perl(MongoDB::DBRef)
BuildRequires:  perl(MongoDB::OID)
BuildRequires:  perl(MongoDB::Timestamp)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(Time::Moment)
BuildRequires:  perl(base)
BuildRequires:  perl(boolean)
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(mro)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(overload)
BuildRequires:  perl(re)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Perl class implements a BSON encoder and decoder. It consumes
documents (typically hash references) and emits BSON strings and vice
versa in accordance with the BSON specification <http://bsonspec.org/>.

Upstream claims it will stop supporting this code on 2020-08-13.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_BSON_enables_optional_test}
Requires:       perl(Math::Int64)
%if !%{defined perl_bootstrap}
Requires:       perl(MongoDB)
Requires:       perl(MongoDB::BSON::Binary)
Requires:       perl(MongoDB::BSON::Regexp)
Requires:       perl(MongoDB::Code)
Requires:       perl(MongoDB::DBRef) >= 1.0.0
Requires:       perl(MongoDB::OID)
Requires:       perl(MongoDB::Timestamp)
%endif
Requires:       perl(Test::Exception)
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n BSON-v%{version}
# Help generators to recognize Perl scripts
for F in t/*.t t/*/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a corpus t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/corpus/*.pl
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
unset AUTHOR_TESTING AUTOMATED_TESTING BSON_EXTJSON BSON_EXTJSON_RELAXED \
    BSON_TEST_SORT_HASH HARNESS_PERL_SWITCHES PERL_BSON_BACKEND \
    PERL_MONGO_NO_DEP_WARNINGS
cd %{_libexecdir}/%{name} && exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset AUTHOR_TESTING AUTOMATED_TESTING BSON_EXTJSON BSON_EXTJSON_RELAXED \
    BSON_TEST_SORT_HASH HARNESS_PERL_SWITCHES PERL_BSON_BACKEND \
    PERL_MONGO_NO_DEP_WARNINGS
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-BSON-tests -f %{oreon_filedir}/perl-BSON-tests.list

%changelog

%autochangelog
