%global source0_hash 1aa2c068722a0ed2df724118933114e1c101defd0aedd5c18d35a177de1a27c1

Name:           fritzing
%global rtld_name org.fritzing.Fritzing

Summary:        Electronic Design Automation software; from prototype to product
License:        GPL-3.0-or-later
URL:            https://fritzing.org/

%global version_no 1.0.6
Release:        3%{?dist}

# The upstream developer no longer marks their releases with git tags.
# The official website says that v1.0.6 was released on 2025-10-21.
#
# There are no commits in the fritzing-app repo on that date.
# The latest commit before that date is the one listed below.
%global app_date 20251007
%global app_commit 04e5bb0241e8f1de24d0fce9be070041c6d5b68e

# There are no commits in the fritzing-parts repo on release date.
# The latest commit made before that date is the one listed below.
%global parts_date 20251007
%global parts_commit 73bc0559bb8399b2f895d68f032e41d7efc720c0

# Include the commit date in the version numbers
%global app_version %{version_no}^%{app_date}
%global parts_version %{version_no}^%{parts_date}

Version:        %{app_version}

Source0:        https://github.com/%{name}/%{name}-app/archive/%{app_commit}/%{name}-app-%{app_commit}.tar.gz
Source1:        https://github.com/%{name}/%{name}-parts/archive/%{parts_commit}/%{name}-parts-%{parts_commit}.tar.gz

# Fedora-specific patch to disable internal auto-updating feature.
# Also removes dependency of libgit2 (used only during the auto-update process).
Patch0:         0000-disable-autoupdate.patch
# Remove references to example sketches that use twitter4j library
Patch2:         0002-remove-twitter4j.patch
# Remove the "Qt version cannot be greater than X.Y.Z" check.
Patch3:         0003-maximum-qt-version.patch

# Fix build issued with Qt 6.9.
# Borrowed from: https://aur.archlinux.org/cgit/aur.git/plain/0004-Work-around-build-issues-with-Qt-6.9.patch?h=fritzing
Patch4:         0004-Work-around-build-issues-with-Qt-6.9.patch

# Fix build error with Qt 6.10.1
Patch5:         0005-qt-6.10.1.patch

# Point library detection scripts to system-provided libs.
Patch10:        0010-quazip-detect.patch
Patch11:        0011-ngspice-detect.patch
Patch12:        0012-clipper1-detect.patch

# Fix program looking for ngspice library in /lib instead of /lib64.
Patch20:        0020-ngspice-location.patch

BuildRequires:  pkgconfig(ngspice)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(polyclipping)
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
BuildRequires:  pkgconfig(quazip1-qt6)
BuildRequires:  pkgconfig(zlib)

BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  svgpp-devel

# Needed for simulations, dlopened at runtime
Recommends:     libngspice%{?_isa}

Requires:       %{name}-parts = %{parts_version}-%{release}
%if %{undefined flatpak}
Requires:       electronics-menu
%endif
Requires:       google-droid-sans-fonts
Requires:       google-droid-sans-mono-fonts

%description
Fritzing is a free software tool to support designers, artists and
hobbyists to work creatively with interactive electronics.

%package parts
Version: %{parts_version}
Summary: Parts library for the Fritzing electronic design application
BuildArch: noarch

# The overall distribution is licensed as CC-BY-SA (see LICENSE.txt), but
# many individual SVG parts in the svg/ directory are licensed as GPL+;
# please see the fz:attr elements named "dist-license", "use-license", and
# "license-url" under the rdf:RDF section of each SVG document for details.
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

# Generate the parts database
./Fritzing -platform minimal -f ./parts -db ./parts/parts.db

%install
%make_install INSTALL_ROOT=%{buildroot}

# A few files in /usr/share/fritzing end up executable.
find %{buildroot}%{_datadir}/%{name} -type f -exec chmod 644 '{}' ';'
find %{buildroot}%{_datadir}/%{name} -type d -exec chmod 755 '{}' ';'

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rtld_name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{rtld_name}.appdata.xml

if [[ "$(find %{buildroot}%{_datadir}/%{name} -name 'TwitterSaurus*' -o -name 'twitter4j*' | wc -l)" -gt 0 ]]; then
  echo "Found TwitterSaurus / twitter4j files - these should NOT be included in the final package" >&2
  exit 1
fi

%files
%doc README.md LICENSE.GPL2 LICENSE.GPL3 LICENSE.CC-BY-SA
%{_bindir}/Fritzing
%{_datadir}/applications/%{rtld_name}.desktop
%{_datadir}/mime/packages/fritzing.xml
%{_datadir}/pixmaps/fritzing.png
%{_metainfodir}/%{rtld_name}.appdata.xml
%{_mandir}/man?/*

%files parts
%doc parts/README.md
%license parts/LICENSE.txt
%{_datadir}/%{name}

%changelog
%autochangelog
