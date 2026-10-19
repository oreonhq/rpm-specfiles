%global source0_hash e39a3f9784da4844b22d6a44739d9f96178d4fc0fbaa6bfe0a420f883c90103c
%bcond_with perl_File_ExtAttr_enables_test
Name:           perl-File-ExtAttr
Version:        1.09
Release:        1%{?dist}
Summary:        Perl extension for accessing extended attributes of files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-ExtAttr
Source0:        https://cpan.metacpan.org/authors/id/R/RI/RICHDAWE/File-ExtAttr-%{version}.tar.gz
Patch0:         File-ExtAttr-1.09-Port-Linux-to-sys-xattr.h.patch
Patch1:         File-ExtAttr-1.09-Remove-dependency-on-attr-library-on-Linux.patch
%if %{with perl_File_ExtAttr_enables_test}
%endif
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

%if %{with perl_File_ExtAttr_enables_test}
make test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
