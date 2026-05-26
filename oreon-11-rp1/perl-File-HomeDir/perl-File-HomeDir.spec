Name:           perl-File-HomeDir
Version:        1.006
Release:        16%{?dist}
Summary:        Find your home and other directories on any platform
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-HomeDir
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/File-HomeDir-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 593737c62df0f6dab5d4122e0b4476417945bb6262c33eedc009665ef1548852
%global source0_file File-HomeDir-1.006.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.5.3
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# POSIX not used on Linux
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd) >= 3.12
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Path) >= 2.01
BuildRequires:  perl(File::Spec) >= 3.12
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(File::Which) >= 0.05
# Mac::Files not used on Linux
# Mac::SystemDirectory not used on Linux
BuildRequires:  perl(vars)
# Win32 not used on Linux
# Tests:
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More) >= 0.90
# Dependencies:
Requires:       perl(Cwd) >= 3.12
Requires:       perl(File::Path) >= 2.01
Requires:       perl(File::Spec) >= 3.12
Requires:       perl(File::Temp) >= 0.19
Requires:       perl(File::Which) >= 0.05

# Remove unwanted and under-specified dependencies
%global __requires_exclude perl\\(Cwd\\)|perl\\(File::Path\\)|perl\\(File::Spec\\)|perl\\(File::Temp\\)|perl\\(File::Which\\)|perl\\(Mac::|perl\\(Win32

%description
File::HomeDir is a module for locating the directories that are "owned"
by a user (typically your user) and to solve the various issues that
arise trying to find them consistently across a wide variety of
platforms.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/File-HomeDir-1.006.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "593737c62df0f6dab5d4122e0b4476417945bb6262c33eedc009665ef1548852" || { echo "oreon: Source0 SHA256 mismatch for File-HomeDir-1.006.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n File-HomeDir-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/File/
%{_mandir}/man3/File::HomeDir.3*
%{_mandir}/man3/File::HomeDir::Darwin.3*
%{_mandir}/man3/File::HomeDir::Darwin::Carbon.3*
%{_mandir}/man3/File::HomeDir::Darwin::Cocoa.3*
%{_mandir}/man3/File::HomeDir::Driver.3*
%{_mandir}/man3/File::HomeDir::FreeDesktop.3*
%{_mandir}/man3/File::HomeDir::MacOS9.3*
%{_mandir}/man3/File::HomeDir::Test.3*
%{_mandir}/man3/File::HomeDir::Unix.3*
%{_mandir}/man3/File::HomeDir::Windows.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.006-16
- Prepare for Oreon 11 (RP1)
