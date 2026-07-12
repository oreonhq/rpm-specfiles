%global source0_hash 70a69e7c4e65cb0c35bf16a0115a6d113a534e4ad9cd6cf2d767a6bd55311ae5

Name:           perl-Color-ANSI-Util
Version:        0.165
Release:        5%{?dist}
Summary:        Routines for dealing with ANSI colors
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Color-ANSI-Util/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/Color-ANSI-Util-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-Time
BuildRequires:  perl(Color::RGB::Util) >= 0.607
BuildRequires:  perl(Exporter) >= 5.57
# Optional - BuildRequires:  perl(Term::Detect::Software)
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(Color::RGB::Util) >= 0.607
Requires:       perl(Exporter) >= 5.57
Recommends:     perl(Term::Detect::Software)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Exporter\\)\\s*$
%global __requires_exclude %{?__requires_exclude}|perl\\(Color::RGB::Util\\)\\s*$

Provides:       perl(Color::ANSI::Util)
%description
This module provides routines for dealing with ANSI colors. The two main
functions are ansifg and ansibg. With those functions, you can specify
colors in RGB and let it output the correct ANSI color escape code
according to the color depth support of the terminal (whether 16-color,
256-color, or 24bit). There are other functions to convert RGB to ANSI
in specific color depths, or reverse functions to convert from ANSI to
RGB codes.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Color-ANSI-Util-%{version}
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
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/author*
rm %{buildroot}%{_libexecdir}/%{name}/t/release*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING RELEASE_TESTING
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Color*
%{_mandir}/man3/Color::ANSI::Util*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
