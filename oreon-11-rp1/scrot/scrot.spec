%global source0_hash 1b4b3acadfe07bf89234838675d1d23508a9a6810cb64584f1d9610103d6cdfa
Name:           scrot
Version:        2.0.0
Release:        1%{?dist}
Summary:        Command line screen capture utility
License:        MIT
URL:            https://github.com/resurrecting-open-source-projects/%{name}
Source0:        https://github.com/resurrecting-open-source-projects/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(imlib2)
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
