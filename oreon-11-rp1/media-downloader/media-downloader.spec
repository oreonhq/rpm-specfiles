%global source0_hash 1308e2fc2b6ffd459918d24006c5da8472711765179f71a0ee6ffba2350ded55
Name:           media-downloader
Version:        5.6.6
Release:        1%{?dist}
Summary:        GUI frontend to multiple CLI based downloading programs
License:        GPL-2.0-or-later
URL:            https://github.com/mhogomchungu/media-downloader
Source0:        https://github.com/mhogomchungu/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires: yt-dlp
Requires: aria2
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
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
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
