%global source0_hash 4380d570a8bf27b81fb629c97a636c1673407f4ac4989ce931720078a90aece7
Summary:        Render a planetary image into an X window
Name:		xplanet
Version:	1.3.1
Release:        26%{?dist}
License:	GPL-2.0-or-later
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		https://gitweb.gentoo.org/repo/gentoo.git/plain/x11-misc/xplanet/files/xplanet-1.3.1-giflib.patch
URL:		http://%{name}.sourceforge.net
Requires:	gnu-free-mono-fonts
# oreon:deps
BuildRequires:  expat-devel
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  glib2-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXt-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  make
BuildRequires:  netpbm-devel
BuildRequires:  pango-devel
# /oreon:deps
%description
Xplanet is similar to Xearth, where an image of the earth is rendered
into an X window.  Azimuthal, Mercator, Mollweide, orthographic, or
rectangular projections can be displayed as well as a window with a
globe the user can rotate interactively.  The other terrestrial
planets may also be displayed. The Xplanet home page has links to
locations with map files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .gif

LANG=C grep -rl "inFile\.getline" . | \
	xargs sed -i.c++11 \
		-e '\@inFile\.getline@s|\(inFile\.getline[ \t]*\)\((.*)\)[ \t]*!= NULL|static_cast<bool> (\1\2)|' \
		-e '\@inFile\.getline@s|\(inFile\.getline[ \t]*\)\((.*)\)[ \t]*== NULL|(!(static_cast<bool> (\1\2)))|'

%build

%configure
make %{?_smp_mflags} -k
%install
CPPROG="cp -p" make DESTDIR=%{buildroot} install
ln -sf ../fonts/gnu-free/FreeMonoBold.ttf \
	%{buildroot}%{_datadir}/%{name}/FreeMonoBold.ttf
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
