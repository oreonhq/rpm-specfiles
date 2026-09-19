%global source0_hash e39a3f9784da4844b22d6a44739d9f96178d4fc0fbaa6bfe0a420f883c90103c

# Do not tests because they need a file system that has enabled extended
# attributes
%bcond_with perl_File_ExtAttr_enables_test

Name:           perl-File-ExtAttr
Version:        1.09
Release:        53%{?dist}
Summary:        Perl extension for accessing extended attributes of files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-ExtAttr
Source0:        https://cpan.metacpan.org/authors/id/R/RI/RICHDAWE/File-ExtAttr-%{version}.tar.gz
# 1/2 Do not use attr library because attr-2.4.48 removed the header files in
# favour of glibc, CPAN RT#125804.
Patch0:         File-ExtAttr-1.09-Port-Linux-to-sys-xattr.h.patch
# 2/2 Do not use attr library because attr-2.4.48 removed the header files in
# favour of glibc, CPAN RT#125804.
Patch1:         File-ExtAttr-1.09-Remove-dependency-on-attr-library-on-Linux.patch

BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
%if %{with perl_File_ExtAttr_enables_test}
# Run-time
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Errno)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Test::Distribution)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
%endif

%description
File::ExtAttr is a Perl module providing access to the extended
attributes of files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-ExtAttr-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor optimize="%{optflags}" NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
%if %{with perl_File_ExtAttr_enables_test}
# NOTE:  these are noisy; as near as I can tell this is expected
# NOTE2: if you're testing on a filesystem that does not support extended
#        attributes, in all likelyhood the tests will fail.  If anyone has 
#        a quick&easy non-priv'ed way to test for this, I'll be more than 
#        happy to include it.
# NOTE3: Tests disabled for now, pending a way to detect & disable on non-ea 
#        enabled filesystems
make test
%endif

%files
%doc Changes README TODO
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/File*
%{_mandir}/man3/*

%changelog
%autochangelog
