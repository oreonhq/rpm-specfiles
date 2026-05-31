%global source0_hash 2794a1aaaeb1d3a287dd2c7286258663796562f7db9ccc6b424bc4f1de8ad014

# Report a difference on string nonequivalnce
%bcond_without perl_Test_Base_enables_diff
# Run extra test
%bcond_without perl_Test_Base_enables_extra_test
# Enable getting documents by URLs
%bcond_without perl_Test_Base_enables_network

Name:           perl-Test-Base
Version:        0.89
Release:        24%{?dist}
Summary:        Data Driven Testing Framework
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Base
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Test-Base-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
%if %{with perl_Test_Base_enables_diff}
BuildRequires:  perl(Algorithm::Diff) >= 1.15
%endif
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Filter::Util::Call)
%if %{with perl_Test_Base_enables_network}
# LWP::Simple not used at tests
%endif
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Scalar::Util) >= 1.07
BuildRequires:  perl(Spiffy) >= 0.40
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.88
%if %{with perl_Test_Base_enables_diff}
BuildRequires:  perl(Text::Diff) >= 0.35
%endif
BuildRequires:  perl(warnings)
BuildRequires:  perl(YAML)
# Test Suite
BuildRequires:  perl(base)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Tester)
%if %{with perl_Test_Base_enables_extra_test}
# Author Tests
BuildRequires:  perl(Test::Pod) >= 1.41
%endif
# Dependencies
%if %{with perl_Test_Base_enables_diff}
Requires:       perl(Algorithm::Diff) >= 1.15
%endif
Requires:       perl(Data::Dumper)
Requires:       perl(File::Path)
Requires:       perl(Filter::Util::Call)
%if %{with perl_Test_Base_enables_network}
Requires:       perl(LWP::Simple)
%endif
Requires:       perl(MIME::Base64)
Requires:       perl(Scalar::Util) >= 1.07
Requires:       perl(Test::Deep)
Requires:       perl(Test::More) >= 0.88
%if %{with perl_Test_Base_enables_diff}
Requires:       perl(Text::Diff) >= 0.35
%endif
Requires:       perl(YAML)

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$
# Remove private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(TestBas
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(TestBas

%description
Testing is usually the ugly part of Perl module authoring. Perl gives you a
standard way to run tests with Test::Harness, and basic testing primitives
with Test::More. After that you are pretty much on your own to develop a
testing framework and philosophy. Test::More encourages you to make your
own framework by subclassing Test::Builder, but that is not trivial.

Test::Base gives you a way to write your own test framework base class that
is trivial.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(lib)
Requires:       perl(strict)
Requires:       perl(Test::Deep)
Requires:       perl(Test::More) >= 0.88
Requires:       perl(Test::Tester)
Requires:       perl(warnings)
Requires:       perl(YAML)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Base-%{version}
# Remove skipped tests
for T in \
    t/get_url.t \
%if %{without perl_Test_Base_enables_extra_test}
    t/author-pod-syntax.t \
%endif
; do
    rm -- "$T"
    perl -i -ne 'print $_ unless m{^\Q'"$T"'\E}' MANIFEST
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_Test_Base_enables_extra_test}
rm %{buildroot}%{_libexecdir}/%{name}/t/author-pod-syntax.t
%endif
# t/000-require-modules.t searches ./lib
rm %{buildroot}%{_libexecdir}/%{name}/t/000-require-modules.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# t/write_file.t writes into CWD and t/xxx.t interferes with "test" file.
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/t "$DIR"
pushd "$DIR"
unset TEST_SHOW_NO_DIFFS
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset TEST_SHOW_NO_DIFFS
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test %{?with_perl_Test_Base_enables_extra_test:AUTHOR_TESTING=1}

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%dir %{perl_vendorlib}/Test
%{perl_vendorlib}/Test/Base
%{perl_vendorlib}/Test/Base.*
%{_mandir}/man3/Test::Base.*
%{_mandir}/man3/Test::Base::*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.89-24
- Prepare for Oreon 11 (RP1)
