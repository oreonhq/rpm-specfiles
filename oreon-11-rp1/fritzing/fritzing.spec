%global source1_hash 90b710b8f73fae5dedce1af01382d67805a21bb9761863a9f73dd9c8f10cbd6c
%global source0_hash 1aa2c068722a0ed2df724118933114e1c101defd0aedd5c18d35a177de1a27c1
Name:           fritzing
%global rtld_name org.fritzing.Fritzing
Summary:        Electronic Design Automation software; from prototype to product
License:        GPL-3.0-or-later
URL:            https://fritzing.org/
%global version_no 1.0.6
Release:        1%{?dist}
%global app_date 20251007
%global app_commit 04e5bb0241e8f1de24d0fce9be070041c6d5b68e
%global parts_date 20251007
%global parts_commit 73bc0559bb8399b2f895d68f032e41d7efc720c0
%global app_version %{version_no}^%{app_date}
%global parts_version %{version_no}^%{parts_date}
Version:        %{app_version}
Source0:        https://github.com/%{name}/%{name}-app/archive/%{app_commit}/%{name}-app-%{app_commit}.tar.gz
Source1:        https://github.com/%{name}/%{name}-parts/archive/%{parts_commit}/%{name}-parts-%{parts_commit}.tar.gz
Patch0:         0000-disable-autoupdate.patch
Patch2:         0002-remove-twitter4j.patch
Patch3:         0003-maximum-qt-version.patch
Patch4:         0004-Work-around-build-issues-with-Qt-6.9.patch
Patch5:         0005-qt-6.10.1.patch
Patch10:        0010-quazip-detect.patch
Patch11:        0011-ngspice-detect.patch
Patch12:        0012-clipper1-detect.patch
Patch20:        0020-ngspice-location.patch
Recommends:     libngspice%{?_isa}
Requires:       %{name}-parts = %{parts_version}-%{release}
%if %{undefined flatpak}
Requires:       electronics-menu
%endif
Requires:       google-droid-sans-fonts
Requires:       google-droid-sans-mono-fonts
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6PrintSupport)
BuildRequires:  pkgconfig(Qt6SerialPort)
BuildRequires:  pkgconfig(Qt6Sql)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  pkgconfig(ngspice)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(polyclipping)
BuildRequires:  pkgconfig(quazip1-qt6)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  svgpp-devel
# /oreon:deps
%description
Fritzing is a free software tool to support designers, artists and
hobbyists to work creatively with interactive electronics.

%package parts
Version: %{parts_version}
Summary: Parts library for the Fritzing electronic design application
BuildArch: noarch
License:       CC-BY-SA-3.0 AND GPL-1.0-or-later
%description parts
A library of part definitions for the Fritzing electronic design application,
containing both metadata and related graphics.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-app-%{app_commit}

%setup -q -T -D -a 1 -n %{name}-app-%{app_commit}
mv %{name}-parts-%{parts_commit}/ parts/

# Remove some GitHub-specific files
rm -rf .github || true
rm -rf parts/.github || true

# The TwitterSaurus examples use (a bundled) twitter4j library, whose license
# is incompatible with Fedora.
rm -f sketches/core/Fritzing\ Creator\ Kit\ DE+EN/creator-kit-*/Fritzing/TwitterSaurus.fzz
rm -f sketches/core/Fritzing\ Creator\ Kit\ DE+EN/creator-kit-*/Processing/twitter4j-core-2.2.5.jar
rm -rf sketches/core/Fritzing\ Creator\ Kit\ DE+EN/creator-kit-*/Processing/TwitterSaurus*
rm -f sketches/core/obsolete/TwitterSaurus.fzz

# Remove a <url> entry which causes the appstream file to fail validation.
sed -e '/<url type="forum">/d' -i '%{rtld_name}.appdata.xml'

%build

%qmake_qt6 PREFIX=%{_prefix}
%make_build V=1
./Fritzing -platform minimal -f ./parts -db ./parts/parts.db
%install
%make_install INSTALL_ROOT=%{buildroot}
find %{buildroot}%{_datadir}/%{name} -type f -exec chmod 644 '{}' ';'
find %{buildroot}%{_datadir}/%{name} -type d -exec chmod 755 '{}' ';'
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{rtld_name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{rtld_name}.appdata.xml
if [[ "$(find %{buildroot}%{_datadir}/%{name} -name 'TwitterSaurus*' -o -name 'twitter4j*' | wc -l)" -gt 0 ]]; then
  echo "Found TwitterSaurus / twitter4j files - these should NOT be included in the final package" >&2
  exit 1
fi
%files -f %{oreon_filedir}/main.list
%files -n fritzing-parts -f %{oreon_filedir}/fritzing-parts.list

%changelog

%autochangelog
