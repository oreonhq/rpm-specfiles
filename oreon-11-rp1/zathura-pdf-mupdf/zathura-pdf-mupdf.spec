%global source0_hash 0125624901cabe3a2fe63315a46e7d966a323c028ff53890dfaf7856adb1f4fc

Name:             zathura-pdf-mupdf

Version:          0.4.4
Release:          9%{?dist}
Summary:          PDF support for zathura via mupdf
License:          Zlib
URL:              https://pwmt.org/projects/%{name}/
Source0:          %{url}/download/%{name}-%{version}.tar.xz
# Upstream patch from 0.4.6 adjusting to shared mupdf library
Patch1:           0001-Update-Debian-build-branch-recent-packaging-changes-.patch
Patch2:           0001-configure-for-shared-mupdf-build.patch

BuildRequires:    binutils
BuildRequires:    cairo-devel
# Needed to validate the desktop file
BuildRequires:    desktop-file-utils
BuildRequires:    gcc
BuildRequires:    git-core
BuildRequires:    girara-devel
BuildRequires:    glib2-devel
# Needed to validate appdata
BuildRequires:    libappstream-glib
BuildRequires:    libjpeg-turbo-devel
BuildRequires:    meson >= 0.43
BuildRequires:    mupdf-devel >= 1.23.9-3
BuildRequires:    zathura-devel >= 0.3.9
Requires:         zathura >= 0.3.9

# Old plugins used alternatives
Conflicts:        zathura-pdf-poppler < 0.2.9

%description
This plugin adds PDF support to zathura using the mupdf rendering engine.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git -p1

%build
%meson
%meson_build

%install
%meson_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml

# Clean the old alternatives link
%pre
[ -L %{_libdir}/zathura/pdf.so ] && rm -f %{_libdir}/zathura/pdf.so || :

%files
%license LICENSE
%doc AUTHORS
%{_libdir}/zathura/libpdf-mupdf.so
%{_datadir}/applications/org.pwmt.zathura-pdf-mupdf.desktop
%{_datadir}/metainfo/org.pwmt.zathura-pdf-mupdf.metainfo.xml

%changelog
%autochangelog
