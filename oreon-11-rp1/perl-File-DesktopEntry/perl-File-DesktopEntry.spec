%global source0_hash 63f95798d80b81ea8cea4848f342f26593c60f152dbd04d8981c846f979e6835

# Run optional tests
%if ! (0%{?rhel})
%{bcond_without perl_File_DesktopEntry_enables_optional_test}
%else
%{bcond_with perl_File_DesktopEntry_enables_optional_test}
%endif

Name:           perl-File-DesktopEntry
Version:        0.23
Release:        2%{?dist}
Summary:        Object to handle .desktop files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-DesktopEntry
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MICHIELB/File-DesktopEntry-0.23.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::BaseDir) >= 0.03
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Test::More) 
BuildRequires:  perl(utf8)
%if %{with perl_File_DesktopEntry_enables_optional_test} && !%{defined perl_bootstrap}
# Optional tests
# Build cycle: perl-CPAN-Changes → perl-Path-Tiny → perl-Unicode-UTF8
# → perl-Module-Install-ReadmeFromPod → perl-IO-All → perl-File-MimeInfo
# → perl-File-DesktopEntry → perl-CPAN-Changes
BuildRequires:  perl(Test::CPAN::Changes)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
%endif

Requires:       perl(Cwd)
Requires:       perl(File::Path)

%description
This module is used to work with .desktop files. The format of these files
is specified by the freedesktop "Desktop Entry" specification. This module
can parse these files but also knows how to run the applications defined by
these files. For this module version 1.0 of the specification was used.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n File-DesktopEntry-%{version}
# Help generators to recognize Perl scripts
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

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a MANIFEST t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/*_pod*
rm %{buildroot}%{_libexecdir}/%{name}/t/06_changes.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes
%{perl_vendorlib}/File*
%{_mandir}/man3/File::DesktopEntry*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.23-2
- Prepare for Oreon 11 (RP1)
