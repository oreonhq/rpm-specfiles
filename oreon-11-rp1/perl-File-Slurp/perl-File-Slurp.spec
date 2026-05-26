Name:           perl-File-Slurp
Version:        9999.32
Release:        17%{?dist}
Summary:        Efficient Reading/Writing of Complete Files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-Slurp
Source0:        https://cpan.metacpan.org/authors/id/C/CA/CAPOEIRAB/File-Slurp-9999.32.tar.gz
# oreon url source checksums begin
%global source0_sha256 4c3c21992a9d42be3a79dd74a3c83d27d38057269d65509a2f555ea0fb2bc5b0
%global source0_file File-Slurp-9999.32.tar.gz
# oreon url source checksums end


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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/File-Slurp-9999.32.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "4c3c21992a9d42be3a79dd74a3c83d27d38057269d65509a2f555ea0fb2bc5b0" || { echo "oreon: Source0 SHA256 mismatch for File-Slurp-9999.32.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
