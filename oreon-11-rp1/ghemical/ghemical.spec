%global source0_hash babb2bda93cf0c20f234452eeb7d19d1d8c0e4c4d611734f110f8de066a1bcb2
Name:			ghemical
Summary:        Molecular mechanics and quantum mechanics front end for GNOME
Version:		3.0.0
Release:        30%{?dist}
License:		GPL-2.0-or-later
URL:			http://www.bioinformatics.org/ghemical/ghemical/index.html
Source0:        http://www.bioinformatics.org/ghemical/download/current/%{name}-%{version}.tar.gz
Patch0:		%{name}-3.0.0-gcc9-friend.patch
Patch1:		%{name}-porting_to_openbabel3.patch
Source11:		%{name}-16x16.png
Source12:		%{name}-32x32.png
Source13:		%{name}-48x48.png
Source14:		%{name}-128x128.png
Requires:		libghemical >= 2.99.1
Requires:		hicolor-icon-theme
Requires:		xorg-x11-fonts-ISO8859-1-100dpi
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  intltool
BuildRequires:  libbonoboui-devel
BuildRequires:  libglade2-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  mopac7-devel
BuildRequires:  mpqc-devel
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtkglext-1.0)
BuildRequires:  pkgconfig(libghemical)
BuildRequires:  pkgconfig(libglade-2.0)
BuildRequires:  pkgconfig(liboglappth)
BuildRequires:  pkgconfig(openbabel-3)
# /oreon:deps
%description
Ghemical is a computational chemistry application.  Ghemical is
written in C++. It has a graphical user interface (in fact, a couple
of them), and it supports both quantum-mechanics (semi-empirical and
ab initio) models and molecular mechanics models (there is an
experimental Tripos 5.2-like force field for organic molecules). Also
a tool for reduced protein models is included. Geometry optimization,
molecular dynamics and a large set of visualization tools are
currently available.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Add ACLOCAL_PATH for gettext 0.25 (ref: bug 2366708)
export ACLOCAL_PATH=%{_datadir}/gettext/m4/
autoreconf -ivf

# fixup character set
iconv -f iso8859-1 -t utf-8 AUTHORS > AUTHORS.conv && \
	touch -r AUTHORS AUTHORS.conv && \
	mv -f AUTHORS.conv AUTHORS

# help : use default xdg-open
sed -i -e "s|mozilla|xdg-open|" src/gtk_app.cpp

cat >%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=Molecular mechanics and quantum mechanics front-end for GNOME
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;GTK;Education;Science;Chemistry;Physics;
Version=1.0
EOF

%build

%configure \
	--enable-threads \
	--enable-openbabel \
	%{nil}
%make_build
%install
%make_install
install -D -p -m 644 %{SOURCE11} %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -D -p -m 644 %{SOURCE12} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -D -p -m 644 %{SOURCE13} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -D -p -m 644 %{SOURCE14} %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
desktop-file-install %{name}.desktop --dir=%{buildroot}%{_datadir}/applications
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
