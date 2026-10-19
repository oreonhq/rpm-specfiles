%global source0_hash 32a50011e955ac6f3b79e0ce5356e4dd9d0430ab15e5630c736c6fe58efe2703
Name:           perl-Graphics-Toolkit-Color
Version:        1.972
Release:        1%{?dist}
Summary:        Color palette constructor
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Graphics-Toolkit-Color
Source0:        https://cpan.metacpan.org/authors/id/L/LI/LICHTKIND/Graphics-Toolkit-Color-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Exporter) >= 5
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Exporter|Test::More|)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Read-only, color-holding Perl objects with methods to obtain their RGB, HSL,
and YIQ values and if possible a name. This is because humans access colors on
hardware level (eye) in RGB, on cognition level in HSL (brain) and on cultural
level (language) with names. There objects also have methods for measuring
color distances and generating related color objects like gradients and
complements. Having easy access to all three and some color math should enable
you to get the color palette you desire.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness 
Requires:       perl(Test::More) >= 1.3
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Graphics-Toolkit-Color-%{version}
chmod +x t/*.t

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
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
%files -n perl-Graphics-Toolkit-Color-tests -f %{oreon_filedir}/perl-Graphics-Toolkit-Color-tests.list

%changelog

%autochangelog
