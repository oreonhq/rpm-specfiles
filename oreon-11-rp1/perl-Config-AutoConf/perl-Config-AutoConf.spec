%global source0_hash bb57a958ef49d3f7162276dae14a7bd5af43fd1d8513231af35d665459454023
%bcond perl_Config_AutoConf_enables_File_Slurper %{undefined rhel}
%bcond perl_Config_AutoConf_enables_Scalar_Util 1
Name:           perl-Config-AutoConf
Version:        0.320
Release:        15%{?dist}
Summary:        A module to implement some of AutoConf macros in pure Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Config-AutoConf
Source0:        https://cpan.metacpan.org/authors/id/A/AM/AMBS/Config-AutoConf-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Config_AutoConf_enables_File_Slurper}
%endif
%if %{with perl_Config_AutoConf_enables_Scalar_Util}
%endif
%if %{with perl_Config_AutoConf_enables_File_Slurper}
Suggests:       perl(File::Slurper)
%endif
%if %{with perl_Config_AutoConf_enables_Scalar_Util}
Suggests:       perl(Scalar::Util) >= 1.18
%endif
Provides:       perl(Config::AutoConf)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Slurper)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module simulates some of the tasks autoconf macros do.  To detect
a command, a library and similar.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Config-AutoConf-%{version}

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.320-15
- Prepare for Oreon 11 (RP1)
