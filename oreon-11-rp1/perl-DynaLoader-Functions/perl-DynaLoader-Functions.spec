# This file is licensed under the terms of GNU GPLv2+.

# Run optinonal tests
%if ! (0%{?rhel})
%{bcond_without perl_DynaLoader_Functions_enables_optional_test}
%else
%{bcond_with perl_DynaLoader_Functions_enables_optional_test}
%endif

Name:           perl-DynaLoader-Functions
Version:        0.004
Release:        8%{?dist}
Summary:        Deconstructed dynamic C library loading
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DynaLoader-Functions
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/DynaLoader-Functions-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 5e8e424671a0b2f1d9dff30e5f99087e7555880eb5d79a328b31f4cd4992983d
%global source0_file DynaLoader-Functions-0.004.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
# Config not used on Linux
BuildRequires:  perl(constant)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(parent)
# Tests:
BuildRequires:  perl-devel
BuildRequires:  perl(Test::More)
%if %{with perl_DynaLoader_Functions_enables_optional_test}
# Optional tests:
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.280209
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
%endif
# Dependencies
Requires:       perl(Carp)
Requires:       perl(DynaLoader)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(VMS::Filespec\\)

%description
This module provides a function-based interface to dynamic loading as used
by Perl. Some details of dynamic loading are very platform-dependent, so
correct use of these functions requires the programmer to be mindful of the
space of platform variations.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(ExtUtils::CBuilder)
Requires:       perl(File::Spec)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/DynaLoader-Functions-0.004.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "5e8e424671a0b2f1d9dff30e5f99087e7555880eb5d79a328b31f4cd4992983d" || { echo "oreon: Source0 SHA256 mismatch for DynaLoader-Functions-0.004.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n DynaLoader-Functions-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL --installdirs=vendor --optimize="%{optflags}"
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -fr %{buildroot}%{_libexecdir}/%{name}/t/pod*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Test t/rules-dbm.t write into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/DynaLoader/
%{_mandir}/man3/DynaLoader::Functions.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.004-8
- Prepare for Oreon 11 (RP1)
