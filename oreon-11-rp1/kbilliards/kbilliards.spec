%global source0_hash ec5cbb9bc80178a3541f2dd8dcd1a7c553fae3ed48369425e26c73a77cbe0c7f

Name:           kbilliards
# Note: the "b" in 0.8.7b is supposed to go in the Release tag.
# Keep that in mind when/if you next upgrade the package
# https://fedoraproject.org/wiki/Packaging:NamingGuidelines
Version:        0.8.7b
Release:        49%{?dist}
Summary:        A Fun Billiards Simulator Game
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.hostnotfound.it/kbilliards.php
Source:         http://www.hostnotfound.it/%{name}/%{name}-%{version}.tar.bz2
Patch0:         sqrtl.patch
Patch1:         %{name}-%{version}-compiler_warnings.patch
Patch2:         %{name}-destdir.patch
Patch3:         %{name}-%{version}-gcc43.patch
Patch4:         %{name}-%{version}-fix-configure-checks.patch
BuildRequires:  make gcc gcc-c++
BuildRequires:  kdelibs3-devel bzip2-devel desktop-file-utils gettext
# required to fix the PNGs (vim-common for xxd)
BuildRequires:  pngcrush vim-common
Requires:       hicolor-icon-theme

%description
A billiards simulator game designed for KDE.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i 's/\r//g' ChangeLog

# fix corrupt PNGs
pngcrush -ow -fix media/balls/ball_shadow.png
pngcrush -ow -fix media/balls/ball_shadowb.png
mv media/maps/kbilliards2004.kbm media/maps/kbilliards2004.xml.bz2
bunzip2 media/maps/kbilliards2004.xml.bz2
grep '<data length="342162">' media/maps/kbilliards2004.xml | sed -e 's/^ *<data length="[^"]*">//g' -e 's!</data>$!!g' | xxd -r -p - media/maps/background.png
grep '<data length="142617">' media/maps/kbilliards2004.xml | sed -e 's/^ *<data length="[^"]*">//g' -e 's!</data>$!!g' | xxd -r -p - media/maps/edges.png
grep '<data length="7910">' media/maps/kbilliards2004.xml | sed -e 's/^ *<data length="[^"]*">//g' -e 's!</data>$!!g' | xxd -r -p - media/maps/holes.png
pngcrush -ow -fix media/maps/background.png
pngcrush -ow -fix media/maps/edges.png
pngcrush -ow -fix media/maps/holes.png
echo 's!<data length="342162">[^<]*</data>!<data length="'`wc -c media/maps/background.png | sed 's/ .*$//g'`'">'`xxd -p -c 999999 media/maps/background.png`'</data>!g;s!<data length="142617">[^<]*</data>!<data length="'`wc -c media/maps/edges.png | sed 's/ .*$//g'`'">'`xxd -p -c 999999 media/maps/edges.png`'</data>!g;s!<data length="7910">[^<]*</data>!<data length="'`wc -c media/maps/holes.png | sed 's/ .*$//g'`'">'`xxd -p -c 999999 media/maps/holes.png`'</data>!g' >media/maps/sedscript.txt
rm -f media/maps/background.png media/maps/edges.png media/maps/holes.png
sed -i -f media/maps/sedscript.txt media/maps/kbilliards2004.xml
rm -f media/maps/sedscript.txt
bzip2 -9 media/maps/kbilliards2004.xml
mv media/maps/kbilliards2004.xml.bz2 media/maps/kbilliards2004.kbm

# fix missing semicolon at the end of the Categories list in the .desktop file
sed -i -e 's/^\(Categories=.*\)$/\1\;/g' src/%{name}.desktop

%build
%configure --disable-rpath
# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%make_install

# fixup translation stuff
pushd po
for i in *.po; do
   POLANG=`echo $i|sed 's/\.po//'`
   mkdir -p $RPM_BUILD_ROOT%{_datadir}/locale/$POLANG/LC_MESSAGES
   msgfmt $i -o $RPM_BUILD_ROOT%{_datadir}/locale/$POLANG/LC_MESSAGES/%{name}.mo
done
popd
%find_lang %{name}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications --remove-key=DocPath \
  --add-category Simulation \
  $RPM_BUILD_ROOT%{_datadir}/applnk/Games/%{name}.desktop

rm -fr $RPM_BUILD_ROOT%{_datadir}/icons/locolor

%files -f %{name}.lang
%doc AUTHORS ChangeLog TODO src/NOATUN_AUTHORS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/apps/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
%autochangelog
