%global source0_hash b916aa949e51ecb48600e381fbf251542cefb4e35a057a721cac39bcdb01a6ae
%bcond check 1
Name:           NsCDE
Version:        2.3
Release:        1%{?dist}
Summary:        Modern and functional CDE desktop based on FVWM
License:        GPL-3.0-only
URL:            https://github.com/NsCDE/NsCDE
Source0:        https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch:          %{name}-Xorg-fvwm2-fix.diff
%if %{with check}
%endif
Requires:       %{name}-data = %{version}-%{release}
Requires:       %{name}-doc = %{version}-%{release}
Requires:       cpp
Requires:       dex-autostart
Requires:       fvwm
Requires:       gettext
Requires:       ImageMagick
Requires:       ksh
Requires:       python3-psutil
Requires:       python3-pyxdg
Requires:       python3-qt5
Requires:       python3-yaml
Requires:       qt5-qtstyleplugins
Requires:       redhat-menus
Requires:       xdotool
Requires:       xdpyinfo
Requires:       xprop
Requires:       xrandr
Requires:       xrdb
Requires:       xrefresh
Requires:       xset
Requires:       xterm
Recommends:     dunst
Recommends:     stalonetray
Recommends:     xscreensaver
Recommends:     xsettingsd
Suggests:       gkrellm
Suggests:       rofi
Suggests:       xclip
Provides:       bundled(colorpicker) = 0
Provides:       bundled(pclock) = 0.13.1
Provides:       bundled(XOverrideFontCursor) = 20190901
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  cpp
BuildRequires:  desktop-file-utils
BuildRequires:  dunst
BuildRequires:  fvwm
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  ksh
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXpm-devel
BuildRequires:  libxcb-devel
BuildRequires:  make
BuildRequires:  python3-psutil
BuildRequires:  python3-qt5
BuildRequires:  python3-yaml
BuildRequires:  redhat-menus
BuildRequires:  rofi
BuildRequires:  sed
BuildRequires:  stalonetray
BuildRequires:  xclip
BuildRequires:  xdotool
BuildRequires:  xdpyinfo
BuildRequires:  xprop
BuildRequires:  xrandr
BuildRequires:  xrdb
BuildRequires:  xrefresh
BuildRequires:  xscreensaver
BuildRequires:  xset
BuildRequires:  xsettingsd
# /oreon:deps
%description

%package        data
Summary:        Data files for %{name}
BuildArch:      noarch
Requires:       %{name}-icon-theme = %{version}-%{release}
%description    data

This package contains data files for %{name}.

%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch
%description    doc

This package contains documentation for %{name}.

%package        icon-theme
Summary:        %{name} icon theme
BuildArch:      noarch
Requires:       hicolor-icon-theme
%description    icon-theme

This package contains the %{name} icon theme.

%prep
%oreon_prep
%build

%set_build_flags
%configure --docdir=%{_docdir}/%{name}
%make_build
%install
%make_install
%find_lang NsCDE --all-name
mkdir -p %{buildroot}%{_docdir}/%{name}-doc
rm %{buildroot}%{_docdir}/%{name}/LICENSE
for d in examples html NsCDE.{pdf,txt}; do
  mv %{buildroot}%{_docdir}/%{name}/${d} %{buildroot}%{_docdir}/%{name}-doc/
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

for f in %{buildroot}%{_datadir}/applications/*.desktop; do
  desktop-file-validate ${f}
done
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
