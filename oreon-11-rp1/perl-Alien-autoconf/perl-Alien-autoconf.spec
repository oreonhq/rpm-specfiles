%global source0_hash a19ec855faa24dabb5020f9f51e2d31950dbef80a067ed65942b4351831ebf35
%global debug_package %{nil}
Name:           perl-Alien-autoconf
Version:        0.20
Release:        1%{?dist}
Summary:        Find autoconf
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Alien-autoconf
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Alien-autoconf-%{version}.tar.gz
Patch0:         Alien-autoconf-0.18-Implement-system-installation.patch
Requires:       autoconf %(perl -e 'print qq{ = $1} if qx{autoconf --version} =~ m{([\d+\.]+)}' 2>/dev/null)
Requires:       perl(Alien::Base) >= 0.038
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Alien::Base|Test2::V0|Test::More)\\)$
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Alien::Base)
BuildRequires:  perl(Alien::Build::MM)
BuildRequires:  perl(Alien::Build::Plugin::Build::Autoconf)
BuildRequires:  perl(Alien::m4)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config)
BuildRequires:  perl(Env)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Alien)
BuildRequires:  perl(alienfile)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This distribution provides autoconf so that it can be used by other Perl
distributions that are on CPAN. This is most commonly necessary when creating
other Aliens that target a autoconf project that does not ship with
a configure script.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test2::V0) >= 0.000121
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Alien-autoconf-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 &&
!s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
rm %{buildroot}/%{perl_vendorarch}/auto/share/dist/Alien-autoconf/_alien/alienfile
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a corpus t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Alien-autoconf-tests -f %{oreon_filedir}/perl-Alien-autoconf-tests.list

%changelog

%autochangelog
