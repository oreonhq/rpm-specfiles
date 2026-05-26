Name: 		perl-Text-Glob
Version: 	0.11
Release: 	27%{?dist}
Summary: 	Perl module to match globbing patterns against text
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/Text-Glob
Source0: 	https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Text-Glob-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 069ccd49d3f0a2dedb115f4bdc9fbac07a83592840953d1fcdfc39eb9d305287
%global source0_file Text-Glob-0.11.tar.gz
# oreon url source checksums end

BuildArch: noarch

BuildRequires:  perl-generators
BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)

%description
Text::Glob implements glob(3) style matching that can be used to match
against text, rather than fetching names from a file-system.  If you
want to do full file globbing use the File::Glob module instead.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Text-Glob-0.11.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "069ccd49d3f0a2dedb115f4bdc9fbac07a83592840953d1fcdfc39eb9d305287" || { echo "oreon: Source0 SHA256 mismatch for Text-Glob-0.11.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Text-Glob-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes
%{perl_vendorlib}/Text
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.11-27
- Prepare for Oreon 11 (RP1)
