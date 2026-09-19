%global source0_hash bf1d4d3af02255f77c0ce96865e6fcb96e258f5ae4eaa28fc27c920f3d3de71f

Name:           perl-ConfigReader
Version:        0.5
Release:        48%{?dist}
Summary:        Read directives from a configuration file
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/ConfigReader
Source0:        https://cpan.metacpan.org/modules/by-module/ConfigReader/ConfigReader-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
The ConfigReader library is a set of classes which reads directives from a
configuration file. The library is completely object oriented, and it is
envisioned that parsers for new styles of configuration files can be
easily added.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ConfigReader-%{version}

%build
pod2man ConfigReader.pod ConfigReader.3

%install
set -x
rm -rf %{buildroot}

install -m 644 -D DirectiveStyle.pm %{buildroot}%{perl_vendorlib}/ConfigReader/DirectiveStyle.pm
install -m 644 -D Spec.pm %{buildroot}%{perl_vendorlib}/ConfigReader/Spec.pm
install -m 644 -D Values.pm %{buildroot}%{perl_vendorlib}/ConfigReader/Values.pm
install -m 644 -D ConfigReader.3 %{buildroot}%{_mandir}/man3/ConfigReader.3

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%files
%doc COPYING.LIB README
%{perl_vendorlib}/ConfigReader
%{_mandir}/man3/ConfigReader.3*

%changelog
%autochangelog
