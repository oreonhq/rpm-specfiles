%global source0_hash 0f62b88ca6745aeb0d72197a767785cee963a321ea92275620d679b03d040196
Name:           printrun
Epoch:          1
Version:        2.2.0
%global prerel  rc8
%global uver    %{version}%{?prerel}
%global tag     %{name}-%{uver}
Release:        1%{?dist}
Summary:        RepRap printer interface and tools
License:        GPL-3.0-or-later AND FSFAP
URL:            https://github.com/kliment/Printrun
Source0:        https://github.com/kliment/Printrun/archive/%{name}-%{version}%{prerel}.tar.gz
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11 || 0%{?oreon} >= 11
ExcludeArch:    %{ix86}
%endif
Patch1:         %{url}/pull/1224.patch
Patch2:         %{url}/pull/1262.patch
Patch3:         %{url}/pull/1303.patch
Patch4:         %{url}/pull/1428.patch
Requires:       pronterface = %{epoch}:%{version}-%{release}
Requires:       pronsole = %{epoch}:%{version}-%{release}
Requires:       plater = %{epoch}:%{version}-%{release}
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  /usr/bin/grep
BuildRequires:  /usr/bin/msgfmt
BuildRequires:  /usr/bin/sed
BuildRequires:  gcc
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-pyserial
BuildRequires:  python3-setuptools
# /oreon:deps
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
%oreon_autofiles pronsole usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles pronterface usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles plater usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n printrun-common -f %{oreon_filedir}/printrun-common.list
%files -n pronsole -f %{oreon_filedir}/pronsole.list
%files -n pronterface -f %{oreon_filedir}/pronterface.list
%files -n plater -f %{oreon_filedir}/plater.list

%changelog

%autochangelog
