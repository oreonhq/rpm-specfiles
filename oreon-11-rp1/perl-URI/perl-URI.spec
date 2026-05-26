# Support isbn URN via Business::ISBN that needs gd library
%if 0%{?rhel} || 0%{?oreon}
%bcond_with perl_URI_enables_Business_ISBN
%bcond_with perl_URI_enables_Regexp_IPv6
%else
%bcond_without perl_URI_enables_Business_ISBN
%bcond_without perl_URI_enables_Regexp_IPv6
%endif

Name:           perl-URI
Version:        5.34
Release:        3%{?dist}
Summary:        A Perl module implementing URI parsing and manipulation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/URI
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/URI-5.34.tar.gz
# oreon url source checksums begin
%global source0_sha256 de64c779a212ff1821896c5ca2bb69e74767d2674cee411e777deea7a22604a8
%global source0_file URI-5.34.tar.gz
# oreon url source checksums end

BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(integer)
BuildRequires:  perl(MIME::Base32)
BuildRequires:  perl(MIME::Base64) >= 2
BuildRequires:  perl(Net::Domain)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::Warnings)
# Optional Tests
# Geo::Point not (yet) available in Fedora
#BuildRequires:  perl(Geo::Point)
# Dependencies
Requires:       perl(Cwd)
Requires:       perl(Data::Dumper)
Requires:       perl(Encode)
Requires:       perl(MIME::Base64) >= 2
Requires:       perl(Net::Domain)
Requires:       perl(utf8)

# Optional Functionality
%if %{with perl_URI_enables_Business_ISBN}
# Business::ISBN pulls in gd and X libraries for barcode support, hence this soft dependency (#1380152)
# Business::ISBN → Test::Pod → Pod::Simple → HTML::Entities (HTML::Parser) → URI
%if 0%{!?perl_bootstrap:1}
BuildRequires:  perl(Business::ISBN) >= 3.005
%endif
Suggests:       perl(Business::ISBN) >= 3.005
%endif
%if %{with perl_URI_enables_Regexp_IPv6}
BuildRequires:  perl(Regexp::IPv6) >= 0.03
Suggests:       perl(Regexp::IPv6) >= 0.03
%endif

# URI::ws incorporated into URI dist at version 5.34
# rhbz#2411728, rhbz#2411834
Obsoletes:      perl-URI-ws < 0.03-32
Provides:       perl-URI-ws = %{version}-%{release}

%description
This module implements the URI class. Objects of this class represent
"Uniform Resource Identifier references" as specified in RFC 2396 (and
updated by RFC 2732).

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_URI_enables_Business_ISBN}
Requires:       perl(Business::ISBN) >= 3.005
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/URI-5.34.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "de64c779a212ff1821896c5ca2bb69e74767d2674cee411e777deea7a22604a8" || { echo "oreon: Source0 SHA256 mismatch for URI-5.34.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n URI-%{version}
chmod -c 644 uri-test

for F in t/*.t t/*.pl; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done


%build
perl Makefile.PL INSTALLDIRS=perl NO_PACKLIST=true NO_PERLLOCAL=true
%{make_build}

%install
%{make_install}

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
perl -i -pe 's{(urls.sto)}{/tmp/$1}' %{buildroot}%{_libexecdir}/%{name}/t/storable.t
perl -i -pe 's{(urls.sto)}{/tmp/$1}' %{buildroot}%{_libexecdir}/%{name}/t/storable-test.pl
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%{_fixperms} -c %{buildroot}

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.md README uri-test
%{perl_privlib}/URI.pm
%{perl_privlib}/URI/
%{_mandir}/man3/URI.3*
%{_mandir}/man3/URI::Escape.3*
%{_mandir}/man3/URI::Heuristic.3*
%{_mandir}/man3/URI::QueryParam.3*
%{_mandir}/man3/URI::Split.3*
%{_mandir}/man3/URI::URL.3*
%{_mandir}/man3/URI::WithBase.3*
%{_mandir}/man3/URI::_punycode.3*
%{_mandir}/man3/URI::icap.3*
%{_mandir}/man3/URI::icaps.3*
%{_mandir}/man3/URI::data.3*
%{_mandir}/man3/URI::file.3*
%{_mandir}/man3/URI::geo.3*
%{_mandir}/man3/URI::ldap.3*
%{_mandir}/man3/URI::otpauth.3*
%{_mandir}/man3/URI::smb.3*
%{_mandir}/man3/URI::ws.3*
%{_mandir}/man3/URI::wss.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.34-3
- Import
