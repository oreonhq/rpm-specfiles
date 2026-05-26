Name:           voikko-fi
Version:        2.5
Release:        10%{?dist}
Summary:        A description of Finnish morphology written for libvoikko

License:        GPL-2.0-or-later
URL:            https://voikko.puimula.org/

# See https://voikko.puimula.org/sources.html for the key fingerprint.
# I did
#  gpg --recv-keys "AC5D 65F1 0C85 96D7 E2DA  E263 3D30 9B60 4AE3 942E"
# and then
#  gpg2 --export --export-options export-minimal AC5D65F10C8596D7E2DAE2633D309B604AE3942E > gpgkey-AC5D65F10C8596D7E2DAE2633D309B604AE3942E.gpg
Source0:        https://www.puimula.org/voikko-sources/%{name}/%{name}-%{version}.tar.gz
Source1:        https://www.puimula.org/voikko-sources/%{name}/%{name}-%{version}.tar.gz.asc
Source2:        gpgkey-AC5D65F10C8596D7E2DAE2633D309B604AE3942E.gpg
# oreon url source checksums begin
%global source0_sha256 3bc9b0a0562526173957bf23b5caaf57b60ecc53be63fc16874118002ec620f1
%global source0_file voikko-fi-2.5.tar.gz
# oreon url source checksums end

BuildRequires:  make
BuildRequires:  gnupg2
BuildRequires:  python3-devel
BuildRequires:  foma
# Voikko 4.3 and beyond on Fedora supports this format of the data files
BuildRequires:  voikko-tools >= 4.3

# Installing this package without libvoikko would be useless.
Requires:       libvoikko >= 4.3

BuildArch:      noarch

# This package replaces malaga-suomi-voikko
Provides:       malaga-suomi-voikko = %{version}-%{release}
Obsoletes:      malaga-suomi-voikko < 1.19-20

%description
Voikko-fi is a description of Finnish morphology written for libvoikko.
The implementation uses unweighted VFST format and provides format 5 Finnish
dictionary for libvoikko 4.0 or later. For Voikko the morphology supports
spell checking, hyphenation and grammar checking.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/voikko-fi-2.5.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3bc9b0a0562526173957bf23b5caaf57b60ecc53be63fc16874118002ec620f1" || { echo "oreon: Source0 SHA256 mismatch for voikko-fi-2.5.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%make_build vvfst

%install
# Upstream uses /usr/lib/voikko as the data file location.
# Zbigniew Jędrzejewski-Szmek recommended using the upstream default on the
# mailing list, see
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/GY6NGGNLK5DIDXOXVGBDA5QONISQOFL7/
make vvfst-install DESTDIR=$RPM_BUILD_ROOT%{_prefix}/lib/voikko


%files
%doc ChangeLog CONTRIBUTORS README.md
%license COPYING
%{_prefix}/lib/voikko/5

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5-10
- Prepare for Oreon 11 (RP1)
