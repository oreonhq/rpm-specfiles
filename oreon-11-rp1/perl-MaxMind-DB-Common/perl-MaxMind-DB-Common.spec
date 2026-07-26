%global source0_hash 6bc6df4bd36300d07aa4a5f8198ae6694ca7e313c038109c88dbc3a997b21bd7

Name:           perl-MaxMind-DB-Common
Version:        0.040001
Release:        19%{?dist}
Summary:        Code shared by the MaxMind database reader and writer
License:        Artistic-2.0
URL:            https://metacpan.org/release/MaxMind-DB-Common
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAXMIND/MaxMind-DB-Common-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(autodie)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
# Data::Dumper::Concise not used at tests
# DateTime not used at tests
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::AllUtils)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::StrictConstructor)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Quote)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Data::Dumper::Concise)
Requires:       perl(DateTime)

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)

%description
This distribution provides some shared code for use by both the MaxMind
database reader and writer Perl modules.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.96

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MaxMind-DB-Common-%{version}
# Remove tests which are always skipped
for F in t/author-* t/release-*; do
    rm "$F"
    perl -i -ne 'print $_ unless m{\A\Q'"$F"'\E}' MANIFEST
done
# Help generators to recognize Perl scripts
for F in $(find t -type f -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset AUTHOR_TESTING
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README.md
%dir %{perl_vendorlib}/MaxMind
%{perl_vendorlib}/MaxMind/DB
%dir %{perl_vendorlib}/Test
%dir %{perl_vendorlib}/Test/MaxMind
%dir %{perl_vendorlib}/Test/MaxMind/DB
%{perl_vendorlib}/Test/MaxMind/DB/Common
%{_mandir}/man3/MaxMind::DB::Common.*
%{_mandir}/man3/MaxMind::DB::Metadata.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
