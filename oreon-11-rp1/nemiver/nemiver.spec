%global source0_hash 85ab8cf6c4f83262f441cb0952a6147d075c3c53d0687389a3555e946b694ef2
Name:		nemiver
Version:	0.9.6
Release:        28%{?dist}
Summary:        A GNOME C/C++ Debugger
License:	GPL-2.0-or-later
URL:		http://projects.gnome.org/nemiver
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.9/%{name}-%{version}.tar.xz
Patch0:		0001-Fix-compiliation-warnings-errors.patch
Patch1:		0001-Use-RefPtr-bool-operator-in-the-conditions.patch
Requires: gsettings-desktop-schemas
Requires:	hicolor-icon-theme
Requires:	gdb
Provides: %{name}-devel = %{version}-%{release}
Provides: %{name}-headers = %{version}-%{release}
Obsoletes:	%{name}-devel < 0.5.4-1
Obsoletes:	%{name}-headers < 0.6.5-2
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  boost-static
BuildRequires:  dconf
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  gdlmm-devel
BuildRequires:  gettext
BuildRequires:  ghex-devel
BuildRequires:  glib2-devel
BuildRequires:  glibmm24-devel
BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:  gtkmm30-devel
BuildRequires:  gtksourceviewmm3-devel
BuildRequires:  intltool
BuildRequires:  libgtop2-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  perl(XML::Parser)
BuildRequires:  sqlite-devel
BuildRequires:  vte291-devel
BuildRequires:  yelp-tools
# /oreon:deps
%description
Nemiver is an ongoing effort to write a standalone graphical debugger that
integrates well in the GNOME desktop environment. It currently features a
backend which uses the well known GNU Debugger (gdb) to debug C/C++ programs.

The yelp package must be installed to make use of Nemiver's documentation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build

%configure --disable-static --disable-schemas-install  --disable-scrollkeeper 
make %{?_smp_mflags} LIBTOOL=%{_bindir}/libtool
%install
rm -rf %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}
desktop-file-install                                    \
	--dir %{buildroot}%{_datadir}/applications	\
	--remove-category=Application			\
	--delete-original				\
	%{buildroot}/%{_datadir}/applications/%{name}.desktop
%ldconfig_scriptlets
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
