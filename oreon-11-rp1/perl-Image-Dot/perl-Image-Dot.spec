%global source0_hash 3b6a036e00b2d1146434f1b99fb954e3f4d4cfc0a06c6761e4f554f40f46c584

Name:           perl-Image-Dot
Version:        1.1
Release:        36%{?dist}
Summary:        Create 1x1 pixel image files in pure perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Image-Dot
Source0:        https://cpan.metacpan.org/authors/id/R/RG/RGIERSIG/Image-Dot-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test)

%description
This package provides 1x1 pixel PNG images of a certain RGB color (also
with transparency) without relying on any external modules like GD, libpng
or Compress::Zlib. These pixel dots can be useful in a pure-perl HTTP
server to be able to create colored dots on-the-fly, e.g. for formatting or
drawing purposes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Image-Dot-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
