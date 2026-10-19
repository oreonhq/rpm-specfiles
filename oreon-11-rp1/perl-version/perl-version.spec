%global source0_hash 9a782d3534c486393e2b190151f6ed64a5083fd76fa142915ae094eb1cc99c04
%bcond_with perl_version_enables_optional_test
Name:           perl-version
Epoch:          9
Version:        0.9934
%global module_version 0.9934
Release:        1%{?dist}
Summary:        Perl extension for Version Objects
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/version
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/version-%{version}.tar.gz
%if %{with perl_version_enables_optional_test} && ! %{defined perl_bootstrap}
%endif
Requires:       perl(B)
Requires:       perl(Carp)
Requires:       perl(locale)
Requires:       perl(UNIVERSAL)
Requires:       perl(warnings)
Requires:       perl(XSLoader)
%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(version::vxs\\)
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
Provides:       perl(version::vpp)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(I18N::Langinfo)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(UNIVERSAL)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(locale)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-version-tests -f %{oreon_filedir}/perl-version-tests.list

%changelog

%autochangelog
