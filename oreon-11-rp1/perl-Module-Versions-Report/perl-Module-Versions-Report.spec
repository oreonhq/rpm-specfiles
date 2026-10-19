%global source0_hash a3261d0d84b17678d8c4fd55eb0f892f5144d81ca53ea9a38d75d1a00ad9796a
Name:           perl-Module-Versions-Report
Version:        1.06
Release:        1%{?dist}
Summary:        Report versions of all modules in memory
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Versions-Report
Source0:        https://cpan.metacpan.org/authors/id/J/JE/JESSE/Module-Versions-Report-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  //bin/perl
BuildRequires:  /usr/bin/make
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test)
BuildRequires:  perl(Text::Tabs)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
If you add "use Module::Versions::Report;" to a program (especially
handy if your program is one that demonstrates a bug in some module),
then when the program has finished running, you well get a report
detailing the all modules in memory, and noting the version of each
(for modules that defined a $VERSION, at least).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Versions-Report-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
