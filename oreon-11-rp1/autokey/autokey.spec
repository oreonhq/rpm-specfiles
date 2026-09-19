%global source0_hash 40341fc4cd9703a34264e9191b5938fc7ed5a6f357992d91e492975d89933acd

%{?python_enable_dependency_generator}
Name:		autokey
Version:	0.96.0
Release:	16%{?dist}
Summary:	Desktop automation utility

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		https://github.com/autokey/autokey
Source0:	https://github.com/autokey/autokey/archive/v%{version}.tar.gz
Patch0:		0001-scripting-Remove-dependency-on-imghdr.patch

BuildArch:	noarch
BuildRequires:	python3-devel,python3-xlib,python3-inotify,python3-dbus,python3-setuptools,python3-qt5-devel

%description
AutoKey is a desktop automation utility for Linux and X11. It allows
the automation of virtually any task by responding to typed abbreviations
and hot keys. It offers a full-featured GUI that makes it highly
accessible for novices, as well as a scripting interface offering
the full flexibility and power of the Python language.

%package common
Summary:	Desktop automation utility - common data
Requires:	python3-dbus
Requires:	python3-file-magic
Requires:	wmctrl
Provides:	autokey = %{version}-%{release}

%description common
This package contains the common data shared between the various front ends.

%package gtk
Summary:	AutoKey GTK+ front end
Requires:	libappindicator-gtk3
Requires:	python3-gobject
Requires:	gtksourceview3
Requires:	zenity
Requires:	autokey-common = %{version}-%{release}
Provides:	autokey = %{version}-%{release}
%description gtk
This package contains the GTK+ front end for autokey

%package qt
Summary:	AutoKey QT front end
Requires:	python3-qscintilla-qt5
Requires:	python3-qt5
Requires:	autokey-common = %{version}-%{release}
Provides:	autokey = %{version}-%{release}
%description qt
This package contains the QT front end for autokey

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
%patch 0 -p 1

%build
%{__python3} setup.py build

%install
rm -rf %{buildroot}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot} --prefix %{_prefix}

# remove shebang from python libraries
for lib in $(find %{buildroot}%{python3_sitelib}/autokey/ -name "*.py"); do
 sed '/\/usr\/bin\/env/d' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

# ensure pkg_resources is able to find the required python packages
 sed -i 's/python3-xlib/python-xlib/' %{buildroot}%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info/requires.txt

%files common
%doc ACKNOWLEDGMENTS README.rst new_features.rst CHANGELOG.rst
%{python3_sitelib}/*
%exclude %{python3_sitelib}/autokey/gtkapp.py*
%exclude %{python3_sitelib}/autokey/gtkui/*
%exclude %{python3_sitelib}/autokey/qtapp.py*
%exclude %{python3_sitelib}/autokey/qtui/*
%{_datadir}/icons/*
%{_bindir}/autokey-run
%{_bindir}/autokey-shell
%{_mandir}/man1/autokey-run.1*

%files gtk
%{_bindir}/autokey-gtk
%{python3_sitelib}/autokey/gtkapp.py*
%{python3_sitelib}/autokey/gtkui/*
%{_datadir}/applications/autokey-gtk.desktop
%{_mandir}/man1/autokey-gtk.1*

%files qt
%{_bindir}/autokey-qt
%{python3_sitelib}/autokey/qtapp.py*
%{python3_sitelib}/autokey/qtui/*
%{_datadir}/applications/autokey-qt.desktop
%{_mandir}/man1/autokey-qt.1*

%changelog
%autochangelog
