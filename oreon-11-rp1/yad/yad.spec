%global source0_hash d5ca05d7658ac45490f1b49e15d24acd2c2011d88dab3f8dab0431ae9f493319

Name:      yad
Version:   9.3
Release:   14%{?dist}
Summary:   Display graphical dialogs from shell scripts or command line

Group:     Applications/System
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:   GPL-3.0-or-later
URL:       http://sourceforge.net/projects/yad-dialog/
Source0:   https://github.com/v1cont/yad/releases/download/v%{version}/yad-%{version}.tar.xz

Patch1:    yad-7.3-size-request.patch

BuildRequires:  make
BuildRequires:  gtk3-devel >= 3.22.0
BuildRequires:  webkit2gtk4.1-devel
BuildRequires:  desktop-file-utils
BuildRequires:  perl(XML::Parser)
BuildRequires:  intltool >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  gettext
BuildRequires:  gtksourceview3-devel
BuildRequires:  gspell-devel

BuildRequires:  gcc

%description
Yad (yet another dialog) is a fork of zenity with many improvements, such as
custom buttons, additional dialogs, pop-up menu in notification icon and more.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1

%build
%configure

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_bindir}/pfd

%find_lang %{name}

# Encoding key in group "Desktop Entry" is deprecated.
# Place the menu entry for yad-icon-browser under "Utilities".
desktop-file-install --remove-key Encoding     \
    --remove-category Development              \
    --add-category    Utility                  \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}-icon-browser.desktop

%post
update-desktop-database %{_datadir}/applications &>/dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
update-desktop-database %{_datadir}/applications &>/dev/null || :
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%doc README.md AUTHORS NEWS THANKS TODO
%license COPYING
%{_bindir}/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/aclocal/%{name}.m4
%{_mandir}/*/*

%changelog
%autochangelog
