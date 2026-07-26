%global source0_hash 090542a8eee9bd3c12e59c4b65624c89d01ffd94204f1f076a1db40b26c09834

Name:           perl-GeoIP2
Version:        2.006002
Release:        18%{?dist}
Summary:        Perl API for MaxMind's GeoIP2 web services and databases
# lib/GeoIP2.pm:                GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/GeoIP2/Model/Country.pm:  GPL-1.0-or-later OR Artistic-1.0-Perl
# LICENSE:                      GPL-1.0-or-later OR Artistic-1.0-Perl
# maxmind-db/LICENSE:               CC-BY-SA-3.0
# maxmind-db/MaxMind-DB-spec.md:    CC-BY-SA-3.0
# README.md:                    GPL-1.0-or-later OR Artistic-1.0-Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/GeoIP2
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAXMIND/GeoIP2-%{version}.tar.gz
# Drop an insecure "use lib", <https://github.com/maxmind/GeoIP2-perl/pull/77>
Patch0:         GeoIP2-2.006002-Do-not-use-lib-from-web-service-request-tool.patch
# Do not use /usr/bin/env in the shebangs
Patch1:         GeoIP2-2.006002-Normalize-a-shebang.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(B)
# Data::Dumper not used at tests
BuildRequires:  perl(Data::Validate::IP) >= 0.25
BuildRequires:  perl(Exporter)
# Getopt::Long not used at tests
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(List::SomeUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MaxMind::DB::Reader) >= 1.000000
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Throwable::Error)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl(lib)
BuildRequires:  perl(MaxMind::DB::Metadata)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Number::Delta)
BuildRequires:  perl(utf8)
Requires:       perl(Throwable::Error)

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)
# Filter private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::GeoIP2\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Test::GeoIP2\\)

%description
This package provides an API for the GeoIP2 web services and databases. The
API also works with the GeoLite2 databases.

%package tests
Summary:        Tests for %{name}
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND CC-BY-SA-3.0
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.96

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n GeoIP2-%{version}
%patch -P0 -p1
%patch -P1 -p1
# Rename web-service-request to a more specific name,
# <https://github.com/maxmind/GeoIP2-perl/issues/78>
mv bin/{,geoip2-}web-service-request
perl -i -pe 's{bin/web-service-request}{bin/geoip2-web-service-request}' \
    Makefile.PL MANIFEST
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
%doc Changes CONTRIBUTING.md README.md
%{_bindir}/geoip2-web-service-request
%{perl_vendorlib}/GeoIP2
%{perl_vendorlib}/GeoIP2.pm
%{_mandir}/man3/GeoIP2.*
%{_mandir}/man3/GeoIP2::*

%files tests
%license maxmind-db/LICENSE
%{_libexecdir}/%{name}

%changelog
%autochangelog
