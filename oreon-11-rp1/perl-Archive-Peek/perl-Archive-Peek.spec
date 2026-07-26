%global source0_hash 710635f61eb8197ff2c25c4f032976926528d133091ede2194c8e28059480d24

Name:		perl-Archive-Peek
Version:	0.37
Release:	12%{?dist}
Summary:	Peek into archives without extracting them
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Archive-Peek
Source0:	https://cpan.metacpan.org/modules/by-module/Archive/Archive-Peek-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Module Runtime
BuildRequires:	perl(Archive::Tar)
BuildRequires:	perl(Archive::Zip)
BuildRequires:	perl(Archive::Zip::MemberRead)
BuildRequires:	perl(Carp)
BuildRequires:	perl(IO::Uncompress::Bunzip2)
BuildRequires:	perl(Moo)
BuildRequires:	perl(Types::Path::Tiny)
# Test Suite
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Test::More) >= 0.96
BuildRequires:	perl(Test::Pod) >= 1.14
# Runtime
Requires:	perl(IO::Uncompress::Bunzip2)

%description
This module lets you peek into archives without extracting them. It currently
supports tar files and zip files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Archive-Peek-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc CHANGES README
%{perl_vendorlib}/Archive/
%{_mandir}/man3/Archive::Peek.3*

%changelog
%autochangelog
