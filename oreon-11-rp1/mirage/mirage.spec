%global source0_hash d214a1b6d99d1d1e83da5848a2cef181f6781e0990e93f7ebff5880b0c43f43c

Name:		mirage
Version:	0.9.5.2
Release:	53%{?dist}
Summary:	A fast and simple image viewer

# SPDX confirmed
License:	GPL-3.0-or-later
URL:		http://mirageiv.berlios.de/
Source0:	http://download.berlios.de/mirageiv/%{name}-%{version}.tar.bz2
# Fix bug 559853, backtrace when clicking middle button in some case
# Must be sent to upstream
Patch0:		mirage-0.9.3-prevmouse-not-defined-with-click.patch
# Don't call gtk.gdk.threads_init() on GLib >= 2.41,
# workaround for bug 1123953
Patch1:		mirage-0.9.5.2-glib241-init-workaround.patch
# Port to python3 + pygi + gtk3
Patch10:		mirage-0.9.5.2-py3-gtk3.patch
# Port to setuptools: PEP632
Patch11:		mirage-0.9.5.2-pep632-distutils-port.patch

BuildRequires:	gcc
BuildRequires:	gettext
BuildRequires:	libX11-devel
BuildRequires:	python3-devel
BuildRequires:	desktop-file-utils
Requires:	gtk3
Requires:	python3-gobject
Requires:	python3-cairo

%description
Mirage is a fast and simple GTK+ image viewer. Because it 
depends only on PyGTK, Mirage is ideal for users who wish to 
keep their computers lean while still having a clean image viewer.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .bt_prevmouse -Z
%patch -P1 -p1 -b .glib241 -Z
# Don't remove rebuilt files!
%{__sed} -i.build -e '/Cleanup/,$d' setup.py

%patch -P10 -p1 -b .py3 -Z
%patch -P11 -p1 -b .pep632 -Z

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%{__rm} -rf $RPM_BUILD_ROOT

%{__mkdir_p} $RPM_BUILD_ROOT
%pyproject_install

# remove document files
%{__rm} -f $RPM_BUILD_ROOT%{_datadir}/%{name}/[A-Z]*

# install desktop file
%{__sed} -i -e 's|%{name}.png|%{name}|' \
	$RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
desktop-file-install \
	--delete-original \
	--remove-category 'Application' \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	$RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

# gettext files
%{find_lang} %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc CHANGELOG
%license COPYING
%doc README
%doc TODO
%doc TRANSLATORS

%{_bindir}/%{name}
%{python3_sitearch}/%{name}.py*
%{python3_sitearch}/*%{version}.*-info
%{python3_sitearch}/*.so
%{python3_sitearch}/__pycache__/%{name}*

%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*.png
%{_datadir}/pixmaps/*.png

%{_datadir}/applications/*%{name}.desktop

%changelog
%autochangelog
