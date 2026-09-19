%global source0_hash 0a5f9e08cd284a1edf0f93dc49a8a7faab86f9795c06116e167043b80ee0bafb

# Multiple files refers to the name "4Pane", not "4pane", so
# let's use 4Pane as %%{name}

# Explicitly declare this, as this package
# really expects this
# (expanded afterwards, use %%define)
%define	_docdir_fmt	%{NAME}

Name:			4Pane
Version:		8.0
Release:		15%{?dist}
Summary:		Multi-pane, detailed-list file manager

# Overall		GPL-3.0-only
# 4Pane.appdata.xml	CC0-1.0
# Accelerators.cpp and etc		LGPL-2.0-or-later (wxWindows)
# sdk/bzip/LICENSE	bzip2-1.0.6 (unused)
# SPDX confirmed
License:		GPL-3.0-only AND LGPL-2.0-or-later AND CC0-1.0
URL:			http://www.4pane.co.uk/
Source0:		http://downloads.sourceforge.net/fourpane/4pane-%{version}.tar.gz
# https://sourceforge.net/p/fourpane/bugs/22/
# https://sourceforge.net/p/fourpane/git4pane/ci/d8b74e4df86fb526ee9caad284b9eb3efe528ac5/
# Make files under /tmp unpredictable
Patch0:		4Pane-d8b74e4-tmp-file-name.patch

BuildRequires:	gcc-c++
BuildRequires:	bzip2-devel
BuildRequires:	xz-devel
BuildRequires:	wxGTK-devel
BuildRequires:  /usr/bin/desktop-file-install
BuildRequires:  /usr/bin/appstream-util
BuildRequires:	gettext
BuildRequires:	git
BuildRequires:	make

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

%if 0
cat > .gitignore <<EOF
configure
config.guess
config.sub
aclocal.m4
config.h.in
EOF

git init
git config user.email "4Pane-maintainers@fedoraproject.org"
git config user.name "4Pane owners"
git add .
git commit -m "base" -q
%endif

sed -i.cflags configure \
	-e '\@[ \t]\{5,\}C.*FLAGS[ \t]*=[ \t]*$@d'

%build
export WX_CONFIG_NAME=$(ls -1 %{_bindir}/wx-config-3.* | sort | tail -n 1)
export EXTRA_CXXFLAGS="%{optflags}"

# --without-builtin_bzip2 means using system bzip2
%configure\
	--disable-desktop \
	--without-builtin_bzip2 || \
	{ sleep 5 ; cat config.log ; sleep 10 ; exit 1; }
%make_build

%install
%make_install

# Some manual installation
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{48x48,32x32}/apps

install -cpm 644 rc/%{name}.desktop %{buildroot}%{_datadir}/applications/
install -cpm 644 bitmaps/%{name}Icon32.xpm %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm
install -cpm 644 bitmaps/%{name}Icon48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

mkdir -p %{buildroot}%{_mandir}/man1
install -cpm 644 4Pane.1 %{buildroot}%{_mandir}/man1/

%find_lang %{name}

# Once remove document and let %%doc re-install them
rm -rf %{buildroot}%{_docdir}/%{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet \
        %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%files -f %{name}.lang
%license	LICENCE
%doc	doc/*
%doc	README
%doc	changelog

%{_bindir}/4pane
%{_bindir}/%{name}

%{_mandir}/man1/%{name}.1*
%{_datadir}/metainfo/%{name}.appdata.xml

%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*

%changelog
%autochangelog
