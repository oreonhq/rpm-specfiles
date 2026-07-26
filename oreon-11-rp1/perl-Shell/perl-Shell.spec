%global source0_hash f7dbebf65261ed0e5abd0f57052b64d665a1a830bab4c8bbc220f235bd39caf5

# Perform optional tests
%bcond_without perl_Shell_enables_optional_tests

Name:       perl-Shell
Version:    0.73
Release:    31%{?dist}
Summary:    Run shell commands transparently within perl
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
URL:        https://metacpan.org/release/Shell
Source0:    https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/Shell-%{version}.tar.gz
BuildArch:  noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(constant)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Test::More)
%if %{with perl_Shell_enables_optional_tests}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.18
%endif

%description
Using Shell while importing "foo" creates a subroutine "foo" in the name space
of the importing package. Calling "foo" with arguments "arg1", "arg2", ...
results in a shell command "foo arg1 arg2...", where the function name and the
arguments are joined with a blank.

This package is included as a show case, illustrating a few Perl features. It
shouldn't be used for production programs.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(warnings)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Shell-%{version}
%if !%{with perl_shell_enables_optional_tests}
rm t/99_pod.t
perl -i -ne 'print $_ unless m{^t/99_pod\.t}' MANIFEST
%endif
# Correct shebangs
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#![\s./]*perl}{$Config{startperl}}' "$F"
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
%if %{with perl_shell_enables_optional_tests}
rm %{buildroot}%{_libexecdir}/%{name}/t/99pod.t
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README
%{perl_vendorlib}/Shell.pm
%{_mandir}/man3/Shell.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
