%global source0_hash 29bb2083f3f982a39f4852243f4f6a11916966f20e6e77864e99269d11e8b65e
Name:           perl-Alien-FFI
Version:        0.27
Release:        15%{?dist}
Summary:        Make available libffi
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Alien-FFI
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Alien-FFI-%{version}.tar.gz
Patch0:         Alien-FFI-0.27-Simplify-alienfile-to-system-installation.patch
%global debug_package %{nil}
Requires:       libffi-devel%{?_isa} %(perl -MPkgConfig::LibPkgConf -e 'print qq{= } . pkgconf_version(q{libffi})' 2>/dev/null)
Requires:       perl(Alien::Base) >= 2.10
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Alien::Base|Test2::V0\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Alien::Base)
BuildRequires:  perl(Alien::Build::MM)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(PkgConfig::LibPkgConf)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Alien)
BuildRequires:  perl(alienfile)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(libffi)
# /oreon:deps
%description
This ensures that libffi library can be used by other Perl distributions.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(IPC::Cmd)
Requires:       perl(Test2::V0) >= 0.000121
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Alien-FFI-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
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
%files -n perl-Alien-FFI-tests -f %{oreon_filedir}/perl-Alien-FFI-tests.list

%changelog

%autochangelog
