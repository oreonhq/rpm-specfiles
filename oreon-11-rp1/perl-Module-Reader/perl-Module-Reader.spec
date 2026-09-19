%global source0_hash 2d5a0adb772517754fbfec0180d6a51039bb0cd3bd3316a59eaa32c05ddde284

Name:           perl-Module-Reader
Version:        0.003003
Release:        26%{?dist}
Summary:        Read the source of a module like perl does
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Reader
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Module-Reader-%{version}.tar.gz
# Adjust an error message to perl 5.38, bug #2222182, CPAN RT#148979,
# proposed to an upstream
Patch0:         Module-Reader-0.003003-Adjust-require-exception-to-perl-5.37.8-wording.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
# IO::String - required only for Perl < 5.008
BuildRequires:  perl(Scalar::Util)
# Tests
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.88

# Hide private modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((InlineModule|MyTestModule)\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((InlineModule|MyTestModule)\\)

%description
Reads the content of perl modules the same way perl does. This includes
reading modules available only by @INC hooks, or filtered through them.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Module-Reader-%{version}
# Help generators to recognize Perl scripts
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
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes
%dir %{perl_vendorlib}/Module
%{perl_vendorlib}/Module/Reader.pm
%{_mandir}/man3/Module::Reader.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
