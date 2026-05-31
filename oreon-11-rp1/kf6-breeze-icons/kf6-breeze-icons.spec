%global source0_hash 63d67d834b28f95f45d53ee4594b1b39de4802429570f0e3b5e63ab509abde8b

# If KF7 still provides these icons, then their installation should then
# be disabled in KF6 builds.
%bcond install_icons 1
# for compatibility, to be removed once Kexi (and others?) are ported
%bcond install_rcc 1

%global framework breeze-icons

%global stable_kf6 stable
%global majmin_ver_kf6 6.24


Name:    kf6-%{framework}
Summary: Breeze icon theme library
Version: 6.24.0
Release:	4%{?dist}

# skladnik.svg is CC-BY-SA-4.0
# folder-edit-sign-encrypt.svg is LGPL-2.1-or-later
# src/lib/ is LGPL-2.0-or-later
# all other icons are LGPL-3.0-or-later
License: LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later AND CC-BY-SA-4.0
URL:     https://develop.kde.org/frameworks/breeze-icons/
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

## upstream patches


## upstreamable patches


BuildRequires: extra-cmake-modules >= %{version}
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
# icon optimizations
BuildRequires: hardlink
# for generate-24px-versions.py
BuildRequires: python3-lxml

%if %{with install_icons}
Requires: breeze-icon-theme = %{version}-%{release}
%else
Requires: breeze-icon-theme
%endif

%description
%{summary}.

%if %{with install_icons}
%package -n breeze-icon-theme
Summary:     Breeze icon theme
# analysis above
License:     LGPL-2.1-or-later AND LGPL-3.0-or-later AND CC-BY-SA-4.0
BuildArch:   noarch
Requires:    hicolor-icon-theme
# Needed for proper Fedora logo
Requires:    system-logos
# upstream name
Provides:    breeze-icons = %{version}-%{release}
# package changed arch
Obsoletes:   breeze-icon-theme < 6.3.0-2
# anaconda icon split out into fedora-only subpackage
Obsoletes:   breeze-icon-theme < 6.13.0-2
Conflicts:   breeze-icon-theme < 6.13.0-2
%description -n breeze-icon-theme
%{summary}.

%if 0%{?fedora}
%package -n breeze-icon-theme-fedora
Summary:     Breeze icon theme Fedora specific icons
License:     LGPL-3.0-or-later
BuildArch:   noarch
Requires:    breeze-icon-theme = %{version}-%{release}
# This is for Fedora only
Requires:    fedora-release-common
Supplements: (breeze-icon-theme and fedora-release-kde)
Obsoletes:   breeze-icon-theme < 6.13.0-2
Conflicts:   breeze-icon-theme < 6.13.0-2
%description -n breeze-icon-theme-fedora
%{summary}.
%endif

%endif

%if %{with install_rcc}
%package -n breeze-icon-theme-rcc
Summary:     Breeze Qt resource files
# analysis above
License:     LGPL-2.1-or-later AND LGPL-3.0-or-later AND CC-BY-SA-4.0
BuildArch:   noarch
# package changed arch
Obsoletes:   breeze-icon-theme-rcc < 6.3.0-2
%description -n breeze-icon-theme-rcc
%{summary}.
%endif

%package     devel
Summary:     Breeze icon theme development files
Requires:    %{name} = %{version}-%{release}
# renamed for https://pagure.io/fedora-kde/SIG/issue/530
Provides:    breeze-icon-theme-devel = %{version}-%{release}
Obsoletes:   breeze-icon-theme-devel < 6.3.0-2
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

# Move Fedora installer icon out of normal breeze installs
mkdir -p icons-fedora/apps/48
mv icons/apps/48/org.fedoraproject.AnacondaInstaller.svg icons-fedora/apps/48


%build
%cmake_kf6 \
  -DBINARY_ICONS_RESOURCE:BOOL=%{?with_install_rcc:ON}%{!?with_install_rcc:OFF} \
  -DSKIP_INSTALL_ICONS:BOOL=%{?with_install_icons:OFF}%{!?with_install_icons:ON} \
  %{nil}

%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose


%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%if %{with install_icons}

## icon optimizations
du -s .
hardlink -c -v %{buildroot}%{_datadir}/icons/
du -s .

# %%ghost icon.cache
touch %{buildroot}%{_kf6_datadir}/icons/{breeze,breeze-dark}/icon-theme.cache

%if 0%{?fedora}
install -pm 0644 icons-fedora/apps/48/org.fedoraproject.AnacondaInstaller.svg %{buildroot}%{_kf6_datadir}/icons/breeze/apps/48
ln -sr %{buildroot}%{_kf6_datadir}/icons/breeze/apps/48/org.fedoraproject.AnacondaInstaller.svg %{buildroot}%{_kf6_datadir}/icons/breeze-dark/apps/48/org.fedoraproject.AnacondaInstaller.svg
%endif

## trigger-based scriptlets
%transfiletriggerin -n breeze-icon-theme -- %{_datadir}/icons/breeze
gtk-update-icon-cache --force %{_datadir}/icons/breeze &>/dev/null || :

%transfiletriggerin -n breeze-icon-theme -- %{_datadir}/icons/breeze-dark
gtk-update-icon-cache --force %{_datadir}/icons/breeze-dark &>/dev/null || :

%transfiletriggerpostun -n breeze-icon-theme -- %{_datadir}/icons/breeze
gtk-update-icon-cache --force %{_datadir}/icons/breeze &>/dev/null || :

%transfiletriggerpostun -n breeze-icon-theme -- %{_datadir}/icons/breeze-dark
gtk-update-icon-cache --force %{_datadir}/icons/breeze-dark &>/dev/null || :

%endif

%files
%license COPYING.LIB
%doc README.md
%{_kf6_libdir}/libKF6BreezeIcons.so.6
%{_kf6_libdir}/libKF6BreezeIcons.so.%{version}

%files devel
%{_kf6_includedir}/BreezeIcons/
%{_kf6_libdir}/cmake/KF6BreezeIcons/
%{_kf6_libdir}/libKF6BreezeIcons.so

%if %{with install_icons}
%files -n breeze-icon-theme
%license COPYING-ICONS
%doc README.md
%ghost %{_datadir}/icons/breeze/icon-theme.cache
%{_datadir}/icons/breeze/index.theme
%{_datadir}/icons/breeze/*/
%ghost %{_datadir}/icons/breeze-dark/icon-theme.cache
%{_datadir}/icons/breeze-dark/index.theme
%{_datadir}/icons/breeze-dark/*/
%exclude %{_datadir}/icons/breeze/breeze-icons.rcc
%if 0%{?fedora}
%exclude %{_datadir}/icons/breeze*/apps/*/org.fedoraproject.AnacondaInstaller.svg
%endif

%if 0%{?fedora}
%files -n breeze-icon-theme-fedora
%{_datadir}/icons/breeze*/apps/*/org.fedoraproject.AnacondaInstaller.svg
%endif

%endif

%if %{with install_rcc}
%files -n breeze-icon-theme-rcc
%{_datadir}/icons/breeze/breeze-icons.rcc
%endif

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Use kf6 cmake build/install macros (avoid qt6 prepare_docs / install_html_docs)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)
