%global source0_hash 0f366a8d659926d3859a8628d4f7592692389b060f67da9a936d19b252b42d96

# Force out of source build
%undefine __cmake_in_source_build

Name:           android-file-transfer
Version:        4.5
Release:        7%{?dist}
Summary:        Reliable Android MTP client with minimalist UI

License:        LGPL-2.1-only
URL:            https://github.com/whoozle/android-file-transfer-linux
Source0:        %{url}/archive/v%{version}/%{name}-linux-%{version}.tar.gz

Requires:       hicolor-icon-theme
BuildRequires:  cmake
BuildRequires:  cmake(pybind11)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(Qt6)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(taglib)

%description
Android File Transfer for Linux — reliable MTP client with minimalist UI
similar to Android File Transfer for Mac.
Features:
- Simple Qt UI with progress dialogs.
- FUSE wrapper (If you'd prefer mounting your device), supporting partial
  read/writes, allowing instant access to your files.
- No file size limits.
- Automatically renames album cover to make it visible from media player.
- USB 'Zerocopy' support found in recent Linux kernel
- No extra dependencies (e.g. libptp/libmtp).
- Command line tool (aft-mtp-cli)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-linux-%{version}

%build
# QT requires the main program not to perform local symbol binding,
# -fPIC accomplishes that
export CXXFLAGS="-fPIC $RPM_OPT_FLAGS"
%cmake -GNinja
%cmake_build

%install
%cmake_install
find %{buildroot} -name '*.a' -delete
desktop-file-install                                       \
    --remove-category="System"                             \
    --remove-category="Filesystem"                         \
    --delete-original                                      \
    --dir=%{buildroot}%{_datadir}/applications             \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files
%license LICENSE
%doc README.md FAQ.md
%{_bindir}/*
%{_datadir}/icons/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml

%changelog
%autochangelog
