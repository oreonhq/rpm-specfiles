%global source0_hash 0726c5cde08e41c88d9e1002f2743dc7f7d39d553d49605a7cf4b8bb9d47349a

Summary:       Immersive viewer for spherical panoramas
Name:          panoglview
Version:       0.2.2
Release:       46%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://hugin.sourceforge.net/
Source0:       http://downloads.sourceforge.net/hugin/%{name}-%{version}.tar.gz
Source1:       %{name}.desktop
Source2:       %{name}.png
Patch0:        wxwidgets3.0.patch
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires: libtiff-devel libjpeg-devel libpng-devel
BuildRequires: wxGTK-devel zlib-devel desktop-file-utils

%description
Use panoglview to explore equirectangular panoramic images.  Equirectangular
panoramas are typically JPEG/TIFF/PNG images with a 2:1 aspect ratio.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
chmod -x src/*.h src/*.cpp

%build
%configure
make %{?_smp_mflags} LDFLAGS="-lGL -lGLU"

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
desktop-file-install --vendor="" \
  --dir=%{buildroot}/%{_datadir}/applications %{SOURCE1}
install -D -m 0755 %{SOURCE2} %{buildroot}/%{_datadir}/pixmaps/%{name}.png

%files
%doc AUTHORS ChangeLog COPYING INSTALL NEWS
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
%autochangelog
