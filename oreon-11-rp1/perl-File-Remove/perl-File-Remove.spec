Name:		perl-File-Remove
Version:	1.61
Release:	11%{?dist}
Summary:	Convenience module for removing files and directories
License:	GPL-1.0-or-later OR Artistic-1.0-Perl

URL:		https://metacpan.org/release/File-Remove
Source0:	https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/File-Remove-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 fd857f585908fc503461b9e48b3c8594e6535766bc14beb17c90ba58d5dc4975
%global source0_file File-Remove-1.61.tar.gz
# oreon url source checksums end

BuildRequires:	%{__perl}
BuildRequires:	%{__make}

BuildRequires:	perl-generators
BuildRequires:	perl(blib)
BuildRequires:	perl(constant)
BuildRequires:	perl(Cwd) >= 3.29
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Glob)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec) >= 3.29
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::More) >= 0.42
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)

BuildArch:	noarch

%description
%{summary}

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/File-Remove-1.61.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "fd857f585908fc503461b9e48b3c8594e6535766bc14beb17c90ba58d5dc4975" || { echo "oreon: Source0 SHA256 mismatch for File-Remove-1.61.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n File-Remove-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install} DESTDIR="$RPM_BUILD_ROOT"
%{_fixperms} "$RPM_BUILD_ROOT"/*

%check
%{__make} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/File
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.61-11
- Prepare for Oreon 11 (RP1)
