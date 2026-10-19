%global source0_hash fa4c487adfb0db3c8f2b6aa274d33d8f827fa234c631bb3af3d94fa4a3c9462f
Name:		perl-MCE-Shared
Version:	1.893
Release:        1%{?dist}
Summary:        MCE extension for sharing data, supporting threads and processes
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/MCE-Shared
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARIOROY/MCE-Shared-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl(IO::FDPass) >= 1.2
Requires:	perl(MCE) >= 1.889
Requires:	perl(overloading)
Requires:	perl(POSIX)
Requires:	perl(Storable) >= 2.04
%global __requires_exclude ^perl\\(PDL\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Errno)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::FDPass)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(MCE)
BuildRequires:  perl(MCE::Flow)
BuildRequires:  perl(MCE::Mutex)
BuildRequires:  perl(MCE::Signal)
BuildRequires:  perl(MCE::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(open)
BuildRequires:  perl(overload)
BuildRequires:  perl(overloading)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
