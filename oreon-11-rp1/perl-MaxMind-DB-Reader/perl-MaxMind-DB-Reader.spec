%global source0_hash 3820078f9c967f9a88721ea40ca05e4999c1c5301bebc1d119060f9ed5ce39a9

# Perform optional tests
%bcond_without perl_MaxMind_DB_Reader_enables_optional_test

# Math::Int128 is not available on 32-bit platforms
%define enable_int128 0
%if %{with perl_MaxMind_DB_Reader_enables_optional_test}
%ifnarch %{ix86} %{arm}
%define enable_int128 1
%endif
%endif

# No ELF executables packaged.
%global debug_package %{nil}

Name:           perl-MaxMind-DB-Reader
Version:        1.000014
Release:        18%{?dist}
Summary:        Read MaxMind database files and look up IP addresses
# lib/MaxMind/DB/Reader.pm: Artistic-2.0
# LICENSE:      Artistic-2.0 text
# Makefile.PL:  Artistic-2.0
# maxmind-db/LICENSE:   CC-BY-SA-3.0
## Not in any binary package
# maxmind-db/MaxMind-DB-spec.md:    CC-BY-SA-3.0
SourceLicense:  Artistic-2.0 AND CC-BY-SA-3.0
License:        Artistic-2.0
URL:            https://metacpan.org/release/MaxMind-DB-Reader
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAXMIND/MaxMind-DB-Reader-%{version}.tar.gz
# Do not use /bin/env in the shebangs
Patch0:         MaxMind-DB-Reader-1.000014-Normalize-shebangs.patch
# Keep fullarch. ifnarch condition does not work on noarch because it consults
# a target architecture.
#BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(autodie)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::IEEE754)
BuildRequires:  perl(Data::Printer)
BuildRequires:  perl(Data::Validate::IP) >= 0.25
BuildRequires:  perl(Encode)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(List::AllUtils)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(MaxMind::DB::Common) >= 0.040001
BuildRequires:  perl(MaxMind::DB::Metadata)
BuildRequires:  perl(MaxMind::DB::Role::Debugs)
BuildRequires:  perl(MaxMind::DB::Types)
BuildRequires:  perl(Module::Implementation)
BuildRequires:  perl(Moo) >= 1.003000
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::StrictConstructor)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Role::Tiny) >= 1.003002
BuildRequires:  perl(Socket) >= 1.87
# Optional run-time:
BuildRequires:  perl(DateTime)
# Tests:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Path::Class) >= 0.27
BuildRequires:  perl(Scalar::Util) >= 1.42
BuildRequires:  perl(Test::Bits)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::MaxMind::DB::Common::Data)
BuildRequires:  perl(Test::MaxMind::DB::Common::Util)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Number::Delta)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(utf8)
%if %{enable_int128}
# Optional tests:
BuildRequires:  perl(Math::Int128)
BuildRequires:  perl(Net::Works::Network) >= 0.21
%endif
Recommends:     perl(DateTime)
Suggests:       perl(MaxMind::DB::Reader::XS) >= 1.000003

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$
# Filter private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::MaxMind::DB::Reader
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Test::MaxMind::DB::Reader

%description
This module provides a low-level interface to the MaxMind database file format
<http://maxmind.github.io/MaxMind-DB/>.

%package tests
Summary:        Tests for %{name}
License:        Artistic-2.0 AND CC-BY-SA-3.0
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{enable_int128}
# Math::Int128 autodetected
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
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}/maxmind-db
cp -a t %{buildroot}%{_libexecdir}/%{name}
cp -a maxmind-db/test-data %{buildroot}%{_libexecdir}/%{name}/maxmind-db
rm %{buildroot}%{_libexecdir}/%{name}/maxmind-db/test-data/write-test-data.pl
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes eg CONTRIBUTING.md README.md
%{_bindir}/mmdb-dump-metadata
%{_bindir}/mmdb-dump-search-tree
%dir %{perl_vendorlib}/MaxMind
%dir %{perl_vendorlib}/MaxMind/DB
%{perl_vendorlib}/MaxMind/DB/Reader
%{perl_vendorlib}/MaxMind/DB/Reader.pm
%{_mandir}/man3/MaxMind::DB::Reader.*

%files tests
%license maxmind-db/LICENSE
%{_libexecdir}/%{name}

%changelog
%autochangelog
