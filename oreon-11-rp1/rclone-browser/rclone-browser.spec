%global source0_hash 5f8242a011b85477749127b7e94e874035c431c2fa6df817e5603ed891604beb

# Force out of source build
%undefine __cmake_in_source_build

Name:           rclone-browser
Version:        1.8.0
Release:        15%{?dist}
Summary:        Simple cross platform GUI for rclone

License:        Unlicense
URL:            https://github.com/kapitainsky/RcloneBrowser
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(Qt5)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  hicolor-icon-theme
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
Requires:       rclone

%description
Simple cross platfrom GUI for rclone command line tool.

Features:
 - Allows to browse and modify any rclone remote, including encrypted ones
 - Uses same configuration file as rclone, no extra configuration required
 - Supports custom location and encryption for .rclone.conf configuration file
 - Simultaneously navigate multiple repositories in separate tabs
 - Lists files hierarchically with file name, size and modify date
 - All rclone commands are executed asynchronously, no freezing GUI
 - File hierarchy is lazily cached in memory, for faster traversal of folders
 - Allows to upload, download, create new folders, rename or delete files and
   folders
 - Allows to calculate size of folder, export list of files and copy rclone
   command to clipboard
 - Can process multiple upload or download jobs in background
 - Drag & drop support for dragging files from local file explorer for
   uploading
 - Streaming media files for playback in player like mpv or similar
 - Mount and unmount folders on macOS and GNU/Linux
 - Optionally minimizes to tray, with notifications when upload/download
   finishes
 - Supports portable mode (create .ini file next to executable with same 
   name), rclone and .rclone.conf path now can be relative to executable

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n RcloneBrowser-%{version}
# Do not report warnings as errors
sed -i "s|-Werror ||" src/CMakeLists.txt

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install
install -Dpm 0644 assets/rclone-browser.appdata.xml %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.appdata.xml

%changelog
%autochangelog
