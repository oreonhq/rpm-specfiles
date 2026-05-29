%global source0_hash a02f6580e9a53cb16694a99adbb6dbf76f17584f3e97f469a22286299507838c

%global fontname oxygen
%global fontconf 61-%{fontname}

Name:           %{fontname}-fonts
Version:        5.4.3
Release:        28%{?dist}
Summary:        Oxygen fonts created by the KDE Community

# See LICENSE-GPL+FE for details about the exception
# Automatically converted from old format: OFL or GPLv3 with exceptions - review is highly recommended.
License:        LicenseRef-Callaway-OFL OR LicenseRef-Callaway-GPLv3-with-exceptions
URL:            http://www.kde.org
Source0:        https://download.kde.org/stable/plasma/5.4.3/oxygen-fonts-5.4.3.tar.xz
Source1:        %{fontconf}-sans.conf
Source2:        %{fontconf}-mono.conf

# essentially a noarch pkg here, no real -debuginfo needed (#1192729)
%define debug_package   %{nil}

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  fontforge
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

# main (meta)package, largely for upgrade path
Requires: %{fontname}-mono-fonts = %{version}-%{release}
Requires: %{fontname}-sans-fonts = %{version}-%{release}

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{name}-%{version}

%build
%{cmake_kf5} %{?fontforge} -DOXYGEN_FONT_INSTALL_DIR=%{_fontdir}
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

%files
# empty metapackage

%files common
%doc COPYING-GPL+FE.txt COPYING-OFL GPL.txt README.md

%files devel
%{_libdir}/cmake/OxygenFont/

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.4.3-28
- Import
