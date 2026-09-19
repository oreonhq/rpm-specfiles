%global source0_hash 57c6828bb4c8a72170feb67dc1f148abf19cab3827779e30877b4611ed67f3ab

Name:           perl-Chart
Version:        2.403.9
Release:        9%{?dist}
Summary:        Series of charting modules
# lib/Chart.pm:         GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Chart/Manual.pod: GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Chart/Manual/Methods.pod: GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Chart/Manual/Workflows.pod    GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Chart/Setting.pm: GPL-1.0-or-later OR Artistic-1.0-Perl
# LICENSE:              GPL-1.0-or-later OR Artistic-1.0-Perl
# README:               GPL-1.0-or-later OR Artistic-1.0-Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Chart
Source0:        https://cpan.metacpan.org/authors/id/L/LI/LICHTKIND/Chart-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp) >= 1.35
BuildRequires:  perl(constant)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(GD) >= 2
BuildRequires:  perl(GD::Image)
BuildRequires:  perl(Graphics::Toolkit::Color) >= 1
BuildRequires:  perl(POSIX)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp) >= 0.19
Requires:       perl(Carp) >= 1.35
Requires:       perl(GD) >= 2
Requires:       perl(Graphics::Toolkit::Color) >= 1

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Carp|GD|Graphics::Toolkit::Color)\\)$

%description
This module is an attempt to build a general purpose graphing module that
is easily modified and expanded.  Chart uses Lincoln Stein's GD module for
all of its graphics primitives calls.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(GD) >= 2

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Chart-v%{version}
chmod -c 644 TODO
chmod +x t/*.t

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README TODO
%{perl_vendorlib}/Chart.pm
%{perl_vendorlib}/Chart
%{_mandir}/man3/Chart.*
%{_mandir}/man3/Chart::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
