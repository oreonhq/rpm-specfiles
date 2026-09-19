%global source0_hash 4eb3906e119b09a7a134e6d7f78c87ec722447f9948e8aa64dcfc7cd3eb6669d

Name:           perl-GPS
Version:        0.17
Release:        32%{?dist}
Summary:        Perl interface to a GPS receiver that implements the Garmin protocol

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/perl-GPS
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SREZIC/perl-GPS-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Device::SerialPort)
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(Device::SerialPort)

%description
This is a perl interface to a GPS receiver that implements the Garmin
protocol.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n perl-GPS-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

for file in $RPM_BUILD_ROOT%{_mandir}/man3/*; do
    iconv -f iso-8859-1 -t utf-8 < "$file" > "${file}_"
    mv "${file}_" "$file"
done

%check
make test

%files
%doc COPYING Changes README TODO
%{perl_vendorlib}/GPS/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
