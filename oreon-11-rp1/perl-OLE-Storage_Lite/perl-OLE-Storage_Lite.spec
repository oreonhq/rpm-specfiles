%global source0_hash 71c3b6ef082176c9585e620dd48f0f4782c282be73f2a653ea4b618f757bb3fd

Name:		perl-OLE-Storage_Lite
Version:	0.24
Release:	2%{?dist}
Summary:	Simple Class for OLE document interface
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/OLE-Storage_Lite
Source0:	https://cpan.metacpan.org/authors/id/J/JM/JMCNAMARA/OLE-Storage_Lite-%{version}.tar.gz
BuildArch:	noarch
# Build:
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(warnings)
# Run-time:
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IO::Scalar)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(strict)
BuildRequires:	perl(Time::Local)
# Tests:
BuildRequires:	perl(Test::More)
# Dependencies:
Requires:	perl(IO::Scalar)

%description
Simple Class for OLE document interface.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n OLE-Storage_Lite-%{version} 

# Fix line endings
perl -pi -e 's/\r\n/\n/g' Changes README sample/{README,*.pl}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README sample/
%{perl_vendorlib}/OLE/
%{_mandir}/man3/OLE::Storage_Lite.3*

%changelog
%autochangelog
