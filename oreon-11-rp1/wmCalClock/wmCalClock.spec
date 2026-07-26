%global source0_hash 6067d30a9a26e263bf555c591439ed93805a3ed803d1c30b5f152223f7412648

Name:           wmCalClock
Version:        1.26
Release:        %autorelease
Summary:        A Calendar clock with antialiased text

License:        GPL-2.0-or-later
URL:            https://www.dockapps.net/wmcalclock
Source0:        https://www.dockapps.net/download/wmcalclock-%{version}.tar.xz

Patch0:         1.26-fix-KnR-prototypes.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXpm-devel
BuildRequires:  git-core

%description
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n wmcalclock-%{version} -S git

%build
%configure
%make_build
 
%install
%make_install

%files
%doc BUGS CHANGES HINTS README TODO
%license COPYING
%{_bindir}/wmCalClock
%{_mandir}/man1/wmCalClock.1*

%changelog
%autochangelog
