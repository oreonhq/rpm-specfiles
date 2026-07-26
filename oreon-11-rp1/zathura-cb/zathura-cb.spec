%global source0_hash 4e201ea54cdc20a93258c43556f6389441af99740de7dca6ca1ff524172fbd47

Name:             zathura-cb
Version:          0.1.11
Release:          4%{?dist}
Summary:          Comic book support for zathura
License:          Zlib
URL:              https://pwmt.org/projects/%{name}
Source0:          https://pwmt.org/projects/%{name}/download/%{name}-%{version}.tar.xz

#BuildRequires:    binutils
BuildRequires:    cairo-devel
# Needed to validate the desktop file
BuildRequires:    desktop-file-utils
BuildRequires:    gcc
BuildRequires:    girara-devel
# Needed to validate appdata
BuildRequires:    libappstream-glib
BuildRequires:    libarchive-devel
BuildRequires:    meson >= 0.43
BuildRequires:    zathura-devel >= 0.3.8

Requires:         zathura >= 0.3.8

%description
The zathura-cb plugin adds comic book archive support to zathura.

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
%{_libdir}/zathura/libcb.so
%{_datadir}/applications/org.pwmt.zathura-cb.desktop
%{_datadir}/metainfo/org.pwmt.zathura-cb.metainfo.xml

%changelog
%autochangelog
