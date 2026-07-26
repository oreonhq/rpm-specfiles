%global source0_hash 87c3f68f8839098f357daa451841746a9eb764866dfb8279942e34ac7075867b

Name: 		perl-File-Flat
Version: 	1.07
Release: 	16%{?dist}
Summary: 	Implements a flat filesystem
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/File-Flat
Source0: 	https://cpan.metacpan.org/authors/id/E/ET/ETHER/File-Flat-%{version}.tar.gz

BuildArch: 	noarch

BuildRequires: %{__perl}
BuildRequires: %{__make}

BuildRequires: perl-generators
BuildRequires: perl(Cwd)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Copy::Recursive) >= 0.35
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Remove) >= 0.38
BuildRequires: perl(File::Spec) >= 0.85
BuildRequires: perl(File::Temp) >= 0.17
BuildRequires: perl(IO::File)
BuildRequires: perl(prefork) >= 0.02
BuildRequires: perl(strict)
BuildRequires: perl(Test::ClassAPI) >= 1.02
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl(vars)
BuildRequires: perl(warnings)

# For improved tests
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::MinimumVersion)
BuildRequires: perl(Test::CPAN::Meta)

%description
File::Flat implements a flat filesystem. A flat filesystem is a filesystem
in which directories do not exist. It provides an abstraction over any 
normal filesystem which makes it appear as if directories do not exist.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-Flat-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{__make} test AUTOMATED_TESTING=1

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/File
%{_mandir}/man3/*

%changelog
%autochangelog
