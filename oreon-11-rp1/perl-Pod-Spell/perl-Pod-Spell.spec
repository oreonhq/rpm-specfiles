%global source0_hash 7ef56c9229f3efbc71a0462ce44490c0dd49fbf3b21fe85bb08b1eeac6f7b063
Name:           perl-Pod-Spell
Version:        1.27
Release:        1%{?dist}
Summary:        A formatter for spell-checking POD
License:        Artistic-2.0
URL:            https://metacpan.org/release/Pod-Spell
Source0:        https://cpan.metacpan.org/modules/by-module/Pod/Pod-Spell-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(File::ShareDir)
Recommends:     perl(I18N::Langinfo)
Recommends:     perl(POSIX)
Provides:       perl(Pod::Spell)
Provides:       perl(Pod::Wordlist)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Lingua::EN::Inflect)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(locale)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Pod::Spell is a Pod formatter whose output is good for spell-checking.
Pod::Spell rather like Pod::Text, except that it doesn't put much
effort into actual formatting, and it suppresses things that look like
Perl symbols or Perl jargon (so that your spell-checking program won't
complain about mystery words like "$thing" or "Foo::Bar" or "hashref").

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Pod-Spell-%{version}

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
%{_fixperms} -c %{buildroot}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_libexecdir}/%{name}/bin
ln -s %{_bindir}/podspell %{buildroot}%{_libexecdir}/%{name}/bin
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Pod-Spell-tests -f %{oreon_filedir}/perl-Pod-Spell-tests.list

%changelog

%autochangelog
