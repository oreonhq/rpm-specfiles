# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ef5d2ef099a1a24a6e83ffe543de73337805d3d39c00b84fa205d725ad1a1b63
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%if 0%{?rhel} || 0%{?oreon}
%bcond_with perl_URI_enables_Business_ISBN
%bcond_with perl_URI_enables_Regexp_IPv6
%else
%bcond_without perl_URI_enables_Business_ISBN
%bcond_without perl_URI_enables_Regexp_IPv6
%endif

Name:           perl-URI
Version:        5.40
Release:        1%{?dist}
Summary:        A Perl module implementing URI parsing and manipulation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/URI
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/URI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: oreon-rpm-macros
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
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
BuildRequires:  perl(Unicode::Normalize)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::Warnings)
Requires:       perl(Cwd)
Requires:       perl(Data::Dumper)
Requires:       perl(Encode)
Requires:       perl(MIME::Base64) >= 2
Requires:       perl(Net::Domain)
Requires:       perl(utf8)

%if %{with perl_URI_enables_Business_ISBN}
%if 0%{!?perl_bootstrap:1}
BuildRequires:  perl(Business::ISBN) >= 3.005
%endif
Suggests:       perl(Business::ISBN) >= 3.005
%endif
%if %{with perl_URI_enables_Regexp_IPv6}
BuildRequires:  perl(Regexp::IPv6) >= 0.03
Suggests:       perl(Regexp::IPv6) >= 0.03
%endif

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

%global __provides_exclude ^perl\\(URI::_foreign\\)$

%prep
%oreon_sha256
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

mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
perl -i -pe 's{(urls.sto)}{/tmp/$1}' %{buildroot}%{_libexecdir}/%{name}/t/storable.t
perl -i -pe 's{(urls.sto)}{/tmp/$1}' %{buildroot}%{_libexecdir}/%{name}/t/storable-test.pl
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
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
%autochangelog
