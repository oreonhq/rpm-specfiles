Name:		perl-Path-Class
Version:	0.37
Release:	31%{?dist}
Summary:	Cross-platform path specification manipulation
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Path-Class
Source0:	https://cpan.metacpan.org/authors/id/K/KW/KWILLIAMS/Path-Class-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 7.32
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec) >= 3.26
BuildRequires:	perl(File::stat)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IO::Dir)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(overload)
BuildRequires:	perl(parent)
BuildRequires:	perl(Perl::OSType)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
# Test Suite
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(warnings)
# Dependencies
Requires:	perl(File::Copy)
Requires:	perl(Perl::OSType)

%description
Path::Class is a module for manipulation of file and directory specifications
(strings describing their locations, like '/home/ken/foo.txt' or
'C:\Windows\Foo.txt') in a cross-platform manner. It supports pretty much every
platform Perl runs on, including Unix, Windows, Mac, VMS, Epoc, Cygwin, OS/2,
and NetWare.

%prep
%setup -q -n Path-Class-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Path/
%{_mandir}/man3/Path::Class.3*
%{_mandir}/man3/Path::Class::Dir.3*
%{_mandir}/man3/Path::Class::Entity.3*
%{_mandir}/man3/Path::Class::File.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.37-31
- Prepare for Oreon 11 (RP1)
