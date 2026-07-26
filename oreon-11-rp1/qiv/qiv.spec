%global source0_hash ef085ffde2d48b05b3665939e5ae1e359d3a381008fb827684f7d6fd4c533704

Name:           qiv
Version:        2.3.3
Release:        %autorelease

Summary:        Quick Image Viewer

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://spiegl.de/qiv/
Source0:        http://spiegl.de/qiv/download/%{name}-%{version}.tgz

Patch0:         2.3.3-makefile-destdir.patch
Patch1:         2.3.3-fix-prototypes.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  imlib2-devel
BuildRequires:  file-devel
BuildRequires:  lcms2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libexif-devel
BuildRequires:  libtiff-devel

%description
qiv is a very small and pretty fast gdk2/Imlib2 image viewer.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%make_build CFLAGS="%{optflags}"

%install
%make_install PREFIX="%{_prefix}"
chmod 644 contrib/qiv-command.example

%files
%doc README Changelog README.TODO contrib/qiv-command.example
%license README.COPYING
%{_bindir}/qiv
%{_mandir}/man1/qiv.1*
%{_datadir}/applications/qiv.desktop
%{_datadir}/pixmaps/qiv.png

%changelog
%autochangelog
