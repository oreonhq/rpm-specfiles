%global source0_hash 71a8394dc78f84c9eebe4e99d80cd2bfbe09bc37574fa7571a391dcc850d9ab3

Name:           media-downloader
Version:        5.3.2
Release:        3%{?dist}
Summary:        GUI frontend to multiple CLI based downloading programs
License:        GPL-2.0-or-later
URL:            https://github.com/mhogomchungu/media-downloader
Source0:        %url/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel
BuildRequires:  desktop-file-utils
Requires: yt-dlp
Requires: aria2

%description
This project is a Qt/C++ based GUI frontend to CLI multiple CLI based tools that
deal with downloading online media.
yt-dlp CLI tool is the default supported tool and other tools can be added by
downloading their extension and a list of supported extensions is managed here.

Features offered:-
 1. The GUI can be used to download any media from any website supported by
    installed extensions.
 2. The GUI offers a configurable list of preset options that can be used to
     download media if they are provided in multiple formats.
 3. The GUI offers an ability to do unlimited number of parallel downloads.
    Be careful with this ability because doing too many parallel downloads may
    cause the host to ban you.
 4. The GUI offers an ability to do batch downloads by entering individual link
    in the UI or telling the app to read them from a local file.
 5. The GUI offers an ability to download playlist from websites that supports
    them like youtube.
 6. The GUI offers ability to manage links to playlist to easily monitor their
    activities(subscriptions).
 7. The GUI is offered in multiple languages and as of this writing, the
    supported languages are English, Chinese, Spanish, Polish, Turkish, Russian,
    Japanese, French and Italian.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n %{name}-%{version}

%build
mkdir build && pushd build
%cmake  -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=release ..
%cmake_build
popd

%install
pushd build
%cmake_install
popd
%find_lang %{name} --all-name --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/translations/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
%autochangelog
