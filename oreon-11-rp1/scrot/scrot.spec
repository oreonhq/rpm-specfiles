%global source0_hash 45bed70abd74ffeeec08b75089ba44900291e9c86309bcce892ccc7ece8f1e61

Name:           scrot
Version:        1.12.1
Release:        %autorelease
Summary:        Command line screen capture utility

License:        MIT
URL:            https://github.com/resurrecting-open-source-projects/%{name}
Source0:        %{URL}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  pkgconfig(imlib2) pkgconfig(libbsd) pkgconfig(x11) pkgconfig(xext) pkgconfig(xcomposite) pkgconfig(xinerama)

%description
scrot is a simple command line screen capture utility.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
autoreconf -if

%configure
%make_build

%install
%make_install

%files
%doc AUTHORS ChangeLog README.md scrot.png FAQ.md CONTRIBUTING.md TODO.md
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
