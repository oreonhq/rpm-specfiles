%global source0_hash 807d5b5d4af317c7719d73c892839a3fc9d23af1d911235328d1fa292b7f8a5a

Summary:       Simple word frequency counter
Name:          wf
Version:       0.41
Release:       38%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:       GPL-2.0-only
URL:           http://www.async.com.br/~marcelo/wf/
Source0:       http://www.async.com.br/~marcelo/wf/wf-%{version}.tar.bz2
Patch0:        0001-Fix-usage-of-global-variables.patch
BuildRequires: make
BuildRequires: gcc
%description
wf scans a text file and counts the frequency of words through the
whole text.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/wf
%{_mandir}/man1/wf.1*

%changelog
%autochangelog
