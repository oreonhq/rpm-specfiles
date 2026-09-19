%global source0_hash fe00d45b163cf86b4c85ebdd23a73d53aa55bc97ba3f691a248ec403d4ade62b

%define BothRequires() \
Requires:		%1 \
BuildRequires:	%1 \
%{nil}

%global		native_wayland	1

%global		majorver		4.20
%define		mainver		4.20.1
%undefine		betaver		

%define		baserelease		7

Name:		catfish
Version:	%{mainver}
Release:	%{?betaver:0.}%{baserelease}%{?betaver:.%betaver}%{?dist}
Summary:	A handy file search tool

# SPDX confirmed
License:	GPL-2.0-only
URL:		https://docs.xfce.org/apps/catfish/start
Source0:	https://archive.xfce.org/src/apps/catfish/%{majorver}/catfish-%{version}%{?betaver}.tar.xz
BuildArch:	noarch

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	intltool

BuildRequires:	python3-devel
BuildRequires:	meson
BuildRequires:	/usr/bin/appstream-util

# python module
%BothRequires	python3-gobject
%BothRequires	python3-pexpect
%BothRequires	python3-dbus

# gir repository
Requires:	gdk-pixbuf2
Requires:	glib2 >= 2.25.0
Requires:	gobject-introspection
Requires:	gtk3 >= 3.22.0
Requires:	pango >= 1.38.0
Requires:	xfconf >= 4.16.0
# optional zeitgeist dependency not listed
# /usr/share/mime/globs2
Requires:	shared-mime-info
# opening file uses this
Requires:	%{_bindir}/xdg-open
# search engine
Requires:	%{_bindir}/locate
# icon
# Requires:	redhat-artwork

%description
Catfish is a handy file searching tool. The interface is
intentionally lightweight and simple, using only GTK+3.
You can configure it to your needs by using several command line
options.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{mainver}%{?betaver}

# Fix up permissions...
find . -type f -print0 | xargs --null chmod 0644
chmod 0755 bin/%{name}

# Remove build time dependency
sed -i meson.build \
	-e '\@dependency@s|,[ \t]*required[^)]*||'
sed -i meson.build \
	-e '\@dependency@s|)|, required: false)|' \
	%{nil}

%build
# Remove unneeded shebang
grep -rl "/usr/bin/env" . | \
	xargs sed -i -e "\@/usr/bin/env[ ][ ]*python@d"

%meson
%meson_build

%install
%meson_install

# Explicitly set GDK_BACKEND
%if ! 0%{?native_wayland}
# Release notes says 1.4.12 has wayland support
# But 4.16.0 gets wayland error again:
# https://bugzilla.redhat.com/show_bug.cgi?id=1920378
# https://gitlab.xfce.org/apps/catfish/-/issues/42

mkdir %{buildroot}%{_libexecdir}
mv %{buildroot}%{_bindir}/catfish %{buildroot}%{_libexecdir}/
cat > %{buildroot}%{_bindir}/catfish <<EOF
#!/usr/bin/bash

export GDK_BACKEND=x11
exec %{_libexecdir}/catfish \$@
EOF
chmod 0755 %{buildroot}%{_bindir}/catfish

%endif

# for backwards compatibility:
%if 0%{?fedora} <= 41
ln -s catfish %{buildroot}%{_bindir}/catfish-py3
%endif

# Install man page manually
%{__mkdir_p} %{buildroot}%{_mandir}/man1
%{__install} -cpm 0644 ./%{name}.1 %{buildroot}%{_mandir}/man1/

# Remove all unnecessary documentation
%{__rm} -rf %{buildroot}%{_datadir}/doc/

%{find_lang} %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.xfce.Catfish.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files -f %{name}.lang
%doc AUTHORS
%doc NEWS
%doc README.md
%license COPYING
%{_bindir}/%{name}
%if 0%{?fedora} <= 41
%{_bindir}/%{name}-py3
%endif

%if ! 0%{?native_wayland}
%{_libexecdir}/%{name}
%endif

%{_mandir}/man1/%{name}.1*
%dir	%{_datadir}/%{name}/
%{_datadir}/%{name}/ui/
%{_datadir}/icons/hicolor/*/apps/org.xfce.%{name}.*
%{_datadir}/applications/org.xfce.Catfish.desktop
%{_metainfodir}/%{name}.appdata.xml
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}_lib/

%changelog
%autochangelog
