%global source0_hash 588333b8d000d3d5fe6b088df196c0e6b5fae9846d191cb8b091343c9d808bc0

Name:           perl-Filter-Encoding
Version:        0.01
Release:        28%{?dist}
Summary:        Write your script in any encoding
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Filter-Encoding
Source0:        https://cpan.metacpan.org/authors/id/S/SP/SPROUT/Filter-Encoding-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(utf8)
Requires:       perl(Carp)

%description
This module allows your code to be written in any ASCII-based encoding.
Just pass the name of the encoding as an argument to use Filter::Encoding.
The source code will be decoded and treated as though it had been written
in UTF-8 with use utf8 in effect. That's all this module does.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Filter-Encoding-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
