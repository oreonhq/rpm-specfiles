%global source0_hash 1bc976e2937724896c9f6eae9e5dca981e27f98430b92de270ee3514fd00ac0f
Name:           perl-Module-cpmfile
Version:        0.006
Release:        11%{?dist}
Summary:        Parse cpmfile
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-cpmfile
Source0:        https://cpan.metacpan.org/authors/id/S/SK/SKAJI/Module-cpmfile-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(CPAN::Meta::Requirements) >= 2.130
Requires:       perl(Exporter) >= 5.57
Requires:       perl(YAML::PP) >= 0.027
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Util\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(CPAN::Meta::Requirements\\)\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(Exporter\\)\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(YAML::PP\\)\s*$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Module::CPANfile)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(YAML::PP)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
cpmfile (usually saved as cpm.yml) is yet another file format for
describing module dependencies, and Module::cpmfile helps you parse it.

cpmfile will be used mainly by App::cpm.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-cpmfile-%{version}

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*
rm -rf %{buildroot}/%{_mandir}/man3/Module::cpmfile::Util*
rm -rf %{buildroot}/%{_mandir}/man3/Module::cpmfile::Prereqs*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Module-cpmfile-tests -f %{oreon_filedir}/perl-Module-cpmfile-tests.list

%changelog

%autochangelog
