%global source0_hash a315f7001a020c6b8f644db1c1dc56ccfbb9e3efcbf12c41ac9eb4e5e75cb5f7

Name:		xscorch
Version:	0.2.1
Release:	31%{?dist}
Summary:	A Scorched Earth clone
License:	GPL-2.0-only
URL:		http://www.xscorch.org/
Source0:	http://www.xscorch.org/releases/%{name}-%{version}.tar.gz
Source1:	xscorch.desktop
Source2:        xscorch.png
Source3:        xscorch.appdata.xml
Patch1:		xscorch-0.2.1-pre2-disable-debug.patch
Patch2:		xscorch-0.2.1-missing-proto.patch
Patch3:		xscorch-0.2.1-memcpy.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:	libX11-devel gtk2-devel desktop-file-utils libappstream-glib
BuildRequires:	perl-interpreter
Requires:       hicolor-icon-theme
Requires:       gdk-pixbuf2-modules-extra

%description
xscorch is a clone of the classic DOS game, "Scorched Earth". The basic goal
is to annihilate enemy tanks using overpowered guns :). Basically, you buy
weapons, you target the enemy by adjusting the angle of your turret and firing
power, and you hope to destroy their tank before they destroy yours.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
# Fix encoding
for i in AUTHORS ChangeLog; do
	iconv -f ISO-8859-1 -t UTF-8 < ${i} > ${i}.tmp
	mv -f ${i}.tmp ${i}
done

%build
export CPPFLAGS="$CPPFLAGS -fcommon -std=gnu17"
%configure --disable-network --disable-sound
make %{?_smp_mflags}

%install
%make_install INSTALL="install -p"

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/xscorch.appdata.xml

%files
%doc doc/AI AUTHORS ChangeLog doc/NETWORK doc/NOTES README
%license COPYING
%{_bindir}/xscorch
%{_datadir}/appdata/xscorch.appdata.xml
%{_datadir}/applications/xscorch.desktop
%{_mandir}/man6/xscorch.6*
%{_datadir}/xscorch/
%{_datadir}/icons/hicolor/64x64/apps/xscorch.png

%changelog
%autochangelog
