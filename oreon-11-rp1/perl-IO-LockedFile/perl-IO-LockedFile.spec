%global source0_hash b1db7e6a6bf1be1e0615a6ecb5cebe78b00e287b127d5856d3f16b35dd47f8b5

Name:           perl-IO-LockedFile
Version:        0.23
Release:        50%{?dist}
Summary:        Something
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-LockedFile
Source0:        https://cpan.metacpan.org/authors/id/R/RA/RANI/IO-LockedFile-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(diagnostics)
BuildArch:      noarch

%description
IO::LockedFile is something

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IO-LockedFile-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

chmod -R u+rwX,go+rX,go-w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
