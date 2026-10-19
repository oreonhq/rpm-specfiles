%global source0_hash 069ccd49d3f0a2dedb115f4bdc9fbac07a83592840953d1fcdfc39eb9d305287
Name: 		perl-Text-Glob
Version: 	0.11
Release:        27%{?dist}
Summary:        Perl module to match globbing patterns against text
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/Text-Glob
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Text-Glob-%{version}.tar.gz
BuildArch: noarch
Provides:       perl(Text::Glob)
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  /usr/bin/perl
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
# /oreon:deps
%description
Text::Glob implements glob(3) style matching that can be used to match
against text, rather than fetching names from a file-system.  If you
want to do full file globbing use the File::Glob module instead.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Text-Glob-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.11-27
- Prepare for Oreon 11 (RP1)
