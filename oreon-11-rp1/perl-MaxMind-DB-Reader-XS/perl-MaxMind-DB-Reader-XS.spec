%global source0_hash aa6fb87fed19d549f29b135de7997ee92b1227d626cb0e890600a91cadc3053a
%bcond_without perl_MaxMind_DB_Reader_XS_enables_optional_test
Name:           perl-MaxMind-DB-Reader-XS
Version:        1.000009
Release:        1%{?dist}
Summary:        Fast XS implementation of MaxMind DB reader
License:        Artistic-2.0 AND (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/MaxMind-DB-Reader-XS
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAXMIND/MaxMind-DB-Reader-XS-%{version}.tar.gz
Patch0:         MaxMind-DB-Reader-XS-1.000008-Do-not-hardcode-debugging.patch
Patch1:         MaxMind-DB-Reader-XS-1.000009-Do-not-call-MMDB_free_entry_data_list-on-libmaxmindd.patch
ExcludeArch:    %{arm} %{ix86}
%if %{with perl_MaxMind_DB_Reader_XS_enables_optional_test}
%endif
Requires:       perl(MaxMind::DB::Reader::Role::HasMetadata)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::MaxMind::DB::Reader\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Test::MaxMind::DB::Reader\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  libmaxminddb-devel
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Config)
BuildRequires:  perl(Config::AutoConf)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Math::Int128)
BuildRequires:  perl(Math::Int64)
BuildRequires:  perl(MaxMind::DB::Metadata)
BuildRequires:  perl(MaxMind::DB::Reader)
BuildRequires:  perl(MaxMind::DB::Reader::Role::HasMetadata)
BuildRequires:  perl(MaxMind::DB::Types)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Implementation)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Net::Works::Network)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::MaxMind::DB::Common::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Number::Delta)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(autodie)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Simply installing this module causes MaxMind::DB::Reader to use the XS
implementation, which is much faster than the Perl implementation.

This Perl module is deprecated and will only receive fixes for major bugs and
security vulnerabilities. New features and functionality will not be added.

%package tests
Summary:        Tests for %{name}
License:        Artistic-2.0 AND CC-BY-SA-3.0
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.96
%if %{with perl_MaxMind_DB_Reader_XS_enables_optional_test}
Requires:       perl(Net::Works::Network) >= 0.21
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n MaxMind-DB-Reader-XS-%{version}
# Remove bundled modules
rm -r ./inc
perl -i -ne 'print $_ unless m{\Ainc/}' MANIFEST
# Remove an unused script we do not want to package because its dependencies
# are not available
rm maxmind-db/test-data/write-test-data.pl
perl -i -ne 'print $_ unless m{\Amaxmind-db/test-data/write-test-data.pl}' MANIFEST
# Help generators to recognize Perl scripts
for F in $(find -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a maxmind-db t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-MaxMind-DB-Reader-XS-tests -f %{oreon_filedir}/perl-MaxMind-DB-Reader-XS-tests.list

%changelog

%autochangelog
