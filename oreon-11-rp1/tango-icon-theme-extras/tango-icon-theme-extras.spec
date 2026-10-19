%global source0_hash b9252179ea2c546e6bb065281d51373f0ae06081e5a98d4255249af4fa8b33db
Name:		tango-icon-theme-extras
Version:	0.1.0
Release:        1%{?dist}
Summary:        Extra Icons from the Tango Project
License:	LicenseRef-Callaway-CC-BY-SA
URL:		http://tango.freedesktop.org/Tango_Desktop_Project
Source0:        http://tango.freedesktop.org/releases/%{name}-%{version}.tar.gz
Patch0:         tango-icon-theme-extras-0.1.0-rsvg-convert.patch
Patch1:         tango-icon-theme-extras-0.1.0-rsvg-convert-configure.patch
BuildArch:	noarch
Requires:	tango-icon-theme
# oreon:deps
BuildRequires:  ImageMagick-devel
BuildRequires:  icon-naming-utils
BuildRequires:  librsvg2-devel
BuildRequires:  librsvg2-tools
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
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
%oreon_autofiles main

%post

touch --no-create %{_datadir}/icons/Tango 2> /dev/null ||:
gtk-update-icon-cache -q %{_datadir}/icons/Tango 2> /dev/null ||:
%postun

touch --no-create %{_datadir}/icons/Tango 2> /dev/null ||:
gtk-update-icon-cache -q %{_datadir}/icons/Tango 2> /dev/null ||:
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
