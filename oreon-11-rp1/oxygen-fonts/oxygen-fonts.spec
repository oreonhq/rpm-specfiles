%global source0_hash a02f6580e9a53cb16694a99adbb6dbf76f17584f3e97f469a22286299507838c
%global fontname oxygen
%global fontconf 61-%{fontname}
Name:           %{fontname}-fonts
Version:        5.4.3
Release:        1%{?dist}
Summary:        Oxygen fonts created by the KDE Community
License:        LicenseRef-Callaway-OFL OR LicenseRef-Callaway-GPLv3-with-exceptions
URL:            http://www.kde.org
Source0:        https://download.kde.org/stable/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        %{fontconf}-sans.conf
Source2:        %{fontconf}-mono.conf
%define debug_package   %{nil}
Requires:       fontpackages-filesystem
Requires: %{fontname}-mono-fonts = %{version}-%{release}
Requires: %{fontname}-sans-fonts = %{version}-%{release}
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  fontforge
BuildRequires:  fontpackages-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
Oxygen fonts created by the KDE Community.

%package common
Summary:        Common files for Oxygen font
Requires:       fontpackages-filesystem
BuildArch:      noarch
%description    common
%{summary}.

%package -n %{fontname}-mono-fonts
Summary:        Oxygen Monospaced Font
Requires:       %{name}-common = %{version}-%{release}
BuildArch:      noarch
%description    -n %{fontname}-mono-fonts
%{summary}.

%package -n %{fontname}-sans-fonts
Summary:        Oxygen Sans-Serif Font
Requires:       %{name}-common = %{version}-%{release}
BuildArch:      noarch
%description    -n %{fontname}-sans-fonts
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{version}

%build

%{cmake_kf5} %{?fontforge} -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DOXYGEN_FONT_INSTALL_DIR=%{_fontdir}
%cmake_build
%install
%cmake_install
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-mono.conf
ln -s %{_fontconfig_templatedir}/%{fontconf}-sans.conf \
      %{buildroot}/%{_fontconfig_confdir}/%{fontconf}-sans.conf
ln -s %{_fontconfig_templatedir}/%{fontconf}-mono.conf \
      %{buildroot}/%{_fontconfig_confdir}/%{fontconf}-mono.conf
%_font_pkg -n sans -f %{fontconf}-sans.conf Oxygen-Sans*.ttf
%_font_pkg -n mono -f %{fontconf}-mono.conf OxygenMono*.ttf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n oxygen-fonts-common -f %{oreon_filedir}/oxygen-fonts-common.list
%files -n oxygen-mono-fonts -f %{oreon_filedir}/oxygen-mono-fonts.list
%files -n oxygen-sans-fonts -f %{oreon_filedir}/oxygen-sans-fonts.list
%files -n oxygen-fonts-devel -f %{oreon_filedir}/oxygen-fonts-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.4.3-28
- Import
