%global source0_hash 91135da48dd97fdbb40ea33306a008a2eae35ac5e3fae15fd420beab106b1e7a

# Enable rendering ISBN into PNG barcodes with GD library
%if 0%{?rhel} >= 9
%bcond_with perl_Business_ISBN_enables_PNG
%else
%bcond_without perl_Business_ISBN_enables_PNG
%endif

Name:           perl-Business-ISBN
%global cpan_version 3.014
Version:        %(echo '%{cpan_version}' | tr '_' '.'})
Release:        1%{?dist}
Summary:        Perl module to work with International Standard Book Numbers

License:        Artistic-2.0
URL:            https://metacpan.org/release/Business-ISBN
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRIANDFOY/Business-ISBN-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::MM_Any)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test::Manifest 1.21 is optional
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Business::ISBN::Data) >= 20230322.001
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(subs)
BuildRequires:  perl(vars)
%if %{with perl_Business_ISBN_enables_PNG}
# Optional run-time:
BuildRequires:  perl(GD::Barcode::EAN13)
%endif
# Tests:
BuildRequires:  perl(Test::More) >= 0.95
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
%if %{with perl_Business_ISBN_enables_PNG}
Recommends:     perl(GD::Barcode::EAN13)
%endif

Provides:       perl(Business::ISBN)
%description
This modules handles International Standard Book Numbers, including
ISBN-10 and ISBN-13.

For exporting ISBN into a bar code, with png_barcode(), you need to install
GD::Barcode::EAN13 Perl module.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Business-ISBN-%{cpan_version}

# Help generators to recognize Perl scripts
for F in `find t -name *.t`; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Remove release tests
rm %{buildroot}%{_libexecdir}/%{name}/t/pod*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README.pod SECURITY.md
%{perl_vendorlib}/Business*
%{_mandir}/man3/Business::ISBN*.3*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
