Name: 		perl-File-Copy-Recursive
Version: 	0.45
Release: 	19%{?dist}
Summary: 	Extension for recursively copying files and directories 
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/File-Copy-Recursive
Source0: 	https://cpan.metacpan.org/authors/id/D/DM/DMUEY/File-Copy-Recursive-0.45.tar.gz
# oreon url source checksums begin
%global source0_sha256 d3971cf78a8345e38042b208bb7b39cb695080386af629f4a04ffd6549df1157
%global source0_file File-Copy-Recursive-0.45.tar.gz
# oreon url source checksums end

BuildArch: noarch

# rpm's perl dep generators fails to catch this
Requires:  perl(File::Glob)

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::File)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warnings)

%description
This module copies and moves directories recursively to an optional depth and
attempts to preserve each file or directory's mode.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/File-Copy-Recursive-0.45.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d3971cf78a8345e38042b208bb7b39cb695080386af629f4a04ffd6549df1157" || { echo "oreon: Source0 SHA256 mismatch for File-Copy-Recursive-0.45.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n File-Copy-Recursive-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
chmod -R u+w %{buildroot}/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/File
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.45-19
- Prepare for Oreon 11 (RP1)
