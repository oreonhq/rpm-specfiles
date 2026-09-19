%global source0_hash ba1f9d494ea2d9875aa5aa5b8d9588cc48d5fed8fcf91932442540eeb1216f36

Name:           xfhell
Version:        3.5.1
Release:        15%{?dist}
Summary:        GTK based Ham Radio application for the Hellschreiber communications mode

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.5b4az.org/
Source0:        http://www.5b4az.org/pkg/%{name}/%{name}-%{version}.tar.bz2
#add .desktop file
Source1:        %{name}.desktop
#temporary Icon
Source2:        %{name}.png

Patch0:         xfhell-Makefile.patch
Patch1: xfhell-configure-c99.patch

BuildRequires: make
BuildRequires:  gcc gcc-c++
BuildRequires:  autoconf, automake, libtool
BuildRequires:  desktop-file-utils
BuildRequires:  alsa-lib-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel

%description
xfhell is a GTK+ application for the "fuzzy" digital amateur radio 
communication mode known as Hellschreiber. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
./autogen.sh
export CFLAGS="%{optflags} `pkg-config --cflags gmodule-2.0`"
export LDFLAGS="%{optflags} -lm `pkg-config --libs gmodule-2.0`"
%configure
%make_build 

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# no upstream .desktop or icon yet
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/
cp -p %{SOURCE2} ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/%{name}.png

desktop-file-install \
        --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}

rm -f %{buildroot}%{_docdir}/%{name}/%{name}.1.gz
mkdir -p %{buildroot}%{_mandir}/man1
cp -a doc/%{name}.1.gz %{buildroot}%{_mandir}/man1/

%files
#Missing copy of the GPL, Notified upstream
%doc AUTHORS ChangeLog README
%doc doc/BDF_Spec.pdf doc/xfhell.html
%{_bindir}/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
