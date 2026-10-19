%global source0_hash a74241d9592892f60f36788fd26627a17325c257c7e146e4870da0e8c399b948
Name:           perl-JSON-Color
Version:        0.134
Release:        1%{?dist}
Summary:        Encode to colored JSON
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/JSON-Color/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/JSON-Color-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(ColorTheme::NoColor)
Requires:       perl(Module::Load::Util) >= 0.009
Requires:       perl(Role::Tiny)
Requires:       perl(Term::ANSIColor) >= 3.00
Recommends:     perl(Scalar::Util::LooksLikeNumber)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Term::ANSIColor)\\)\s*$
Provides:       perl(JSON::Color)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Color::ANSI::Util)
BuildRequires:  perl(ColorTheme::NoColor)
BuildRequires:  perl(ColorThemeBase::Static::FromStructColors)
BuildRequires:  perl(ColorThemeRole::ANSI)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Graphics::ColorNamesLite::WWW)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Load::Util)
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/author*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
unset AUTHOR_TESTING
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-JSON-Color-tests -f %{oreon_filedir}/perl-JSON-Color-tests.list

%changelog

%autochangelog
