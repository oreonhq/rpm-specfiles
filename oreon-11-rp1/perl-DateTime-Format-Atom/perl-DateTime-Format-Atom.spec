%global source0_hash 6aa649aeb710e0489ed5b71ff15694713bb3045e7cf877674ede50f8d5f7f302

# Perform optional tests
%bcond_without perl_DateTime_Format_Atom_enables_optional_test

Name:           perl-DateTime-Format-Atom
Version:        1.8.0
Release:        4%{?dist}
Summary:        Parse and format Atom date-time strings
License:        CC0-1.0
URL:            https://metacpan.org/release/DateTime-Format-Atom
Source0:        https://cpan.metacpan.org/authors/id/I/IK/IKEGAMI/DateTime-Format-Atom-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(constant)
BuildRequires:  perl(DateTime::Format::RFC3339)
BuildRequires:  perl(version)
# Tests:
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Test::More)
%if %{with perl_DateTime_Format_Atom_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.22
%endif
Requires:       perl(:VERSION) >= 5.10

%description
This Perl module understands the Atom date/time format, an ISO 8601 profile,
defined at <http://tools.ietf.org/html/rfc4287>.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DateTime-Format-Atom-v%{version}
# Remove always skipped tests
for F in t/01_devel_mark_check.t t/02_devel_version_check.t \
        t/03_devel_whitespace.t t/04_devel_permissions.t \
        t/06_devel_pod_coverage.t \
%if %{without perl_DateTime_Format_Atom_enables_optional_test}
        t/05_pod.t \
%endif
;do
    rm -- "$F"
    perl -i -ne 'print $_ unless m{\A\Q'"$F"'\E\Z}' MANIFEST
done
# Correct shebangs
for F in t/*.t; do
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
%if %{with perl_DateTime_Format_Atom_enables_optional_test}
rm %{buildroot}%{_libexecdir}/%{name}/t/05_pod.t
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset DEVEL_TESTS
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE.txt
%doc Changes README.txt
%dir %{perl_vendorlib}/DateTime
%dir %{perl_vendorlib}/DateTime/Format
%{perl_vendorlib}/DateTime/Format/Atom.pm
%{_mandir}/man3/DateTime::Format::Atom.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
