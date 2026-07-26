%global source0_hash d339d057359c8f7249ce1958ea9618b50d9f6b3ff6228199c319f5eb17e13be8

Name:           perl-File-Tempdir
Version:        0.02
Release:        30%{?dist}
Summary:        Object interface for File::Temp module
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-Tempdir

Source0:        https://cpan.metacpan.org/authors/id/N/NA/NANARDON/File-Tempdir-%{version}.tar.gz
%{?el5:BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)}
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

# Run-time
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Testing
BuildRequires:  perl(Test::More)

%description
This module provide an object interface to tempdir() from File::Temp. This
allow to destroy the temporary directory as soon you don't need it anymore
using the magic DESTROY() function automatically call be perl when the
object is no longer reference.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-Tempdir-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
%if 0%{?el5}
rm -rf $RPM_BUILD_ROOT
%endif

make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
