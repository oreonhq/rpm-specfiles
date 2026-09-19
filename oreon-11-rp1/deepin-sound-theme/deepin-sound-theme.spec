%global source0_hash 73206d000fe0e33597d33e05572d8e09aae7896d2640d114a0f19f8f1a44582b

Name:           deepin-sound-theme
Version:        15.10.6
Release:        %autorelease
Summary:        Deepin sound theme
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-sound-theme
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make

%description
Sound files for the Deeping Desktop Environment.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build

%install
%make_install

%files
%doc README.md
%license LICENSE
%dir %{_datadir}/sounds/deepin/
%dir %{_datadir}/sounds/deepin/stereo/
%{_datadir}/sounds/deepin/index.theme
%{_datadir}/sounds/deepin/stereo/*.wav

%changelog
%autochangelog
