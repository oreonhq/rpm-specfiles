%global source1_hash 57405f3327356c279411ac3849aacced2df9da451554df6754ba51d84019092e
%global source0_hash d6f236fcafe16611b88c468502665dd5e9c73aa18eae0666e8ca9062ef5a471e
Name:           qps
Version:        2.13.0
Release:        1%{?dist}
Summary:        Qt process viewer and manager
License:        GPL-2.0-or-later
URL:            https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  perl
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(lxqt)
# /oreon:deps
%description
Qps is a visual process manager, an X11 version of "top" or "ps" that
displays processes in a window and lets you sort and manipulate them.

Qps can:
  o  Change nice value of a process.
  o  Alter the scheduling policy and soft realtime priority of a process.
  o  Display the TCP/UDP sockets used by a process, and names of the
     connected hosts (Linux only).
  o  Display the memory mappings of the process (which files and shared
     libraries are loaded   where).
  o  Display the open files of a process, and the state of unix domain sockets.
  o  Kill or send any other signal to selected processes.
  o  Display the load average as a graph, and use this as its icon when
     iconified.
  o  Show (as graph or numbers) current CPU, memory and swap usage.
  o  Sort the process table on any attribute (size, cpu usage, owner etc).
  o  On SMP systems running Linux 2.6 or later (or Solaris), display cpu usage
     for each processor, and which CPU a process is running on.
  o  Display the environment variables of any process.
  o  Show the process table in tree form, showing the parent-child
     relationship.
  o  Execute user-defined commands on selected processes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%find_lang %{name} --with-qt
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.lxqt.Qps.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
