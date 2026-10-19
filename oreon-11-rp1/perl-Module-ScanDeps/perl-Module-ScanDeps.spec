%global source0_hash 1f5e119cade1466c39c71e5bc35a8d4f4e672635db03d79a5a0dcf08c4e2b5a3
%{bcond_with perl_Module_ScanDeps_enables_prefork}
%{bcond_with perl_Module_ScanDeps_enables_optional_tests}
Name:           perl-Module-ScanDeps
Summary:        Recursively scan Perl code for dependencies
Version:        1.37
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-ScanDeps
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSCHUPP/Module-ScanDeps-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Module_ScanDeps_enables_optional_tests}
%if !%{defined perl_bootstrap} && %{with perl_Module_ScanDeps_enables_prefork}
%endif
%endif
Requires:       perl(B)
Requires:       perl(DynaLoader)
Requires:       perl(Data::Dumper)
Requires:       perl(Encode)
Requires:       perl(File::Find)
Requires:       perl(FindBin)
Requires:       perl(Text::ParseWords)
Recommends:     perl(Digest::MD5)
Recommends:     perl(Storable)
Suggests:       perl(CPANPLUS::Backend)
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}/%{name}
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}^%{_libexecdir}/%{name}/t/data
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Utils\\)
Provides:       perl(Module::ScanDeps)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Net::FTP)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(autouse)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(less)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module scans potential modules used by perl programs and returns a
hash reference.  Its keys are the module names as they appear in %%INC (e.g.
Test/More.pm).  The values are hash references.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(AutoLoader)
Requires:       perl(autouse)
Requires:       perl(Carp)
Requires:       perl(if)
Requires:       perl(less)
Requires:       perl(Net::FTP)
%if %{with perl_Module_ScanDeps_enables_optional_tests}
Requires:       perl(Module::Pluggable)
%if !%{defined perl_bootstrap} && %{with perl_Module_ScanDeps_enables_prefork}
Requires:       perl(prefork)
%endif
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Module-ScanDeps-%{version}

# Help file to recognise the Perl scripts
for F in `find t -name *.t -o -name *.pl`; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -f %{buildroot}%{_libexecdir}/%{name}/t/0-pod.t
perl -i -pe 's{ "-Mblib",}{}' %{buildroot}%{_libexecdir}/%{name}/t/19-autosplit.t
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

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Module-ScanDeps-tests -f %{oreon_filedir}/perl-Module-ScanDeps-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.37-4
- Prepare for Oreon 11 (RP1)
