%global source0_hash b459d0b73e18d3c69f15f58acf018cdb599d54482344de570b877874b33cbc53
%bcond_without perl_Parse_PMFile_enables_optional_test
Name:           perl-Parse-PMFile
Version:        0.48
Release:        1%{?dist}
Summary:        Parses .pm file as PAUSE does
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Parse-PMFile
Source0:        https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/Parse-PMFile-%{version}.tar.gz
Patch0:         Parse-PMFile-0.41-Do-not-use-ExtUtils-MakeMaker-CPANfile.patch
BuildArch:      noarch
%if %{with perl_Parse_PMFile_enables_optional_test}
%endif
Requires:       perl(JSON::PP) >= 2.00
Requires:       perl(version) >= 0.83
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((JSON::PP|version)\\)$
Provides:       perl(Parse::PMFile)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Dumpvalue)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Opcode)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(version::vpp)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The most of the code of this module is taken from the PAUSE code as of
April 2013 almost verbatim. Thus, the heart of this module should be quite
stable. However, I made it not to use pipe ("-|") as well as I stripped
database-related code. If you encounter any issue, that's most probably
because of my modification.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Parse-PMFile-%{version}
%patch -P0 -p1
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -f %{buildroot}%{_libexecdir}/%{name}/t/99_pod*
for F in 10_self_check.t 80_version_overload.t 81_version_overload_with_explicit_vpp.t; do
    perl -i -pe 's{\$FindBin::Bin/../lib/}{%{perl_vendorlib}/}' %{buildroot}%{_libexecdir}/%{name}/t/$F
done
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset TEST_POD
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Parse-PMFile-tests -f %{oreon_filedir}/perl-Parse-PMFile-tests.list

%changelog

%autochangelog
