%global source0_hash a9121dc7d88c38986c9a794994acfb67cb5d2dea70140299ebfb4f468ed37898

Name:           perl-Data-AMF
Version:        0.09
Release:        42%{?dist}
Summary:        Serialize/deserialize Adobe's AMF (ActionMessageFormat) data
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/pod/release/TYPESTER/Data-AMF-0.09/lib/Data/AMF.pm
Source0:        https://cpan.metacpan.org/authors/id/T/TY/TYPESTER/Data-AMF-0.09.tar.gz
BuildArch:      noarch
Patch0:         Data-AMF-0.09-Fix-building-on-Perl-without-dot-in-INC.patch

BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Any::Moose)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Spiffy)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(YAML)
BuildRequires:  sed

Requires:       perl(DateTime)
Requires:       perl(XML::LibXML)

%{?perl_default_filter}

%description
This module is a (de-)serializer for Adobe's AMF (Action Message Format).
Data::AMF is core module and it recognizes only AMF data, not AMF packet.
If you want to read/write AMF Packet, see Data::AMF::Packet instead.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-AMF-%{version}
%patch -P0 -p1
rm inc/YAML.pm
sed -i -e '/^inc\/YAML.pm$/d' MANIFEST
echo VENDORLIB %{perl_vendorlib}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
