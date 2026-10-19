%global source0_hash 2b7455e63344b98e4db4ca50ff6982f5f81c309e563014d7401cccf2b3acc6bf
Name:           qiv
Version:        3.0.1
Release:        1%{?dist}
Summary:        Quick Image Viewer
License:        GPL-2.0-only
URL:            http://spiegl.de/qiv/
Source0:        http://spiegl.de/qiv/download/%{name}-%{version}.tgz
Patch0:         3.0.1-makefile-destdir.patch
Patch1:         3.0.1-fix-prototypes.patch
# oreon:deps
BuildRequires:  file-devel
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  imlib2-devel
BuildRequires:  lcms2-devel
BuildRequires:  libexif-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  make
# /oreon:deps
%description
qiv is a very small and pretty fast gdk2/Imlib2 image viewer.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build CFLAGS="%{optflags}"
%install
%make_install PREFIX="%{_prefix}"
chmod 644 contrib/qiv-command.example
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
