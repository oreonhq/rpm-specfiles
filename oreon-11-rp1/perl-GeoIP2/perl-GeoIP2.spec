%global source0_hash 090542a8eee9bd3c12e59c4b65624c89d01ffd94204f1f076a1db40b26c09834
Name:           perl-GeoIP2
Version:        2.006002
Release:        1%{?dist}
Summary:        Perl API for MaxMind's GeoIP2 web services and databases
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/GeoIP2
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAXMIND/GeoIP2-%{version}.tar.gz
Patch0:         GeoIP2-2.006002-Do-not-use-lib-from-web-service-request-tool.patch
Patch1:         GeoIP2-2.006002-Normalize-a-shebang.patch
BuildArch:      noarch
Requires:       perl(Throwable::Error)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::GeoIP2\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Test::GeoIP2\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(B)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Validate::IP)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(List::SomeUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MaxMind::DB::Metadata)
BuildRequires:  perl(MaxMind::DB::Reader)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Number::Delta)
BuildRequires:  perl(Throwable::Error)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%files -n perl-GeoIP2-tests -f %{oreon_filedir}/perl-GeoIP2-tests.list

%changelog

%autochangelog
