%global source0_hash c812f2f4446fd5de16734e13c02ea9aa25ba4e3ba9f72b732c0ff90f9ba34935

Name:             zathura-pdf-poppler
Version:          0.3.3
Release:          4%{?dist}
Summary:          PDF support for zathura via poppler
License:          Zlib
URL:              http://pwmt.org/projects/%{name}
Source0:          http://pwmt.org/projects/%{name}/download/%{name}-%{version}.tar.xz

#BuildRequires:    binutils
# Needed to validate the desktop file
BuildRequires:    desktop-file-utils
BuildRequires:    gcc
BuildRequires:    girara-devel
BuildRequires:    glib2-devel
# Needed to validate appdata
BuildRequires:    libappstream-glib
BuildRequires:    meson >= 0.61
BuildRequires:    poppler-glib-devel >= 21.12
BuildRequires:    zathura-devel >= 0.5.3

Requires:         zathura >= 0.5.3
# Old plugins used alternatives
Conflicts:        zathura-pdf-mupdf < 0.3.3

%description
The zathura-pdf-poppler plugin adds PDF support to zathura by using
the poppler rendering engine.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%meson
%meson_build

%install
%meson_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml

# Clean the old alternatives link
%pre
[ -L %{_libdir}/zathura/pdf.so ] || rm -f %{_libdir}/zathura/pdf.so

%files
%license LICENSE
%doc AUTHORS
%{_libdir}/zathura/libpdf-poppler.so
%{_datadir}/applications/org.pwmt.zathura-pdf-poppler.desktop
%{_datadir}/metainfo/org.pwmt.zathura-pdf-poppler.metainfo.xml

%changelog
%autochangelog
