%global source0_hash 2b2e53e8428ad9b6e8dc8a55b3a5183381911a4dae2c0072fa96296bbb1970d6

Summary: An X Window System graphical chessboard
Name: xboard
Version: 4.9.1
Release: 24%{?dist}
URL: https://www.gnu.org/software/xboard/
Source0: ftp://ftp.gnu.org/pub/gnu/xboard/xboard-%{version}.tar.gz
Source1: xboard.desktop
Requires: chessprogram, xorg-x11-fonts-100dpi
License: GPL-3.0-or-later
BuildRequires: make
BuildRequires:  gcc
BuildRequires: desktop-file-utils >= 0.2.93
BuildRequires: texinfo
BuildRequires: xorg-x11-xbitmaps, libICE-devel, libXmu-devel, libSM-devel
BuildRequires: libXaw-devel, libXt-devel, xorg-x11-proto-devel
BuildRequires: libXpm-devel, libXext-devel
BuildRequires: automake
BuildRequires: gettext
BuildRequires: texinfo-tex
BuildRequires: librsvg2-devel
BuildRequires: gtk2-devel
BuildRequires: pango-devel

%description
Xboard is an X Window System based graphical chessboard which can be
used with the GNU chess and Crafty chess programs, with Internet Chess
Servers (ICSs), with chess via email, or with your own saved games.

Install the xboard package if you need a graphical chessboard.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q 

# Needed for ppc64, automake can't be run here
cp -f %{_datadir}/automake-*/config.* .

%build
export CPPFLAGS="$CPPFLAGS -fcommon"
%configure
make %{?_smp_mflags}

%install
%make_install

desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	%{SOURCE1}

desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	*.desktop

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
install -pm 755 -p cmail $RPM_BUILD_ROOT%{_bindir}

%find_lang %{name}

%files -f %{name}.lang
%license COPYING COPYRIGHT
%doc AUTHORS NEWS README FAQ.html
%doc engine-intf.html
%config(noreplace) %{_sysconfdir}/xboard.conf
%{_bindir}/xboard
%{_bindir}/cmail
%{_mandir}/man6/xboard.6*
%{_infodir}/xboard.info*
%{_datadir}/icons/hicolor/*/apps/xboard.png
%{_datadir}/icons/hicolor/*/apps/xboard.svg
%{_datadir}/games/xboard
%{_datadir}/applications/xboard*.desktop
%{_datadir}/mime/packages/xboard.xml

%changelog
%autochangelog
