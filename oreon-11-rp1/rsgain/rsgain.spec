%global source0_hash 26f7acd1ba0851929dc756c93b3b1a6d66d7f2f36b31f744c8181f14d7b5c8a7

Version:        3.6
%global forgeurl https://github.com/complexlogic/rsgain/
%forgemeta

Name:           rsgain
Release:        %autorelease
Summary:        Simple but powerful ReplayGain 2.0 tagging utility
URL:            %{forgeurl}
Source0:        %{forgesource}

# rsgain: BSD-2-Clause
# CRCpp: BSD-3-Clause
License:        BSD-2-Clause AND BSD-3-Clause

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  inih-devel
BuildRequires:  libavcodec-free-devel
BuildRequires:  libavformat-free-devel
BuildRequires:  libavutil-free-devel
BuildRequires:  libebur128-devel
BuildRequires:  libswresample-free-devel
BuildRequires:  taglib-devel

Provides:       bundled(CRCpp) = 1.2.0.0^20220528git71f2152

%description
rsgain (really simple gain) is a ReplayGain 2.0 command line utility.
It applies loudness metadata tags to your files, while leaving the audio
stream untouched. A ReplayGain-compatible player will dynamically adjust
the volume of your tagged files during playback.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup

%build
%cmake -DUSE_STD_FORMAT=ON -DINSTALL_MANPAGE=ON
%cmake_build

%install
%cmake_install

%check
%ctest
%{buildroot}/%{_bindir}/%{name} custom |& grep -F 'No files were specified'

%files
%license LICENSE
%license LICENSE-CRCpp
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
