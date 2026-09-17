%global source0_hash 78199ff925b7cd0ffeb628d47909ca4172f8ff0d8fd8192bb537e0c012e6f4c6

# Disable tests because some of the tools are not available in Fedora
%bcond_with tests

Name:          flacon
Version:       12.0.0
Release:       4%{?dist}
Summary:       Audio File Encoder

License:       LGPL-2.1-or-later
URL:           https://flacon.github.io/
Source0:       https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  uchardet-devel
BuildRequires:  pkgconfig(taglib)
# For %%check
BuildRequires:  %{_bindir}/appstream-util
BuildRequires:  %{_bindir}/desktop-file-validate
%if %{with tests}
# Test deps
BuildRequires:  %{_bindir}/mac
BuildRequires:  %{_bindir}/flac
BuildRequires:  %{_bindir}/wavpack
BuildRequires:  %{_bindir}/ttaenc
%endif
BuildRequires: make
BuildRequires: zlib-devel

# formats/aac.h (encoder)
Recommends:     %{_bindir}/faac
# formats/ape.h (decoder)
Recommends:     %{_bindir}/mac
# formats/flac.h (encoder, decoder)
Recommends:     %{_bindir}/flac
# formats/mp3.h (encoder)
Recommends:     %{_bindir}/lame
# formats/ogg.h (encoder)
Recommends:     %{_bindir}/oggenc
# formats/opus.h (encoder)
Recommends:     %{_bindir}/opusenc
# formats/tta.h (decoder)
Recommends:     %{_bindir}/ttaenc
# formats/wv.h (encoder)
Recommends:     %{_bindir}/wavpack
# formats/wc.h (decoder)
Recommends:     %{_bindir}/wvunpack

%description
Flacon extracts individual tracks from one big audio file containing
the entire album of music and saves them as separate audio files. 
To do this, it uses information from the appropriate CUE file. 
Besides, Flacon makes it possible to conveniently revise or specify 
tags both for all tracks at once or for each tag separately.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake -DBUILD_TESTS=%{?with_tests:Yes}%{!?with_tests:No}
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/com.github.Flacon.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%if %{with tests}
cd %{_target_platform}/tests && ./flacon_test
%endif

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/metainfo/com.github.Flacon.metainfo.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
