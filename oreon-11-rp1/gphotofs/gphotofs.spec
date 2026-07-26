%global source0_hash 676ec4de69a81c193ffc31bdc7b587ac2a2cc3780b14f0e7c9c4c0a517b343cc

Summary: A FUSE filesystem module to mount your camera as a filesystem
Name: gphotofs
Version: 0.5
Release: 26%{?dist}
License: GPL-1.0-or-later
URL: http://www.gphoto.org/proj/gphotofs/
BuildRequires:  gcc
BuildRequires: glib2-devel, fuse-devel, libgphoto2-devel
BuildRequires: make
Source0: http://downloads.sourceforge.net/gphoto/%{name}-%{version}.tar.bz2

%description
A filesystem client based on libgphoto2 that exposes supported cameras
as filesystems; while some cameras implement the USB Mass Storage class
and already appear as filesystems (making this program redundant), many
use the Picture Transfer Protocol (PTP) or some other custom protocol.
But as long as the camera is supported by libgphoto2, it can be mounted
as a filesystem using this program.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%doc AUTHORS COPYING README NEWS ChangeLog

%{_bindir}/gphotofs

%changelog
%autochangelog
