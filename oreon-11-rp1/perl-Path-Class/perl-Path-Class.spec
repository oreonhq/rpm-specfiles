%global source0_hash 654781948602386f2cb2e4473a739f17dc6953d92aabc2498a4ca2561bc248ce
Name:		perl-Path-Class
Version:	0.37
Release:        31%{?dist}
Summary:        Cross-platform path specification manipulation
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Path-Class
Source0:        https://cpan.metacpan.org/authors/id/K/KW/KWILLIAMS/Path-Class-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl(File::Copy)
Requires:	perl(Perl::OSType)
Provides:       perl(Path::Class)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Perl::OSType)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Path::Class is a module for manipulation of file and directory specifications
(strings describing their locations, like '/home/ken/foo.txt' or
'C:\Windows\Foo.txt') in a cross-platform manner. It supports pretty much every
platform Perl runs on, including Unix, Windows, Mac, VMS, Epoc, Cygwin, OS/2,
and NetWare.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Path-Class-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.37-31
- Prepare for Oreon 11 (RP1)
