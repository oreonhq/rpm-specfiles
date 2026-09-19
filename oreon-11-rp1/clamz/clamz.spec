%global source0_hash 5a63f23f15dfa6c2af00ff9531ae9bfcca0facfe5b1aa82790964f050a09832b

Name:           clamz
Version:        0.5
Release:        35%{?dist}
Summary:        Amazon MP3 Music Store Downloader
License:        GPL-3.0-or-later
URL:            https://code.google.com/archive/p/clamz/
Source0:        https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/clamz/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  libcurl-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  expat-devel
BuildRequires:  make

%description
Clamz is a little command-line program to download MP3 files from
Amazon.com's music store.  It is intended to serve as a substitute
for Amazon's official MP3 Downloader, which is not free software (and
therefore is only available in binary form for a limited set of
platforms.)  Clamz can be used to download either individual songs or
complete albums that you have purchased from Amazon.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure
%make_build

%install
%make_install UPDATE_MIME_DATABASE=: UPDATE_DESKTOP_DATABASE=:

%files
%doc README
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml

%changelog
%autochangelog
