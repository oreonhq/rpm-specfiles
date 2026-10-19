%global source0_hash 9e67e2301c59bd58ec27f1c7da23502c7c1f64731fe5894152c1de01751a81da
Name:           nfoview
Version:        2.1
Release:        1%{?dist}
Summary:        Viewer for NFO files
License:        GPL-3.0-or-later
URL:            https://otsaloma.io/nfoview/
Source0:        https://github.com/otsaloma/nfoview/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       shared-mime-info
Requires:       hicolor-icon-theme
Requires:       python3-gobject
Requires:       terminus-fonts
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
NFO Viewer is a simple viewer for NFO files, which are "ASCII" art in
the CP437 codepage. The advantages of using NFO Viewer instead of a
text editor are preset font and encoding settings, automatic window
size and clickable hyperlinks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build PREFIX=%{_prefix}
%install
%make_install PREFIX=%{_prefix}
desktop-file-install                                        \
    --add-category="TextTools;"                             \
    --remove-category="Viewer;"                             \
    --delete-original                                       \
    --dir=%{buildroot}%{_datadir}/applications              \
    %{buildroot}%{_datadir}/applications/io.otsaloma.nfoview.desktop
%find_lang %{name}
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/io.otsaloma.nfoview.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
