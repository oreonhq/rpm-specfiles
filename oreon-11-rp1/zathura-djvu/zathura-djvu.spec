%global source0_hash 32e9d89929a76cd7d3fcbaf79f441868bdabedf17317d1d1843faa1f19338d95

Name:             zathura-djvu
Version:          0.2.10
Release:          4%{?dist}
Summary:          DjVu support for zathura
License:          Zlib
URL:              http://pwmt.org/projects/%{name}
Source0:          http://pwmt.org/projects/%{name}/download/%{name}-%{version}.tar.xz

#BuildRequires:    binutils
BuildRequires:    cairo-devel
#BuildRequires:    coreutils
BuildRequires:    djvulibre-devel
# Needed to validate the desktop file
BuildRequires:    desktop-file-utils
BuildRequires:    girara-devel
BuildRequires:    glib2-devel
# Needed to validate appdata
BuildRequires:    libappstream-glib
BuildRequires:    meson >= 0.43
BuildRequires:    gcc
BuildRequires:    zathura-devel >= 0.3.8

Requires:         zathura >= 0.3.8

%description
The zathura-djvu plugin adds DjVu support to zathura by
using the djvulibre library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%meson
%meson_build

%install
%meson_install
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml

%files
%license LICENSE
%doc AUTHORS
%{_libdir}/zathura/libdjvu.so
%{_datadir}/applications/org.pwmt.zathura-djvu.desktop
%{_datadir}/metainfo/org.pwmt.zathura-djvu.metainfo.xml

%changelog
%autochangelog
