%global source0_hash 86161a0461386b334a5ffb17cdf094a491941884678272f45749813514ddafcb

Summary: A program for 2D drawing organic molecules
Name: chemtool
Version: 1.6.14
Release: 31%{?dist}
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Source0: http://ruby.chemie.uni-freiburg.de/~martin/chemtool/%{name}-%{version}.tar.gz
Patch0: %{name}-compile.patch
Patch1: %{name}-desktop.patch
Patch2: %{name}-gmd.patch
Patch3: %{name}-gcc10.patch
URL: http://ruby.chemie.uni-freiburg.de/~martin/chemtool/chemtool.html
BuildRequires:  gcc
BuildRequires: desktop-file-utils
BuildRequires: gtk2-devel
BuildRequires: kde3-filesystem
BuildRequires: libXt-devel
BuildRequires: make
Requires: openbabel
Requires: transfig

%description
Chemtool is a program for drawing organic molecules easily and store them
in a variety of output formats including as a X bitmap, Xfig, SVG or EPS
file.  It runs under the X Window System using the GTK widget set.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure \
  --with-kdedir=%{_prefix} \
  --with-gnomedir=%{_prefix}
%make_build

%install
install -d %{buildroot}%{_datadir}/{applications,mimelnk/application,mime-info,mime-types,pixmaps} \
        %{buildroot}%{_datadir}/icons/hicolor/{32x32/mimetypes,48x48/apps}

# fix line endings
pushd examples
tr -d '\r' < 14263232.mol > 14263232.mol.unix && mv -f 14263232.mol.unix 14263232.mol
tr -d '\r' < sample.sdf > sample.sdf.unix && mv -f sample.sdf.unix sample.sdf
popd

%make_install

install -pm644 kde/mimelnk/application/x-chemtool.desktop     %{buildroot}%{_datadir}/mimelnk/application
install -pm644 kde/icons/hicolor/32x32/mimetypes/chemtool.png %{buildroot}%{_datadir}/icons/hicolor/32x32/mimetypes
install -pm644 gnome/mime-types/chemtool.*                    %{buildroot}%{_datadir}/mime-types
install -pm644 gnome/gnome-application-chemtool.png           %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/chemtool.png
desktop-file-install \
                     --dir=%{buildroot}%{_datadir}/applications \
                     --add-category=Education \
                     --add-category=Science \
                     chemtool.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog README TODO examples using_chemtool.html
%{_bindir}/chemtool
%{_bindir}/chemtoolbg
%{_bindir}/cht
%{_datadir}/mimelnk/application/x-chemtool.desktop
%{_datadir}/mime-types/chemtool.keys
%{_datadir}/mime-types/chemtool.mime
%{_datadir}/icons/hicolor/32x32/mimetypes/chemtool.png
%{_datadir}/icons/hicolor/48x48/apps/chemtool.png
%{_datadir}/applications/chemtool.desktop
%{_mandir}/man1/chemtool.1*
%{_mandir}/man1/cht.1*

%changelog
%autochangelog
