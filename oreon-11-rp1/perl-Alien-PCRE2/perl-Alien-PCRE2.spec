%global source0_hash a026c2e63f0e2dca8547c842489fbf376d831f6585a7dd7bed2b52a3416d5ee1
Name:           perl-Alien-PCRE2
Version:        0.017000
Release:        10%{?dist}
Summary:        Install and locate PCRE2 library
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Alien-PCRE2
Source0:        https://cpan.metacpan.org/authors/id/W/WB/WBRASWELL/Alien-PCRE2-%{version}.tar.gz
Patch0:         Alien-PCRE2-0.017000-Disable-shared-mode.patch
%global debug_package %{nil}
Requires:       pcre2-devel%{?_isa}
%if "0" == "%(pkgconf --exist libpcre2-8 2>/dev/null; echo $?)"
Requires:       pkgconfig(libpcre2-8) = %(pkgconf --modversion libpcre2-8)
%endif
Requires:       perl(Alien::Base) >= 0.038
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Alien::Base\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  pcre2-devel
BuildRequires:  perl(Alien::Base)
BuildRequires:  perl(Alien::Build::MM)
BuildRequires:  perl(Alien::Build::Plugin::PkgConfig::Negotiate)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(English)
BuildRequires:  perl(Env)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Alien)
BuildRequires:  perl(Test::Alien::Diag)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(alienfile)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(libpcre2-8)
# /oreon:deps
%description
This package can be used by other Perl modules that require PCRE2 library, the
new Perl Compatible Regular Expression engine.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Alien-PCRE2-%{version}
# Remove tests which are always skipped.
rm t/03_pcre2grep.t
perl -i -ne 'print $_ unless m{\A\Qt/03_pcre2grep.t\E}' MANIFEST
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

export ALIEN_PCRE2_MIN_VERSION=0
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
rm %{buildroot}/%{perl_vendorarch}/auto/share/dist/Alien-PCRE2/_alien/alienfile
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Alien-PCRE2-tests -f %{oreon_filedir}/perl-Alien-PCRE2-tests.list

%changelog

%autochangelog
