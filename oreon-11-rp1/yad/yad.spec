%global source0_hash d5ca05d7658ac45490f1b49e15d24acd2c2011d88dab3f8dab0431ae9f493319
Name:      yad
Version:   9.3
Release:        14%{?dist}
Summary:        Display graphical dialogs from shell scripts or command line
Group:     Applications/System
License:   GPL-3.0-or-later
URL:       http://sourceforge.net/projects/yad-dialog/
Source0:        https://github.com/v1cont/yad/releases/download/v%{version}/yad-%{version}.tar.xz
Patch1:    yad-7.3-size-request.patch
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gspell-devel
BuildRequires:  gtk3-devel
BuildRequires:  gtksourceview3-devel
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig
BuildRequires:  webkit2gtk4.1-devel
# /oreon:deps
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
desktop-file-install --remove-key Encoding     \
    --remove-category Development              \
    --add-category    Utility                  \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}-icon-browser.desktop
%oreon_autofiles main

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
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
