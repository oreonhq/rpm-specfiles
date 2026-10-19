%global source0_hash bbb85061d2ea3736184fd181d09e598278d28e970983cfb0d7b2f809776efd14
%bcond_with tests
Name:          flacon
Version:       13.0.2
Release:        1%{?dist}
Summary:        Audio File Encoder
License:       LGPL-2.1-or-later
URL:           https://flacon.github.io/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%if %{with tests}
%endif
Recommends:     %{_bindir}/faac
Recommends:     %{_bindir}/mac
Recommends:     %{_bindir}/flac
Recommends:     %{_bindir}/lame
Recommends:     %{_bindir}/oggenc
Recommends:     %{_bindir}/opusenc
Recommends:     %{_bindir}/ttaenc
Recommends:     %{_bindir}/wavpack
Recommends:     %{_bindir}/wvunpack
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  /usr/bin/flac
BuildRequires:  /usr/bin/mac
BuildRequires:  /usr/bin/ttaenc
BuildRequires:  /usr/bin/wavpack
BuildRequires:  cmake
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(taglib)
BuildRequires:  uchardet-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Flacon extracts individual tracks from one big audio file containing
the entire album of music and saves them as separate audio files. 
To do this, it uses information from the appropriate CUE file. 
Besides, Flacon makes it possible to conveniently revise or specify 
tags both for all tracks at once or for each tag separately.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DBUILD_TESTS=%{?with_tests:Yes}%{!?with_tests:No}
%cmake_build
%install
%cmake_install
%find_lang %{name} --with-qt
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/com.github.Flacon.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%if %{with tests}
cd %{_target_platform}/tests && ./flacon_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
