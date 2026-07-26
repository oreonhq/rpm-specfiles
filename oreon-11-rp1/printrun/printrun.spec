%global source0_hash 0f62b88ca6745aeb0d72197a767785cee963a321ea92275620d679b03d040196

Name:           printrun
Epoch:          1
Version:        2.0.0
%global prerel  rc8
%global uver    %{version}%{?prerel}
%global tag     %{name}-%{uver}
Release:        0.41.%{prerel}%{?dist}

Summary:        RepRap printer interface and tools
# Only AppData is FSFAP
# Automatically converted from old format: GPLv3+ and FSFAP - review is highly recommended.
License:        GPL-3.0-or-later AND FSFAP

URL:            https://github.com/kliment/Printrun
Source0:        https://github.com/kliment/Printrun/archive/%{tag}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11
ExcludeArch:    %{ix86}
%endif

# Fix a crashes on Python 3.10
Patch1:         %{url}/pull/1224.patch
Patch2:         %{url}/pull/1262.patch
Patch3:         %{url}/pull/1303.patch
# Fix a crash on Python 3.13
Patch4:         %{url}/pull/1428.patch

BuildRequires:  gcc
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pyserial
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  /usr/bin/grep
BuildRequires:  /usr/bin/msgfmt
BuildRequires:  /usr/bin/sed

Requires:       pronterface = %{epoch}:%{version}-%{release}
Requires:       pronsole = %{epoch}:%{version}-%{release}
Requires:       plater = %{epoch}:%{version}-%{release}

%description
Printrun is a set of G-code sending applications for RepRap.
It consists of printcore (dumb G-code sender), pronsole (featured command line
G-code sender), pronterface (featured G-code sender with graphical user
interface), and a small collection of helpful scripts.
This package installs whole Printrun.

###############################################

%package        common
Summary:        Common files for Printrun
Requires:       python3-appdirs
Requires:       python3-lxml
Requires:       python3-numpy

Provides:       bundled(tatlin)

%description    common
Printrun is a set of G-code sending applications for RepRap.
This package contains common files.

###############################################

%package     -n pronsole
Summary:        CLI interface for RepRap
Requires:       python3-pyserial
Requires:       %{name}-common = %{epoch}:%{version}-%{release}
# So that it just works
Requires:       3dprinter-udev-rules

BuildArch:      noarch

%description -n pronsole
Pronsole is a featured command line G-code sender.
It controls the ReRap printer. It is a part of Printrun.

################################################

%package     -n pronterface
Summary:        GUI interface for RepRap
Requires:       python3-cairocffi
Requires:       python3-cffi
Requires:       python3-dbus
Requires:       python3-gobject
Requires:       python3-psutil
Requires:       python3-pyglet
Requires:       python3-wxpython4
Requires:       simarrange
Requires:       pronsole = %{epoch}:%{version}-%{release}
# So that it just works
Requires:       3dprinter-udev-rules

BuildArch:      noarch

%description -n pronterface
Pronterface is a featured G-code sender with graphical user interface.
It controls the ReRap printer. It is a part of Printrun.

###############################################

%package     -n plater
Summary:        RepRap STL plater
Requires:       %{name}-common = %{epoch}:%{version}-%{release}
Requires:       python3-cairocffi
Requires:       python3-cffi
Requires:       python3-gobject
Requires:       python3-psutil
Requires:       python3-pyglet
Requires:       python3-wxpython4
Requires:       simarrange
BuildArch:      noarch

%description -n plater
Plater is a GUI tool to prepare printing plate from STL files for ReRap.
It is a part of Printrun.

###############################################

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Printrun-%{tag}

# don't pin wxpython
sed -i 's/wxPython (== 4.1.0)/wxPython (>= 4)/' requirements.txt

# sed upstream's desktop files to remove .py extensions from Exec
sed -i 's/.py//' *.desktop

# remove useless shebangs
grep -ilrx printrun -e '#!/usr/bin/env python3' --include '*.py'| xargs sed -i '1s|^#!/usr/bin/env python3$||'

%build
# rebuild locales
cd locale
for FILE in *
  do msgfmt $FILE/LC_MESSAGES/plater.po -o $FILE/LC_MESSAGES/plater.mo || :
     msgfmt $FILE/LC_MESSAGES/pronterface.po -o $FILE/LC_MESSAGES/pronterface.mo || :
done
cd ..

%py3_build

%install
%py3_install

cd %{buildroot}%{_bindir}
for FILE in *.py; do
  mv -f $FILE ${FILE%.py}
done

cd -

%{find_lang} pronterface
%{find_lang} plater

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%files
%doc README*
%license COPYING

%files common
%{python3_sitearch}/%{name}/
%{python3_sitearch}/Printrun-*.egg-info/
%{_bindir}/printcore*
%doc README*
%license COPYING

%files -n pronsole
%{_bindir}/pronsole*
%{_datadir}/pixmaps/pronsole.png
%{_datadir}/applications/pronsole.desktop
%{_datadir}/metainfo/pronsole.appdata.xml
%doc README*
%license COPYING

%files -n pronterface -f pronterface.lang
%{_bindir}/pronterface*
%{_datadir}/pronterface/
%{_datadir}/pixmaps/pronterface.png
%{_datadir}/applications/pronterface.desktop
%{_datadir}/metainfo/pronterface.appdata.xml
# This file is needed by both pronterface and plater, so it is in both
# https://bugzilla.redhat.com/show_bug.cgi?id=1777737
%{_datadir}/pixmaps/plater.png
%doc README*
%license COPYING

%files -n plater -f plater.lang
%{_bindir}/plater*
%{_datadir}/applications/plater.desktop
%{_datadir}/pixmaps/plater.png
%{_datadir}/metainfo/plater.appdata.xml
%doc README*
%license COPYING

%changelog
%autochangelog
