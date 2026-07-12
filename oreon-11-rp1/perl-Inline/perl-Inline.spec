%global source0_hash 105e4271ace1c1b5a264d771ff111d8b928b256002888222862c7be9686f39c5

# Perform an optional test
%bcond_without perl_Inline_enables_optional_test

Name:           perl-Inline
Version:        0.87
Release:        3%{?dist}
Summary:        Inline Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Url:            https://metacpan.org/release/Inline
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Inline-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Find)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Socket)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version) >= 0.82
# Tests only
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Inline::Files)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(XXX)
# Test::Pod 1.41 not used
BuildRequires:  perl(Test::Warn) >= 0.23
%if %{with perl_Inline_enables_optional_test}
# Optional tests
BuildRequires:  perl(diagnostics)
%endif
Requires:       perl(Digest::MD5)
Requires:       perl(DynaLoader)
Requires:       perl(File::Spec) >= 0.80
Requires:       perl(FindBin)
Requires:       perl(Socket)
Requires:       perl(version) >= 0.82

%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((File::Spec|version)\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Inline\\)$
# Remove private modules
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((TestInlineSetup|TestML::Bridge)\\)$
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}

Provides:       perl(Inline)
Provides:       perl(Inline::MakeMaker)
Provides:       perl(Inline)
Provides:       perl(Inline::MakeMaker)
%description
The Inline module allows you to put source code from other programming
languages directly "inline" in a Perl script or module. The code is
automatically compiled as needed, and then loaded for immediate access
from Perl.

Inline saves you from the hassle of having to write and compile your
own glue code using facilities like XS or SWIG. Simply type the code
where you want it and run your Perl as normal. All the hairy details
are handled for you. The compilation and installation of your code
chunks all happen transparently; all you will notice is the delay of
compilation on the first run.

The Inline code only gets compiled the first time you run it (or
whenever it is modified) so you only take the performance hit
once. Code that is Inlined into distributed modules (like on the CPAN)
will get compiled when the module is installed, so the end user will
never notice the compilation time.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Inline-%{version}
find example -type f -exec chmod 0644 {} +
# Help generators to recognize Perl scripts
for F in t/*.t; do
    if [ "$F" != "t/03errors.t" ] && [ "$F" != "t/09perl5lib.t" ]; then
        perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    fi
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Remove author tests
rm -f %{buildroot}%{_libexecdir}/%{name}/t/000*
rm -f %{buildroot}%{_libexecdir}/%{name}/t/author-pod-syntax.t
# XXX Not running
rm -f %{buildroot}%{_libexecdir}/%{name}/t/03errors.t
rm -f %{buildroot}%{_libexecdir}/%{name}/t/09perl5lib.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset PERL_INLINE_DIRECTORY PERL5LIB PERL5OPT
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
unset AUTHOR_TESTING PERL_INLINE_DIRECTORY PERL5LIB PERL5OPT
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING example README
%{perl_vendorlib}/Inline*
%{_mandir}/man3/*.3*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
