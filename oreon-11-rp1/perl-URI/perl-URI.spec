%global source0_hash 5a8750ddd8ee743d7cc89bebdd542a9b78a34023164ebe19dea0c248e121c21e
%if 0%{?rhel} || (0%{?oreon} >= 11)
%bcond_with perl_URI_enables_Business_ISBN
%bcond_with perl_URI_enables_Regexp_IPv6
%else
%bcond_without perl_URI_enables_Business_ISBN
%bcond_without perl_URI_enables_Regexp_IPv6
%endif
Name:           perl-URI
Version:        5.37
Release:        1%{?dist}
Summary:        A Perl module implementing URI parsing and manipulation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/URI
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/URI-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Cwd)
Requires:       perl(Data::Dumper)
Requires:       perl(Encode)
Requires:       perl(MIME::Base64) >= 2
Requires:       perl(Net::Domain)
Requires:       perl(utf8)
%if %{with perl_URI_enables_Business_ISBN}
%if 0%{!?perl_bootstrap:1}
%endif
Suggests:       perl(Business::ISBN) >= 3.005
%endif
%if %{with perl_URI_enables_Regexp_IPv6}
Suggests:       perl(Regexp::IPv6) >= 0.03
%endif
Obsoletes:      perl-URI-ws < 0.03-32
Provides:       perl-URI-ws = %{version}-%{release}
Provides:       perl(URI)
Provides:       perl(URI::Escape)
Provides:       perl(URI::URL)
Provides:       perl(URI::_idna)
Provides:       perl(URI::file)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Business::ISBN)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(MIME::Base32)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Net::Domain)
BuildRequires:  perl(Regexp::IPv6)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Unicode::Normalize)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(integer)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-URI-tests -f %{oreon_filedir}/perl-URI-tests.list

%changelog

%autochangelog
