%global source2_hash 73e1475d5595f97fd374a4e635a05f666ddf10300fc53b3902b2e322740fb730
%global source1_hash 28ca7d948b8deae4cee32919f6f545afee7eec0d39794c7d2e8254a42cd5872b
%global source0_hash 940c557835dfc7aed10ae5cff9b1be562673093e610bc04389e6ac9ad3990945
Name:           dumpasn1
Version:        20250606
Release:        1%{?dist}
Summary:        ASN.1 object dump utility
License:        MIT
URL:            https://github.com/cryptlib/dumpasn1/
Source0:        https://raw.githubusercontent.com/cryptlib/dumpasn1/6667e5725c92505427c30ab054f8a5659ff972e1/dumpasn1.c
Source1:        https://raw.githubusercontent.com/cryptlib/dumpasn1/6667e5725c92505427c30ab054f8a5659ff972e1/dumpasn1.cfg
Source2:        https://raw.githubusercontent.com/cryptlib/dumpasn1/6667e5725c92505427c30ab054f8a5659ff972e1/dumpasn1.1
# oreon:deps
BuildRequires:  gcc
BuildRequires:  sed
# /oreon:deps
%description
dumpasn1 is an ASN.1 object dump program that will dump data encoded
using any of the ASN.1 encoding rules in a variety of user-specified
formats.

%prep

%setup -q -c -T

install -pm 644 %{SOURCE0} %{SOURCE1} %{SOURCE2} .

sed -i -e 's|/etc/dumpasn1/|%{_sysconfdir}/dumpasn1/|' dumpasn1.{c,1}

%build

%{__cc} $RPM_OPT_FLAGS -std=c99 -DDEBIAN -o dumpasn1 dumpasn1.c
%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 755 dumpasn1 $RPM_BUILD_ROOT%{_bindir}/dumpasn1
install -Dpm 644 dumpasn1.cfg \
    $RPM_BUILD_ROOT%{_sysconfdir}/dumpasn1/dumpasn1.cfg
install -Dpm 644 dumpasn1.1 $RPM_BUILD_ROOT%{_mandir}/man1/dumpasn1.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
