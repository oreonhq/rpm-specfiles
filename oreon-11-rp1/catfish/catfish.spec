%global source0_hash fe00d45b163cf86b4c85ebdd23a73d53aa55bc97ba3f691a248ec403d4ade62b
%define BothRequires() \
Requires:		%1 \
%{nil}
%global		native_wayland	1
%global		majorver		4.20
%define		mainver		4.20.1
%undefine		betaver		
%define		baserelease		7
Name:		catfish
Version:	%{mainver}
Release:        7%{?dist}
Summary:        A handy file search tool
License:	GPL-2.0-only
URL:		https://docs.xfce.org/apps/catfish/start
Source0:        https://archive.xfce.org/src/apps/%{name}/%{majorver}/%{name}-%{version}.tar.xz
BuildArch:	noarch
%BothRequires	python3-gobject
%BothRequires	python3-pexpect
%BothRequires	python3-dbus
Requires:	gdk-pixbuf2
Requires:	glib2 >= 2.25.0
Requires:	gobject-introspection
Requires:	gtk3 >= 3.22.0
Requires:	pango >= 1.38.0
Requires:	xfconf >= 4.16.0
Requires:	shared-mime-info
Requires:	%{_bindir}/xdg-open
Requires:	%{_bindir}/locate
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  python3-dbus
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-pexpect
# /oreon:deps
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

grep -rl "/usr/bin/env" . | \
	xargs sed -i -e "\@/usr/bin/env[ ][ ]*python@d"
%meson
%meson_build
%install
%meson_install
%if ! 0%{?native_wayland}
mkdir %{buildroot}%{_libexecdir}
mv %{buildroot}%{_bindir}/catfish %{buildroot}%{_libexecdir}/
cat > %{buildroot}%{_bindir}/catfish <<EOF
export GDK_BACKEND=x11
exec %{_libexecdir}/catfish \$@
EOF
chmod 0755 %{buildroot}%{_bindir}/catfish
%endif
%{__mkdir_p} %{buildroot}%{_mandir}/man1
%{__install} -cpm 0644 ./%{name}.1 %{buildroot}%{_mandir}/man1/
%{__rm} -rf %{buildroot}%{_datadir}/doc/
%{find_lang} %{name}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.xfce.Catfish.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
