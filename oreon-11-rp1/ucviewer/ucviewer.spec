%global source0_hash ce8d7421e5a8bc451f1856a52bab1a1bc9f02b4f15f05e41576e6188aa1af863
%global svndate	20101019
%global svnrev	4
Name:		ucviewer
Version:	0.1
Release:        1%{?dist}
Summary:        A tool for browsing Unicode tables
License:	GPL-2.0-or-later
URL:		http://sourceforge.net/projects/ucviewer/
Source0:        %{name}-%{svndate}.tar.bz2
Source1:	%{name}.desktop
Patch0:		%{name}-20101019-system-lua.patch
Patch1:		%{name}-20101019-no-prompting.patch
Patch2:         %{name}-20101019-lua_open-to-luaL_newstate.patch
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  qt-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
