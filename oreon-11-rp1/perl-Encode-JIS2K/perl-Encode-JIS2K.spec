%global source0_hash 022f1f3d6869742b3718c27bfcca6f7c96aceffac0a2267d140bbf653d7c0ac2

Name:           perl-Encode-JIS2K
Version:        0.05
Release:        9%{?dist}
Summary:        JIS X 0212 (aka JIS 2000) Encodings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Encode-JIS2K
Source0:        https://cpan.metacpan.org/modules/by-module/Encode/Encode-JIS2K-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl(base)
BuildRequires:  perl(Config)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::CJKConstants)
BuildRequires:  perl(Encode::Encoding)
BuildRequires:  perl(Encode::JP::H2Z)
BuildRequires:  perl(ExtUtils::MakeMaker) %{!?el7:>= 6.76}
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl-Encode-devel
BuildRequires:  perl-generators
Requires:       perl(Encode::JP::H2Z)

%{?perl_default_filter}

%description
This module implements encodings that covers JIS X 0213 charset (AKA JIS 2000,
hence the module name).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Encode-JIS2K-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" \
  %{!?el7:NO_PACKLIST=1 NO_PERLLOCAL=1}
%make_build

%install
%make_install
%if 0%{?el7}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name perllocal.pod -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
%endif
%{_fixperms} %{buildroot}/*

%check
%make_build test

%files
%doc Changes README
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto/

%changelog
%autochangelog
