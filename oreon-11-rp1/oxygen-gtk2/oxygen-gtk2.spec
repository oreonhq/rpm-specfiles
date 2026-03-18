
%undefine __cmake_in_source_build

Name:    oxygen-gtk2
Summary: Oxygen GTK+2 theme
Version: 1.4.6
Release: 31%{?dist}

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     https://cgit.kde.org/oxygen-gtk.git/
Source0: http://download.kde.org/stable/oxygen-gtk2/%{version}/src/%{name}-%{version}.tar.bz2

## upstream patches

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gtk2-devel

Obsoletes: oxygen-gtk < 1.2.1

%description
Oxygen-Gtk is a port of the default KDE widget theme (Oxygen), to gtk.

It's primary goal is to ensure visual consistency between gtk-based and
qt-based applications running under KDE. A secondary objective is to also
have a stand-alone nice looking gtk theme that would behave well on other
Desktop Environments.

Unlike other attempts made to port the KDE oxygen theme to gtk, this
attempt does not depend on Qt (via some Qt to Gtk conversion engine), 
nor does render the widget appearance via hard-coded pixmaps, which 
otherwise breaks every time some setting is changed in KDE.


%prep
%autosetup


%build
# TODO: Please submit an issue to upstream (rhbz#2381350)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake \
  -DOXYGEN_FORCE_KDE_ICONS_AND_FONTS=0

%cmake_build


%install
%cmake_install


%files
%doc AUTHORS README
%license COPYING
%{_bindir}/oxygen-gtk-demo
%{_libdir}/gtk-2.0/*/engines/liboxygen-gtk.so
%{_datadir}/themes/oxygen-gtk/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.6-31
- Prepare for Oreon 11 (RP1)
