%global source0_hash e5f5ec03a0611397f8aafd07f05d4763726d9911139d9e267c5f308af9a6955b
Summary:        An X Window System utility for monitoring system resources
Name:          xosview
Version:       1.25
Release:        2%{?dist}
License:       GPL-1.0-or-later
URL:           http://www.pogo.org.uk/~mark/xosview/
Source0:        http://www.pogo.org.uk/~mark/xosview/releases/xosview-%{version}.tar.gz
Patch:         xosview-1.24-app-def.patch
Requires:      xorg-x11-fonts-misc
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  libXpm-devel
BuildRequires:  make
# /oreon:deps
%description
The xosview utility displays a set of bar graphs which show the
current system state, including memory usage, CPU usage, system load,
etc. Xosview runs under the X Window System.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build OPTFLAGS="%{optflags}"
%install
%make_install PREFIX=%{_prefix}
install -p -m 0644 -D Xdefaults %{buildroot}%{_datadir}/X11/app-defaults/XOsview
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/xosview.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
