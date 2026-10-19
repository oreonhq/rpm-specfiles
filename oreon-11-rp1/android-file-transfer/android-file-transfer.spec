%global source0_hash 0f366a8d659926d3859a8628d4f7592692389b060f67da9a936d19b252b42d96
%undefine __cmake_in_source_build
Name:           android-file-transfer
Version:        4.5
Release:        1%{?dist}
Summary:        Reliable Android MTP client with minimalist UI
License:        LGPL-2.1-only
URL:            https://github.com/whoozle/android-file-transfer-linux
Source0:        https://github.com/whoozle/%{name}-linux/archive/v%{version}/%{name}-linux-%{version}.tar.gz
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(pybind11)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(Qt6)
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(taglib)
# /oreon:deps
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
%global oreon_srcdir %{name}-linux-%{version}
%oreon_prep
%build

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
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
