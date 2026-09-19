%global source0_hash a3f2ca9d2baefc1aaa40908b2f9cb9292fda3e7d797e38bbd78eabb9d9daeb6b

%global cpan_version 1.92

Name:           perl-BDB
# Extend to 2 digits to get higher RPM package version than 1.88
Version:        %{cpan_version}
Release:        29%{?dist}
Summary:        Asynchronous Berkeley DB access
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/BDB
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/BDB-%{cpan_version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libdb-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.8
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(common::sense)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader)
Requires:       perl(XSLoader)

%{?perl_default_filter}

%description
Asynchronous Berkeley DB access.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn BDB-%{cpan_version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license COPYING
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/BDB.pm
%{_mandir}/man3/*.3*

%changelog
%autochangelog
