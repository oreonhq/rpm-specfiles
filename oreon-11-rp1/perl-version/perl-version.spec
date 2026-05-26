# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_version_enables_optional_test
%else
%bcond_with perl_version_enables_optional_test
%endif

Name:           perl-version
Epoch:          9
Version:        0.99.33
%global module_version 0.9933
Release:        522%{?dist}
Summary:        Perl extension for Version Objects
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/version
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/version-%{module_version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 dc07d9388ca3d3f67146312904bcdb35fe416bb30056158f80df3281a94fae58
%global source0_file version-0.9933.tar.gz
# oreon url source checksums end
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
# ExtUtils::CBuilder not helpful
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Temp) >= 0.13
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(locale)
BuildRequires:  perl(overload)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(UNIVERSAL)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl(XSLoader)
# Tests only
BuildRequires:  perl(base)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(I18N::Langinfo)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More) >= 0.45
# Optional tests
%if %{with perl_version_enables_optional_test} && ! %{defined perl_bootstrap}
BuildRequires:  perl(Test::Taint)
%endif
Requires:       perl(B)
Requires:       perl(Carp)
Requires:       perl(locale)
Requires:       perl(UNIVERSAL)
Requires:       perl(warnings)
Requires:       perl(XSLoader)

%{?perl_default_filter}
# version::vxs is private module (see bug #633775)
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(version::vxs\\)
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}

%description
Version objects were added to Perl in 5.10. This module implements version
objects for older version of Perl and provides the version object API for
all versions of Perl. All previous releases before 0.74 are deprecated and
should not be used due to incompatible API changes. Version 0.77 introduces
the new 'parse' and 'declare' methods to standardize usage. You are
strongly urged to set 0.77 as a minimum in your code.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(I18N::Langinfo)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/version-0.9933.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "dc07d9388ca3d3f67146312904bcdb35fe416bb30056158f80df3281a94fae58" || { echo "oreon: Source0 SHA256 mismatch for version-0.9933.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n version-%{module_version}

# Help file to recognise the Perl scripts
for F in t/*.t t/survey_locales; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done
perl -MConfig -i -pe 's/\A#!.*perl/$Config{startperl}/' t/*.pm

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" UNINST=0 NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc CHANGES README
%doc %{perl_vendorarch}/version.pod
%dir %{perl_vendorarch}/version/
%doc %{perl_vendorarch}/version/Internals.pod
%{perl_vendorarch}/auto/version/
%{perl_vendorarch}/version.pm
%{perl_vendorarch}/version/vpp.pm
%{perl_vendorarch}/version/vxs.pm
%{perl_vendorarch}/version/regex.pm
%{_mandir}/man3/version.3pm*
%{_mandir}/man3/version::Internals.3pm*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.99.33-522
- Prepare for Oreon 11 (RP1)
