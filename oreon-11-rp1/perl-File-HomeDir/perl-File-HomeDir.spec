%global source0_hash 593737c62df0f6dab5d4122e0b4476417945bb6262c33eedc009665ef1548852
Name:           perl-File-HomeDir
Version:        1.006
Release:        1%{?dist}
Summary:        Find your home and other directories on any platform
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-HomeDir
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/File-HomeDir-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Cwd) >= 3.12
Requires:       perl(File::Path) >= 2.01
Requires:       perl(File::Spec) >= 3.12
Requires:       perl(File::Temp) >= 0.19
Requires:       perl(File::Which) >= 0.05
%global __requires_exclude perl\\(Cwd\\)|perl\\(File::Path\\)|perl\\(File::Spec\\)|perl\\(File::Temp\\)|perl\\(File::Which\\)|perl\\(Mac::|perl\\(Win32
Provides:       perl(File::HomeDir)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
File::HomeDir is a module for locating the directories that are "owned"
by a user (typically your user) and to solve the various issues that
arise trying to find them consistently across a wide variety of
platforms.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n File-HomeDir-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.006-16
- Prepare for Oreon 11 (RP1)
