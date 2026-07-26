%global source0_hash 213c0eb0cc13167dd1fa1ecc2af39f7225911f18b14a89e0c1566456270bcbf5

Name:           perl-Module-Starter
Epoch:          1
Version:        1.82
Release:        2%{?dist}
Summary:        A simple starter kit for any module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Starter
Source0:        https://cpan.metacpan.org/authors/id/X/XS/XSAWYERX/Module-Starter-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.8.3
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Pod::Usage) >= 1.21
# Software::LicenseUtils version from Software::License in META
BuildRequires:  perl(Software::LicenseUtils) >= 0.103005
# Tests:
# base not used
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(parent)
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(version) >= 0.77
Requires:  perl(ExtUtils::Manifest)
# Software::LicenseUtils version from Software::License in META
Requires:  perl(Software::LicenseUtils) >= 0.103005

%{?perl_default_filter}
# Filter in-lined Perl code from lib/Module/Starter/Simple.pm
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((ExtUtils::MakeMaker|inc::Module::Install|Module::Build|Test::More)\\)
# Remove underspecied dependencies
%global __requires_exclude %{__requires_exclude}|^perl\\(version\\)$
# Hide private modules
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((Foo::Bar|Module::Starter::TestPlugin)\\)

%description
This is a CPAN module/utility to assist in the creation of new modules in a
sensible and sane fashion.  Unless you're interested in extending the
functionality of this module, you should examine the documentation for
'module-starter', for information on how to use this tool.

It is noted that there are a number of extensions to this tool, including
plugins to create modules using templates as recommended by Damian Conway's
"Perl Best Practices" (O'Reilly, 2005).  (See also the package
perl-Module-Starter-PBP for the aforementioned templates.)

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(ExtUtils::MakeMaker)
Requires:       perl(Test::More) >= 0.94
Requires:       perl(version) >= 0.77

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Starter-%{version}

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
#!/bin/bash
# t/test-dist.t writes in o $PWD/t/data
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset DONT_DEL_TEST_DIST MODULE_STARTER_DIR RELEASE_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorlib}/Module
%{perl_vendorlib}/Module/Starter{,.pm}
%{_bindir}/module-starter
%{_mandir}/man1/module-starter.*
%{_mandir}/man3/*Module::Starter{.,::}*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
