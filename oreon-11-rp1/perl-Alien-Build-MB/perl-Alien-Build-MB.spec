%global source0_hash a4d4c78e0321d137ca3e711e31b47f33b0cf5645312ad90aba57f99ff29aca37
Name:           perl-Alien-Build-MB
Version:        0.09
Release:        1%{?dist}
Summary:        Alien::Build installer class for Module::Build
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Alien-Build-MB
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Alien-Build-MB-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Alien::Build) >= 1.14
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Alien::Build\\)$
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Alien::Build)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a Module::Build subclass that uses Alien::Build to help create
Alien distributions. The author recommends Alien::Build::MM, which uses
ExtUtils::MakeMaker instead. The primary rationale for this class, is to
prove independence from any particular installer, so that other
installers may be added in the future if they become available. If you
really do prefer to work with Module::Build though, this may be the
installer for you!

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Test::More)
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Alien-Build-MB-%{version}
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t corpus %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Alien-Build-MB-tests -f %{oreon_filedir}/perl-Alien-Build-MB-tests.list

%changelog

%autochangelog
