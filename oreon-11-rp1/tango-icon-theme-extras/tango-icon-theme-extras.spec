%global source0_hash b9252179ea2c546e6bb065281d51373f0ae06081e5a98d4255249af4fa8b33db

Name:		tango-icon-theme-extras
Version:	0.1.0
Release:	33%{?dist}
Summary:	Extra Icons from the Tango Project

# Automatically converted from old format: CC-BY-SA - review is highly recommended.
License:	LicenseRef-Callaway-CC-BY-SA
URL:		http://tango.freedesktop.org/Tango_Desktop_Project

Source0:	http://tango.freedesktop.org/releases/%{name}-%{version}.tar.gz

# https://bugs.freedesktop.org/show_bug.cgi?id=45803
Patch0:         tango-icon-theme-extras-0.1.0-rsvg-convert.patch
Patch1:         tango-icon-theme-extras-0.1.0-rsvg-convert-configure.patch

BuildArch:	noarch

BuildRequires: make
BuildRequires:	icon-naming-utils >= 0.7.2
BuildRequires:	ImageMagick-devel >= 5.5.7
BuildRequires:  librsvg2-devel >= 2.35.2
BuildRequires:  librsvg2-tools
BuildRequires:	pkgconfig >= 0.19

Requires:	tango-icon-theme

## Much of this is from the included README file...
%description
Contains extra icons for from the Tango Project. Currently this includes Tango
icons for iPod Digital Audio Player (DAP) devices and the Dell Pocket DJ DAP.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q 
%patch -P0 -p1
%patch -P1 -p1

%build
%configure --enable-png-creation
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%post
touch --no-create %{_datadir}/icons/Tango 2> /dev/null ||:
gtk-update-icon-cache -q %{_datadir}/icons/Tango 2> /dev/null ||:

%postun
touch --no-create %{_datadir}/icons/Tango 2> /dev/null ||:
gtk-update-icon-cache -q %{_datadir}/icons/Tango 2> /dev/null ||:

%files
%{_datadir}/icons/Tango/*
%doc AUTHORS ChangeLog COPYING README 

%changelog
%autochangelog
