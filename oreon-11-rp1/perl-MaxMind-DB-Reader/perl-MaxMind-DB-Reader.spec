%global source0_hash 3820078f9c967f9a88721ea40ca05e4999c1c5301bebc1d119060f9ed5ce39a9
%bcond_without perl_MaxMind_DB_Reader_enables_optional_test
%define enable_int128 0
%if %{with perl_MaxMind_DB_Reader_enables_optional_test}
%ifnarch %{ix86} %{arm}
%define enable_int128 1
%endif
%endif
%global debug_package %{nil}
Name:           perl-MaxMind-DB-Reader
Version:        1.000014
Release:        18%{?dist}
Summary:        Read MaxMind database files and look up IP addresses
SourceLicense:  Artistic-2.0 AND CC-BY-SA-3.0
License:        Artistic-2.0
URL:            https://metacpan.org/release/MaxMind-DB-Reader
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAXMIND/MaxMind-DB-Reader-%{version}.tar.gz
Patch0:         MaxMind-DB-Reader-1.000014-Normalize-shebangs.patch
%if %{enable_int128}
%endif
Recommends:     perl(DateTime)
Suggests:       perl(MaxMind::DB::Reader::XS) >= 1.000003
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::MaxMind::DB::Reader
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Test::MaxMind::DB::Reader
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::IEEE754)
BuildRequires:  perl(Data::Printer)
BuildRequires:  perl(Data::Validate::IP)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(List::AllUtils)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Math::Int128)
BuildRequires:  perl(MaxMind::DB::Common)
BuildRequires:  perl(MaxMind::DB::Metadata)
BuildRequires:  perl(MaxMind::DB::Role::Debugs)
BuildRequires:  perl(MaxMind::DB::Types)
BuildRequires:  perl(Module::Implementation)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::StrictConstructor)
BuildRequires:  perl(Net::Works::Network)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::Bits)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::MaxMind::DB::Common::Data)
BuildRequires:  perl(Test::MaxMind::DB::Common::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Number::Delta)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(autodie)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides a low-level interface to the MaxMind database file format
<http://maxmind.github.io/MaxMind-DB/>.

%package tests
Summary:        Tests for %{name}
License:        Artistic-2.0 AND CC-BY-SA-3.0
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{enable_int128}
Requires:       perl(Net::Works::Network) >= 0.21
%endif
Requires:       perl(Test::More) >= 0.96
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n MaxMind-DB-Reader-%{version}
chmod -x eg/*
# Help generators to recognize Perl scripts
for F in $(find t -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done
%if !%{enable_int128}
rm t/MaxMind/DB/Reader-decoder.t
perl -i -ne 'print $_ unless m{\A\Qt/MaxMind/DB/Reader-decoder.t\E}' MANIFEST
%endif

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}/maxmind-db
cp -a t %{buildroot}%{_libexecdir}/%{name}
cp -a maxmind-db/test-data %{buildroot}%{_libexecdir}/%{name}/maxmind-db
rm %{buildroot}%{_libexecdir}/%{name}/maxmind-db/test-data/write-test-data.pl
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-MaxMind-DB-Reader-tests -f %{oreon_filedir}/perl-MaxMind-DB-Reader-tests.list

%changelog

%autochangelog
