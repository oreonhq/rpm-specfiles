%global source0_hash 3d7c31d5ea314589d2a963290ad16f4d3d631a41e802b8b39f8be0c9f71eb8e9

%global obsNVR 0.12.11

Name:           fbreader
Version:        0.99.4
Release:        20%{?dist}
Summary:        E-book reader

License:        GPL-2.0-or-later
URL:            http://www.fbreader.org/
Source0:        http://www.fbreader.org/files/desktop/fbreader-sources-%{version}.tgz
Patch0:         %{name}-0.99.4-optflags.patch
Patch1:         %{name}-0.99.4-default_browser.patch

# libunibreak dropped i686
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  bzip2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  expat-devel
BuildRequires:  fribidi-devel
BuildRequires:  libcurl-devel
BuildRequires:  libunibreak-devel
BuildRequires:  qt4-devel
BuildRequires:  sqlite-devel
BuildRequires:  zlib-devel
BuildRequires: make

# needed because sometimes the API change without soname bump
Requires:       zlibrary%{?_isa} = %{version}-%{release}
Provides:       %{name}-qt = %{version}-%{release}
Obsoletes:      %{name}-qt < %{obsNVR}
Obsoletes:      %{name}-gtk < %{obsNVR}

# bz #1624218
ExcludeArch:    armv7hl

%description
FBReader is an e-book reader, with the following main features:

* Supports several formats: fb2, HTML, CHM, plucker, Palmdoc, zTxt
  (Weasel), TCR (psion), RTF, OEB, OpenReader, mobipocket, plain text.
* Direct reading from tar, zip, gzip and bzip2 archives. (Multiple
  books in one archive are supported.)
* Automatic library building.
* Automatic encoding detection is supported.
* Automatically generated contents table.
* Embedded images support.
* Footnotes/hyperlinks support.
* Position indicator.
* Keeps the last open book and the last read positions for all opened
  books between runs.
* List of last opened books.
* Automatic hyphenations. Liang's algorithm is used. The same
  algorithm is used in TeX, and TeX hyphenation patterns are used in
  FBReader. Patterns for Czech, English, Esperanto, French, German and
  Russian are included in the current version.
* Text search.
* Full-screen mode.
* Screen rotation by 90, 180 and 270 degrees.

%package -n     zlibrary
Summary:        Cross-platform GUI library
Provides:       zlibrary-ui-qt = %{version}-%{release}
Obsoletes:      zlibrary-ui-qt < %{obsNVR}
Obsoletes:      zlibrary-ui-gtk < %{obsNVR}

%description -n zlibrary
ZLibrary is a cross-platform library to build applications running on
desktop Linux, Windows, and different Linux-based PDAs.

%package -n     zlibrary-devel
Summary:        Development files for zlibrary
Requires:       zlibrary%{?_isa} = %{version}-%{release}

%description -n zlibrary-devel
This package contains the libraries amd header files that are needed
for writing applications with Zlibrary.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

%build
%make_build

%install
%make_install LIBDIR=%{_libdir}
%make_install do_install_dev LIBDIR=%{_libdir}
desktop-file-install \
  --remove-category="Application" \
  --delete-original \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/FBReader.desktop

%ldconfig_scriptlets -n zlibrary

%files
%license fbreader/LICENSE
%doc ChangeLog
%{_bindir}/FBReader
%{_datadir}/FBReader
%{_datadir}/applications/FBReader.desktop
%{_datadir}/pixmaps/FBReader.png
%{_datadir}/pixmaps/FBReader

%files -n zlibrary
%doc fbreader/LICENSE
%{_libdir}/lib*.so.*
%{_datadir}/zlibrary

%files -n zlibrary-devel
%{_includedir}/*
%{_libdir}/lib*.so

%changelog
%autochangelog
