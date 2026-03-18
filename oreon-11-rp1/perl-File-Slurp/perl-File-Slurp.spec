Name:           perl-File-Slurp
Version:        9999.32
Release:        17%{?dist}
Summary:        Efficient Reading/Writing of Complete Files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-Slurp
Source0:        https://cpan.metacpan.org/modules/by-module/File/File-Slurp-%{version}.tar.gz

BuildArch: noarch

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(re)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

# Tests
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec) >= 3.01
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)

%description
This module provides subs that allow you to read or write entire files with
one simple call. They are designed to be simple to use, have flexible ways
to pass in or get the file contents and to be very efficient. There is also
a sub to read in all the files in a directory other than . and ..

These slurp/spew subs work for files, pipes and sockets, and stdio, 
pseudo-files, and DATA.

%prep
%setup -q -n File-Slurp-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
# For license text(s), see the perl package.
%doc Changes README.md
%{perl_vendorlib}/File
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9999.32-17
- Prepare for Oreon 11 (RP1)
