%global source0_hash a9493d10de63e33c5097f7a69c9ab2bd11ec638f53d384458234ab45c11f9dda

Name:           perl-Devel-CheckOS
Version:        2.04
Release:        5%{?dist}
Summary:        Check what OS we're running on
# Devel/AssertOS/Extending.pod: CC-BY-SA-2.0-UK
# Devel/CheckOS/Families.pod:   CC-BY-SA-2.0-UK
# Other files:  GPL-2.0-only OR Artistic-1.0-Perl
License:        (GPL-2.0-only OR Artistic-1.0-Perl) AND CC-BY-SA-2.0-UK
URL:            https://metacpan.org/release/Devel-CheckOS
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/Devel-CheckOS-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Find::Rule) >= 0.28
BuildRequires:  perl(parent)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warnings)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
Requires:       perl(File::Find::Rule) >= 0.28

# Remove unversioned requires
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Find::Rule\\)$

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{__requires_exclude}|^perl\\(Devel::AssertOS::(AnOperatingSystem.*\|NotAnOperatingSystem))\s*$

%description
Devel::CheckOS provides a more friendly interface to $^O, and also lets you
check for various OS families such as Unix, which includes things like Linux,
*BSD, AIX, HPUX, Solaris etc.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-CheckOS-%{version}

# Help file to recognise the Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done
chmod +x t/coverage.sh

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/pod.t
mkdir -p %{buildroot}%{_libexecdir}/%{name}/bin
ln -s %{_bindir}/use-devel-assertos %{buildroot}%{_libexecdir}/%{name}/bin
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license ARTISTIC.txt GPL2.txt
%doc CHANGELOG README TODO
%{_bindir}/use-devel-assertos
%dir %{perl_vendorlib}/Devel
%{perl_vendorlib}/Devel/AssertOS*
%{perl_vendorlib}/Devel/CheckOS*
%{_mandir}/man1/use-devel-assertos.1.gz
%{_mandir}/man3/Devel::AssertOS*
%{_mandir}/man3/Devel::CheckOS*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
