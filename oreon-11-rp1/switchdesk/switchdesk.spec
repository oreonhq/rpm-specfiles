%global source0_hash 3b95d65848a87e3d541f1195ae045a18f746ee1407c86120a9c11022f9b1bcae

Name: switchdesk
Summary: A desktop environment switcher
Version: 5.0.2
Release: 7%{?dist}
Url: https://github.com/ngothan/switchdesk
Source: https://github.com/ngothan/switchdesk/archive/%{version}/%{name}-%{version}.tar.gz
License: GPL-2.0-or-later
BuildArch: noarch
BuildRequires: make
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: desktop-file-utils

%description
The Desktop Switcher is a tool which enables users to easily switch
between various desktop environments that they have installed.

Support for different environments on different computers is available, as
well as support for setting a global default environment.

Install switchdesk if you need a tool for switching between desktop
environments.

%package gui
Summary: A graphical interface for the Desktop Switcher
Requires: %{name} = %{version}-%{release}
Requires: python3
Requires: python3-gobject-base
Requires: desktop-file-utils

%description gui
The switchdesk-gui package provides the graphical user interface for
the Desktop Switcher.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
install -p -m 644 %{name}.desktop %{buildroot}%{_datadir}/applications/

%find_lang %{name}

%files
%doc AUTHORS COPYING
%dir %{_datadir}/%{name}
%{_bindir}/%{name}*
%{_datadir}/%{name}/Xclients*
%{_mandir}/man1/%{name}*
%lang(fr)%{_mandir}/fr/man1/%{name}*

%files gui -f %{name}.lang
%{_datadir}/%{name}/*.glade
%{_datadir}/%{name}/*.py*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*.png

%changelog
%autochangelog
