%global source0_hash ebf56ee84807c438723e9624836db73498c18a4ac93d78fc1dc0531418517a17

%global appname switchmail
%global __python /usr/bin/python3

Summary: The Mail Transport Agent Switcher
Name: system-switch-mail
Version: 2.0.1
Release: 27%{?dist}
Url: http://than.fedorapeople.org/system-switch-mail
Source0: http://than.fedorapeople.org/system-switch-mail/%{name}-%{version}.tar.xz
Patch0: system-switch-mail-2.0.1-python3.patch
License: GPL-2.0-or-later
BuildArch: noarch

Requires: newt-python3
Requires: polkit

BuildRequires: make
BuildRequires:  python3-devel
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: desktop-file-utils

%description
The system-switch-mail is the Mail Transport Agent Switcher.
It enables users to easily switch between various Mail Transport Agent
that they have installed.

%package gui
Summary: A GUI interface for Mail Transport Agent Switcher
Requires: %{name} = %{version}-%{release}
Requires: usermode-gtk
Requires: python3-gobject-base
Requires: desktop-file-utils
Obsoletes: %{name}-gnome < 2.0

%description gui
The system-switch-mail-gnome package contains a GNOME interface for the
Mail Transport Agent Switcher.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
make %{?_smp_mflags}

%install
make PYTHON=%{__python3} DESTDIR=%{buildroot} mandir=%{_mandir} sysconfdir=%{_sysconfdir} install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appname}.desktop
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/%{name}/

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING AUTHORS
%{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/backend.py*
%{_datadir}/%{name}/%{appname}-tui.py*
%{_mandir}/man1/*

%files gui
%{_datadir}/polkit-1/actions/org.fedoraproject.switchmail.policy
%{_datadir}/applications/*
%{_datadir}/%{name}/%{appname}-gui.py*
%{_datadir}/%{name}/%{appname}.glade
%{_datadir}/%{name}/__pycache__
%{_datadir}/pixmaps/*.png

%changelog
%autochangelog
