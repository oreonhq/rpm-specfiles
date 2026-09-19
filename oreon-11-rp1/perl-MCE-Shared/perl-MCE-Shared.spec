%global source0_hash fa4c487adfb0db3c8f2b6aa274d33d8f827fa234c631bb3af3d94fa4a3c9462f

Name:		perl-MCE-Shared
Version:	1.893
Release:	4%{?dist}
Summary:	MCE extension for sharing data, supporting threads and processes
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/MCE-Shared
Source0:	https://cpan.metacpan.org/authors/id/M/MA/MARIOROY/MCE-Shared-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(base)
BuildRequires:	perl(bytes)
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
BuildRequires:	perl(Errno)
BuildRequires:	perl(if)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(MCE) >= 1.889
BuildRequires:	perl(MCE::Mutex)
BuildRequires:	perl(MCE::Signal)
BuildRequires:	perl(MCE::Util)
BuildRequires:	perl(overload)
BuildRequires:	perl(overloading)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Socket)
BuildRequires:	perl(Storable) >= 2.04
BuildRequires:	perl(strict)
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(warnings)
# Optional Functionality
# Note: MCE will pull in Sereal if it is available
BuildRequires:	perl(IO::FDPass) >= 1.2
# Test Suite
BuildRequires:	perl(MCE::Flow)
BuildRequires:	perl(open)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(utf8)
# Dependencies
Requires:	perl(IO::FDPass) >= 1.2
Requires:	perl(MCE) >= 1.889
Requires:	perl(overloading)
Requires:	perl(POSIX)
Requires:	perl(Storable) >= 2.04

# Remove bogus dependency on perl(PDL)
%global __requires_exclude ^perl\\(PDL\\)

%description
This module provides data sharing capabilities for MCE, supporting threads and
processes. MCE::Hobo provides threads-like parallelization for running code
asynchronously.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MCE-Shared-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE Copying
%doc Changes README.md
%{perl_vendorlib}/MCE/
%{_mandir}/man3/MCE::Hobo.3*
%{_mandir}/man3/MCE::Shared.3*
%{_mandir}/man3/MCE::Shared::Array.3*
%{_mandir}/man3/MCE::Shared::Base.3*
%{_mandir}/man3/MCE::Shared::Cache.3*
%{_mandir}/man3/MCE::Shared::Common.3*
%{_mandir}/man3/MCE::Shared::Condvar.3*
%{_mandir}/man3/MCE::Shared::Handle.3*
%{_mandir}/man3/MCE::Shared::Hash.3*
%{_mandir}/man3/MCE::Shared::Minidb.3*
%{_mandir}/man3/MCE::Shared::Ordhash.3*
%{_mandir}/man3/MCE::Shared::Queue.3*
%{_mandir}/man3/MCE::Shared::Scalar.3*
%{_mandir}/man3/MCE::Shared::Sequence.3*
%{_mandir}/man3/MCE::Shared::Server.3*

%changelog
%autochangelog
