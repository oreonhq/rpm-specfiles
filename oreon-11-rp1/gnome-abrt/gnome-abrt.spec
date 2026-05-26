# TODO: https://fedoraproject.org/wiki/Packaging:AutoProvidesAndRequiresFiltering
#       rpmlint warns about private-shared-object-provides
#       can't use filter because the package doesn't met any of the required criteria
#         ! Noarch package       ... caused by libreport wrappers shared library
#         ! no binaries in $PATH ... caused by gnome-abrt python script in /usr/bin

# Uncomment when building from a git snapshot.
#%%global snapshot 1
%global commit 3e3512d2d6c81a4ca9b3b4d3f3936c876a6482f7
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:       gnome-abrt
Version:    1.4.3
Release:    9%{?snapshot:.git%{shortcommit}}%{?dist}
Epoch:      1
Summary:    A utility for viewing problems that have occurred with the system

License:    GPL-2.0-or-later
URL:        https://github.com/abrt/%{name}
%if 0%{?snapshot}
Source0:        https://github.com/abrt/gnome-abrt/archive/1.4.3/gnome-abrt-1.4.3.tar.gz
%else
Source0:        https://github.com/abrt/gnome-abrt/archive/1.4.3/gnome-abrt-1.4.3.tar.gz
# oreon url source checksums begin
%global source0_sha256 38fe08b8e1a3e5c6e7f2265be0e655804e0741258d753653d31bd8d36199f8e1
%global source0_file gnome-abrt-1.4.3.tar.gz
# oreon url source checksums end
%endif

BuildRequires: git-core
BuildRequires: meson >= 0.59.0
BuildRequires: gettext
BuildRequires: libtool
BuildRequires: python3-devel
BuildRequires: desktop-file-utils
BuildRequires: asciidoc
BuildRequires: xmlto
BuildRequires: pkgconfig(pygobject-3.0)
BuildRequires: libreport-gtk-devel > 2.14.0
BuildRequires: python3-libreport
BuildRequires: abrt-gui-devel > 2.14.0
BuildRequires: gtk3-devel
%if 0%{?fedora}
BuildRequires: python3-six
BuildRequires: python3-gobject
BuildRequires: python3-dbus
BuildRequires: python3-humanize
%endif

Requires:   glib2%{?_isa} >= 2.63.2
Requires:   gobject-introspection%{?_isa} >= 1.63.1
Requires:   python3-libreport
Requires:   python3-gobject
Requires:   python3-dbus
Requires:   python3-humanize
Requires:   python3-beautifulsoup4

%description
A GNOME application allows users to browse through detected problems and
provides them with convenient way for managing these problems.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/gnome-abrt-1.4.3.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "38fe08b8e1a3e5c6e7f2265be0e655804e0741258d753653d31bd8d36199f8e1" || { echo "oreon: Source0 SHA256 mismatch for gnome-abrt-1.4.3.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -S git %{?snapshot:-n %{name}%-%{commit}}


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name}

%check
%meson_test


%files -f %{name}.lang
%doc COPYING README.md
%{python3_sitearch}/gnome_abrt
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/metainfo/*
%{_mandir}/man1/%{name}.1*
%{_datadir}/icons/hicolor/*/apps/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.3-9
- Prepare for Oreon 11 (RP1)
