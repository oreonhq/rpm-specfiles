%global source0_hash 2f4c17c4ec53dcc9a0e9dc3e79629b690bc70ca343077a5aece719dfcb74bb03
%global maj_version 1.3
%global min_version 2
Name:           immix
Version:        %{maj_version}.%{min_version}
Release:        1%{?dist}
Summary:        An image mixer
License:        GPL-3.0-or-later
URL:            http://immix.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{maj_version}-%{min_version}.tar.gz
Patch:          0001-Make-compatible-with-Exiv2-0.28.0.patch
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  exiv2-devel
BuildRequires:  fftw-devel
BuildRequires:  make
BuildRequires:  qt4-devel
# /oreon:deps
%description
Immix alignes and averages a set of similar images,
 thereby decreasing the numerical noise. It is especially
 useful with digital cameras images shot in a low light
 environment: multiple noisy, high-ISO setting images
 can be combined to get a single less noisy, low-ISO-like
 image, without the blur typically associated with low-ISO
 (motion during exposure) or noise reduction algorithms.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{maj_version}
chmod 0644 *.{cpp,h}
# it seems that "lrelease" does'nt work on rawhide
sed -i -e s/lrelease/lrelease-qt4/ immix.pro
sed -i -e 's@Icon=/usr/share/pixmaps/%{name}.svg@Icon=%{name}@' packaging/%{name}.desktop

%build

%{qmake_qt4}
%make_build
%install
%make_install INSTALL_ROOT=$RPM_BUILD_ROOT
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --delete-original \
  --mode 644 \
  $RPM_BUILD_ROOT%{_datadir}/applications/immix.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
