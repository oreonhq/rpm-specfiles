%global source0_hash ce8d7421e5a8bc451f1856a52bab1a1bc9f02b4f15f05e41576e6188aa1af863

%global svndate	20101019
%global svnrev	4

Name:		ucviewer
# The only place I could find a version was in the documentation.
Version:	0.1
Release:	0.36.%{svndate}svn%{svnrev}%{?dist}
Summary:	A tool for browsing Unicode tables
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://sourceforge.net/projects/ucviewer/
# Upstream does not release versioned tarballs
# Also, they bundle a copy of lua. :P
# svn export https://ucviewer.svn.sourceforge.net/svnroot/ucviewer ucviewer-20101019
# rm -rf ucviewer-20101019/src/lua-5.1.4
# tar cfj ucviewer-20101019.tar.bz2 ucviewer-20101019
Source0:	%{name}-%{svndate}.tar.bz2
# Desktop file not provided by upstream
Source1:	%{name}.desktop
# Use system lua
Patch0:		%{name}-20101019-system-lua.patch
# Don't prompt on buildtype (and use sane system paths)
Patch1:		%{name}-20101019-no-prompting.patch
# lua_open() changed to luaL_newstate()
Patch2:         %{name}-20101019-lua_open-to-luaL_newstate.patch
BuildRequires: make
BuildRequires:	lua-devel, qt-devel
BuildRequires:	desktop-file-utils
BuildRequires:  gcc-c++

%description
Unicode Viewer is a tool for browsing Unicode tables to obtain detailed
information about every glyph. It provides a GUI with multiple functions
for navigating through the data and a Lua scripting interface to create
new functions. It also displays each glyph's DUCET-information and
allows sorting according to an order specified in an allkeys.txt-File.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{svndate}
%patch -P0 -p1 -b .system
%patch -P1 -p1 -b .no-prompting
%patch -P2 -p1 -b .lua_open

%build
%{qmake_qt4}
make %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install
mkdir %{buildroot}%{_datadir}/pixmaps
pushd %{buildroot}%{_datadir}/pixmaps
ln -s ../UnicodeViewer/icon/uc-book.png .
popd
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

%files
%doc ReadMe.txt
%license License.txt
%{_bindir}/UnicodeViewer
%{_datadir}/applications/ucviewer.desktop
%{_datadir}/pixmaps/uc-book.png
%{_datadir}/UnicodeViewer/

%changelog
%autochangelog
