%global source1_hash 2d060ed234a432dbc9d9f3953d28e457c8f939e2bc3833acd269a060b145ddab
%global source0_hash 5c147c1c92323941e5847b5c46d00b35ff6b62dc3cf348516bc0fbdc87340220
%global source2_key_fpr AC5D65F10C8596D7E2DAE2633D309B604AE3942E
Name:           voikko-fi
Version:        2.6
Release:        1%{?dist}
Summary:        A description of Finnish morphology written for libvoikko
License:        GPL-2.0-or-later
URL:            https://voikko.puimula.org/
Source0:        https://www.puimula.org/voikko-sources/%{name}/%{name}-%{version}.tar.gz
Source1:        https://www.puimula.org/voikko-sources/%{name}/%{name}-%{version}.tar.gz.asc
Source2:        gpgkey-AC5D65F10C8596D7E2DAE2633D309B604AE3942E.gpg
Requires:       libvoikko >= 4.3
BuildArch:      noarch
Provides:       malaga-suomi-voikko = %{version}-%{release}
Obsoletes:      malaga-suomi-voikko < 1.19-20
# oreon:deps
BuildRequires:  foma
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  voikko-tools
# /oreon:deps
%description
Voikko-fi is a description of Finnish morphology written for libvoikko.
The implementation uses unweighted VFST format and provides format 5 Finnish
dictionary for libvoikko 4.0 or later. For Voikko the morphology supports
spell checking, hyphenation and grammar checking.

%prep

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build

%make_build vvfst
%install
make vvfst-install DESTDIR=$RPM_BUILD_ROOT%{_prefix}/lib/voikko
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5-10
- Prepare for Oreon 11 (RP1)
