# Perform optional tests
%bcond_without perl_Convert_ASN1_enables_optional_test

Summary:        ASN.1 encode/decode library
Name:           perl-Convert-ASN1
Version:        0.34
Release:        7%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Convert-ASN1
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TIMLEGGE/Convert-ASN1-%{version}.tar.gz
# Allow running tests from a read-only location,
# <https://github.com/gbarr/perl-Convert-ASN1/pull/40>
Patch0:         Convert-ASN1-0.27-Use-temporary-output-files-for-tests.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.4
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
# Optional run-time:
BuildRequires:  perl(bytes)
# Tests:
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(Math::BigInt) >= 1.997
BuildRequires:  perl(Test::More) >= 0.90
%if %{with perl_Convert_ASN1_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Data::Dumper)
%endif
Suggests:       perl(bytes)
Requires:       perl(Carp)
Requires:       perl(Encode)
Requires:       perl(POSIX)
Requires:       perl(Time::Local)
Requires:       perl(utf8)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Math::BigInt\\)$

%description
Convert::ASN1 encodes and decodes ASN.1 data structures using BER/DER rules.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Math::BigInt) >= 1.997
%if %{with perl_Convert_ASN1_enables_optional_test}
# Optional tests:
Requires:       perl(Data::Dumper)
%endif

%description tests
Tests from %{name}-%{version}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Convert-ASN1-%{version}

# Help file to recognise the Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
unset YYDEBUG
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc ChangeLog OldChanges README.md examples/
%{perl_vendorlib}/Convert/
%{_mandir}/man3/Convert::ASN1*.3pm*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.34-7
- Prepare for Oreon 11 (RP1)
