%global source0_hash d2085fd2e55875dcecd12efd8e7ba3b1498efecede123d10c3dc60b2334c8377
Name:           anagramarama
Version:        0.9
Release:        1%{?dist}
Summary:        Anagram puzzle game
License:        GPL-2.0-or-later AND CC-BY-3.0
URL:            http://identicalsoftware.com/anagramarama/
Source0:        http://identicalsoftware.com/%{name}//%{name}-%{version}.tgz
Requires:      hicolor-icon-theme
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libgamerzilla-devel
BuildRequires:  make
# /oreon:deps
%description
Anagramarama is a simple wordgame in which one tries to guess all the different
permutations of a scrambled word which form another word within the
time limit.  Guess the original word and you move on to the next
level.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
