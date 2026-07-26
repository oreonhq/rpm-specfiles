%global source0_hash 47629578e89d96d1541c91d040aec4316f03ad6d01dc3eecb8f82a33445c1e4e

Name:           wmdocker
Version:        1.5
Release:        38%{?dist}
Summary:        KDE and GNOME2 system tray replacement docking application

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://icculus.org/openbox/2/docker/
Source0:        http://icculus.org/openbox/2/docker/docker-1.5.tar.gz

Patch0:         1.5-fix-parce_cmd_line.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  libX11-devel

%description
Docker is a docking application (WindowMaker dock app) which acts as a system
tray for KDE and GNOME2. It can be used to replace the panel in either
environment, allowing you to have a system tray without running the KDE/GNOME
panel or environment.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n docker-%{version}

%build
%make_build CFLAGS="%{optflags}" XLIBPATH=%{_libdir}/X11

%install
%__mkdir_p %{buildroot}%{_bindir}
%make_install PREFIX=%{buildroot}/%{_prefix}
# due to package rename to prevent conflicts with docker
mv %{buildroot}/%{_bindir}/docker %{buildroot}/%{_bindir}/wmdocker

%files
%doc README
%license COPYING
%{_bindir}/wmdocker

%changelog
%autochangelog
