%global source0_hash 55da78fccf4c19d3d173fab38fc6ce6df0078f839a8a3e699199e4ef19428803

Name:           perl-Image-Xpm
Version:        1.13
Release:        28%{?dist}
Summary:        Load, create, manipulate and save xpm image files in Perl
License:        GPL-1.0-or-later
URL:            https://metacpan.org/release/Image-Xpm
Source0:        https://cpan.metacpan.org/authors/id/S/SU/SUMMER/Image-Xpm-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Image::Base)
BuildRequires:  perl(ExtUtils::MakeMaker)

Provides:       perl(Image::Xpm)
%description
This class module provides basic load, manipulate and save functionality for
the xpm file format.  It inherits from Image::Base which provides additional
manipulation functionality.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Image-Xpm-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc README
%{perl_vendorlib}/Image/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
