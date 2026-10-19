%global source0_hash ab3e3845337b78ee14b50fdbc68197c71f5ea66ebdde0870dee4e642c305c514
Name:           perl-Pod-Simple
Epoch:          1
Version:        3.47
Release:        1%{?dist}
Summary:        Framework for parsing POD documentation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Simple
Source0:        https://cpan.metacpan.org/authors/id/K/KH/KHW/Pod-Simple-%{version}.tar.gz
BuildArch:      noarch
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Text::Wrap\\)$
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{__requires_exclude}|^perl\\(helpers\\)$
Provides:       perl(Pod::Simple)
Provides:       perl(Pod::Simple::Checker)
Provides:       perl(Pod::Simple::Methody)
Provides:       perl(Pod::Simple::RTF)
Provides:       perl(Pod::Simple::XMLOutStream)
Provides:       perl(Pod::Simple::PullParser)
Provides:       perl(Pod::Simple::PullParserEndToken)
Provides:       perl(Pod::Simple::PullParserStartToken)
Provides:       perl(Pod::Simple::PullParserTextToken)
Provides:       perl(Pod::Simple::Text)
Provides:       perl(Pod::Simple::PullParser)
Provides:       perl(Pod::Simple::PullParserEndToken)
Provides:       perl(Pod::Simple::PullParserStartToken)
Provides:       perl(Pod::Simple::PullParserTextToken)
Provides:       perl(Pod::Simple::Text)
Provides:       perl(Pod::Simple::XHTML)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Pod::Escapes)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(base)
BuildRequires:  perl(if)
BuildRequires:  perl(integer)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Pod::Simple is a Perl library for parsing text in the POD (plain old
documentation) markup language that is typically used for writing
documentation for Perl and for Perl modules.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(FindBin)
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Pod-Simple-%{version}

# Help generators to recognize Perl scripts
for F in t/*.t t/*.pl; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset PERL_CORE PERL_TEST_DIFF
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Pod-Simple-tests -f %{oreon_filedir}/perl-Pod-Simple-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.47-4
- Prepare for Oreon 11 (RP1)
