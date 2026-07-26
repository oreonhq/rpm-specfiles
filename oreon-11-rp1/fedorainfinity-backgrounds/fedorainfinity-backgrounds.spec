%global source0_hash 30747b78660bd88359c4c3caa2d80dbd42a7c38dc9ca7423dc34827c536fd1f0

Name:		fedorainfinity-backgrounds
Version:	0.0.5    
Release:	34%{?dist}
Summary:	Fedora Infinity desktop backgrounds
URL:		http://fedoraproject.org/wiki/Artwork/F8Themes/Infinity

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2
Source0:	desktop-backgrounds-infinity-%{version}.tar.bz2
BuildArch:	noarch

%description
This package contains desktop backgrounds for the Fedora Infinity theme, 
which was the default theme for Fedora 8.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n desktop-backgrounds-infinity-%{version}

%install
# copy image files
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/share/backgrounds/infinity
cp -a $RPM_BUILD_DIR/desktop-backgrounds-infinity-%{version}/*.png \
	$RPM_BUILD_ROOT/%{_prefix}/share/backgrounds/infinity
# copy slideshow xml file
cp -a $RPM_BUILD_DIR/desktop-backgrounds-infinity-%{version}/infinity.xml \
	$RPM_BUILD_ROOT/%{_prefix}/share/backgrounds/infinity
# copy metadata xml file for GNOME
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/share/gnome-background-properties
cp -a $RPM_BUILD_DIR/desktop-backgrounds-infinity-%{version}/desktop-backgrounds-infinity.xml \
	$RPM_BUILD_ROOT/%{_prefix}/share/gnome-background-properties
# copy metadata xml file for MATE
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/share/mate-background-properties
ln -s ../gnome-background-properties/desktop-backgrounds-infinity.xml \
	$RPM_BUILD_ROOT/%{_prefix}/share/mate-background-properties

%files
%license COPYING
%{_datadir}/backgrounds/infinity
%{_datadir}/gnome-background-properties
%{_datadir}/mate-background-properties

%changelog
%autochangelog
