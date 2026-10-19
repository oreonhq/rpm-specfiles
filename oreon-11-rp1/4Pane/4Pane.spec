%global source0_hash 0a5f9e08cd284a1edf0f93dc49a8a7faab86f9795c06116e167043b80ee0bafb
%define	_docdir_fmt	%{NAME}
Name:			4Pane
Version:		8.0
Release:        15%{?dist}
Summary:        Multi-pane, detailed-list file manager
License:		GPL-3.0-only AND LGPL-2.0-or-later AND CC0-1.0
URL:			http://www.4pane.co.uk/
Source0:        http://downloads.sourceforge.net/fourpane/4pane-%{version}.tar.gz
Patch0:		4Pane-d8b74e4-tmp-file-name.patch
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-install
BuildRequires:  bzip2-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  make
BuildRequires:  wxGTK-devel
BuildRequires:  xz-devel
# /oreon:deps
%description
4Pane is a multi-pane, detailed-list file manager. It is designed
to be fully-featured without bloat, and aims for speed rather than
visual effects.
In addition to standard file manager things, it offers multiple
undo and redo of most operations (including deletions), archive
management including 'virtual browsing' inside archives, multiple
renaming/duplication of files, a terminal emulator and user-defined
tools.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n 4pane-%{version}
%patch -P0 -p1 -b .tmpfile

sed -i.cflags configure \
	-e '\@[ \t]\{5,\}C.*FLAGS[ \t]*=[ \t]*$@d'

%build

export WX_CONFIG_NAME=$(ls -1 %{_bindir}/wx-config-3.* | sort | tail -n 1)
export EXTRA_CXXFLAGS="%{optflags}"
%configure\
	--disable-desktop \
	--without-builtin_bzip2 || \
	{ sleep 5 ; cat config.log ; sleep 10 ; exit 1; }
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{48x48,32x32}/apps
install -cpm 644 rc/%{name}.desktop %{buildroot}%{_datadir}/applications/
install -cpm 644 bitmaps/%{name}Icon32.xpm %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm
install -cpm 644 bitmaps/%{name}Icon48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
mkdir -p %{buildroot}%{_mandir}/man1
install -cpm 644 4Pane.1 %{buildroot}%{_mandir}/man1/
%find_lang %{name}
rm -rf %{buildroot}%{_docdir}/%{name}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet \
        %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
