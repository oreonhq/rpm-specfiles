%global source0_hash 6e11776e640798a1ac4168d53877f105bb3e8cf93b443c160841e3acdab63939
%global xfceversion 4.21
Name:           xfce4-settings
Version:        4.21.0
Release:        1%{?dist}
Summary:        Settings Manager for Xfce
License:        GPL-2.0-or-later
URL:            http://www.xfce.org/
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2
Patch10:        xfce4-settings-%{xfceversion}-fedora.patch
%ifnarch s390 s390x
%endif
Requires:       xfconf
# oreon:deps
BuildRequires:  colord-devel
BuildRequires:  desktop-file-utils
BuildRequires:  exo-devel
BuildRequires:  garcon-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libXrandr-devel
BuildRequires:  libcanberra-devel
BuildRequires:  libnotify-devel
BuildRequires:  libxfce4ui-devel
BuildRequires:  libxfce4util-devel
BuildRequires:  libxklavier-devel
BuildRequires:  make
BuildRequires:  xfconf-devel
BuildRequires:  xorg-x11-drv-libinput-devel
# /oreon:deps
%description
This package includes the settings manager applications for the Xfce desktop. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch 10

%build

%configure --enable-sound-settings --enable-pluggable-dialogs --enable-maintainer-mode --enable-xorg-libinput
%make_build
%install
%make_install
for file in %{buildroot}%{_datadir}/applications/*.desktop ; do
    desktop-file-install \
        --add-category="X-XFCE" \
        --remove-category="XFCE" \
        --delete-original \
        --dir=%{buildroot}%{_datadir}/applications \
        $file
done
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
