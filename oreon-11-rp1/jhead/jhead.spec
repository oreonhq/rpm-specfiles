%global source0_hash 999a81b489c7b2a7264118f194359ecf4c1b714996a2790ff6d5d2f3940f1e9f

Name: jhead
Version: 3.08
Release: 7%{?dist}
Summary: Tool for displaying EXIF data embedded in JPEG images
License: LicenseRef-Fedora-Public-Domain
URL: http://www.sentex.net/~mwandel/jhead/
Source0: https://codeload.github.com/Matthias-Wandel/jhead/tar.gz/refs/tags/%{version}#/jhead-%{version}.tar.gz
Requires: libjpeg-turbo-utils
BuildRequires: gcc
BuildRequires: make

%description
Jhead displays and manipulates the non-image portions of EXIF formatted
JPEG images, such as the images produced by most digital cameras.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"

%install
%{__mkdir_p} ${RPM_BUILD_ROOT}/%{_bindir}
cp -p jhead ${RPM_BUILD_ROOT}/%{_bindir}
%{__mkdir_p} ${RPM_BUILD_ROOT}/%{_mandir}/man1/
cp -p jhead.1 ${RPM_BUILD_ROOT}/%{_mandir}/man1/

%files
%doc readme.txt usage.html changes.txt
%attr(0755,root,root) %{_bindir}/*
%{_mandir}/man?/*

%changelog
%autochangelog
