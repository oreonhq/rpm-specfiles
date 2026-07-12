%global source0_hash a74241d9592892f60f36788fd26627a17325c257c7e146e4870da0e8c399b948

Name:           perl-JSON-Color
Version:        0.134
Release:        8%{?dist}
Summary:        Encode to colored JSON
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/JSON-Color/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/JSON-Color-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Color::ANSI::Util)
BuildRequires:  perl(ColorTheme::NoColor)
BuildRequires:  perl(ColorThemeBase::Static::FromStructColors)
BuildRequires:  perl(ColorThemeRole::ANSI)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Graphics::ColorNamesLite::WWW)
BuildRequires:  perl(Module::Load::Util) >= 0.009
BuildRequires:  perl(parent)
BuildRequires:  perl(Role::Tiny)
# Not used for tests - Scalar::Util::LooksLikeNumber
BuildRequires:  perl(Term::ANSIColor) >= 3.00
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(ColorTheme::NoColor)
Requires:       perl(Module::Load::Util) >= 0.009
Requires:       perl(Role::Tiny)
Requires:       perl(Term::ANSIColor) >= 3.00
Recommends:     perl(Scalar::Util::LooksLikeNumber)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Term::ANSIColor)\\)\s*$

Provides:       perl(JSON::Color)
%description
This module generates JSON, colorized with ANSI escape sequences.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n JSON-Color-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

# Help file to recognise the Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%install
%{make_install}
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/author*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
unset AUTHOR_TESTING
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/ColorTheme*
%{perl_vendorlib}/JSON*
%{_mandir}/man3/ColorTheme::JSON::Color::*
%{_mandir}/man3/JSON::Color*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
