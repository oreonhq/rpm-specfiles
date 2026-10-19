%global source0_hash 66aeac6127418be5e471ead3744648c766bd01482825c5b66652675f2bc86a8f
%global cpan_version_major 0.42
%global cpan_version_minor 34
%global cpan_version %{cpan_version_major}%{?cpan_version_minor}
%if ! (0%{?rhel}) || (0%{?oreon} >= 11)
%bcond_without perl_Module_Build_enables_optional_test
%else
%bcond_with perl_Module_Build_enables_optional_test
%endif
Name:           perl-Module-Build
Epoch:          2
Version:        %{cpan_version_major}%{?cpan_version_minor:.%cpan_version_minor}
Release:        1%{?dist}
Summary:        Build and install Perl modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Build
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/Module-Build-0.4234.tar.gz
Patch1:         Module-Build-0.4231-Do-not-die-on-missing-ExtUtils-CBuilder-in-have_c_co.patch
BuildArch:      noarch
%if !%{defined perl_bootstrap}
%if %{with perl_Module_Build_enables_optional_test}
%if 0%{?fedora}  || 0%{?rhel} < 7 || (0%{?oreon} >= 11)
%endif
%endif
%endif
Requires:       perl(CPAN::Meta) >= 2.142060
Requires:       perl(CPAN::Meta::Converter) >= 2.141170
Requires:       perl(CPAN::Meta::Merge)
Recommends:     perl(ExtUtils::CBuilder) >= 0.27
Requires:       perl(ExtUtils::Install) >= 0.3
Requires:       perl(ExtUtils::Manifest) >= 1.54
Requires:       perl(ExtUtils::Mkbootstrap)
Requires:       perl(ExtUtils::ParseXS) >= 2.21
Requires:       perl(inc::latest)
Requires:       perl(Module::Metadata) >= 1.000002
Requires:       perl(Perl::OSType) >= 1
Requires:       perl(TAP::Harness::Env)
Requires:       perl(Test::Harness)
%if !%{defined perl_bootstrap}
Requires:       perl(Software::License)
%endif
Requires:       perl(Pod::Html)
Requires:       perl(Pod::Man) >= 2.17
Requires:       perl(Pod::Text)
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((ExtUtils::Install|File::Spec|Module::Build|Module::Metadata|Perl::OSType)\\)$
%global __requires_exclude %__requires_exclude|^perl\\(CPAN::Meta::YAML\\) >= 0.002$
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{__requires_exclude}|^perl\\(DistGen\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(MBTest\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(Simple\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(Software::License.*\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(Tie::CPHash\\)
Provides:       perl(Module::Build)
Provides:       perl(Module::Build::Compat)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(AutoSplit)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Converter)
BuildRequires:  perl(CPAN::Meta::Merge)
BuildRequires:  perl(CPAN::Meta::YAML)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::Install)
BuildRequires:  perl(ExtUtils::Installed)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(ExtUtils::Mkbootstrap)
BuildRequires:  perl(ExtUtils::Packlist)
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(PAR::Dist)
BuildRequires:  perl(Parse::CPAN::Meta)
BuildRequires:  perl(Perl::OSType)
BuildRequires:  perl(Pod::Readme)
BuildRequires:  perl(TAP::Harness)
BuildRequires:  perl(TAP::Harness::Env)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(inc::latest)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Module::Build is a system for building, testing, and installing Perl
modules. It is meant to be an alternative to ExtUtils::MakeMaker.
Developers may alter the behavior of the module through sub-classing in a
much more straightforward way than with MakeMaker. It also does not require
a make on your system - most of the Module::Build code is pure-perl and
written in a very cross-platform way. In fact, you don't even need a shell,
so even platforms like MacOS (traditional) can use it fairly easily. Its
only prerequisites are modules that are included with perl 5.6.0, and it
works fine on perl 5.005 if you can install a few additional modules.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if !%{defined perl_bootstrap}
%if %{with perl_Module_Build_enables_optional_test}
Requires:       perl(Archive::Zip)
Requires:       perl(File::ShareDir) >= 1.00
Requires:       perl(PAR::Dist)
%endif
%endif
Requires:       perl(TAP::Harness)
Requires:       perl(TAP::Harness::Env)
Requires:       perl(Text::ParseWords)
Requires:       perl(version) >= 0.87
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n Module-Build-%{cpan_version}

# Help generators to recognize Perl scripts
for F in `find t -name *.t -o -name *.pl`; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t _build %{buildroot}%{_libexecdir}/%{name}
perl -pi -e 's#%{buildroot}##' %{buildroot}%{_libexecdir}/%{name}/_build/runtime_params
rm %{buildroot}%{_libexecdir}/%{name}/_build/magicnum
mkdir -p %{buildroot}%{_libexecdir}/%{name}/bin
ln -s %{_bindir}/config_data %{buildroot}%{_libexecdir}/%{name}/bin
rm %{buildroot}%{_libexecdir}/%{name}/t/00-compile.t
for F in `find %{buildroot}%{_libexecdir}/%{name}/t -name *.t -o -name *.pm`; do
    perl -pi -e "s/^\s*blib_load\('([^']+)'\);/use \1;/" $F
    perl -pi -e "s/^blib_load '([^']+)';/use \1;/" $F
done
perl -pi -e "s{'-Mblib', }{'-I'.\\N{U+0024}tmp.'/Simple/blib/lib', '-I'.\\N{U+0024}tmp.'/Simple/blib/arch', }x" \
    %{buildroot}%{_libexecdir}/%{name}/t/xs.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

rm t/signature.t
LANG=C TEST_SIGNATURE=1 MB_TEST_EXPERIMENTAL=1 ./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Module-Build-tests -f %{oreon_filedir}/perl-Module-Build-tests.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2:0.42.34-10
- Import
