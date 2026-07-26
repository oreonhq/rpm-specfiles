%global source0_hash 5dd63dc6fdb73bfec2030ac5d3cfb44963b082a98b8d0258a30a88f6a75ced6b

Name: liberation-circuit
Summary: Real-time strategy game with programmable units
# Automatically converted from old format: GPLv3 - review is highly recommended.
License: GPL-3.0-only

URL: https://linleyh.itch.io/liberation-circuit

%global git_date 20220102
%global git_commit_long 19e3363547793e931fd9419b61ebc2cd8e257714
%global git_commit_short %(c="%{git_commit_long}"; echo "${c:0:8}")

Version: 1.3
Release: 20.%{git_date}git%{git_commit_short}%{?dist}

%global repo_url https://github.com/linleyh/%{name}
Source0: %{repo_url}/archive/%{git_commit_long}/%{name}-%{git_commit_long}.tar.gz

BuildRequires: allegro5-devel
BuildRequires: allegro5-addon-acodec-devel
BuildRequires: allegro5-addon-audio-devel
BuildRequires: allegro5-addon-dialog-devel
BuildRequires: allegro5-addon-image-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: mesa-libGL-devel
BuildRequires: make

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

Requires: hicolor-icon-theme
Requires: %{name}-data = %{version}-%{release}

%description
Escape from a hostile computer system! Harvest data to create an armada
of battle-processes to aid your escape. Take command directly and play the game
as an RTS, or use the game's built-in editor and compiler to write
your own unit AI in a simplified version of C.

%package data
Summary: Data files required to play Liberation Circuit
BuildArch: noarch

%description data
This package contains assets, such as graphics and sound effects,
required to play Liberation Circuit.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{git_commit_long}

# Fix Makefile overriding CFLAGS
sed -e 's|CFLAGS\s*=\s*|CFLAGS += |g' -i Makefile

%build
%make_build

cat > bin/%{name}-wrapper << EOF
#!%{_bindir}/sh
cd %{_datadir}/%{name}
%{_libexecdir}/%{name} "\$@"
EOF

%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 bin/%{name}-wrapper  %{buildroot}%{_bindir}/%{name}

install -m 755 -d %{buildroot}%{_libexecdir}/
install -m 755 bin/libcirc  %{buildroot}%{_libexecdir}/%{name}

install -m 755 -d %{buildroot}%{_datadir}/%{name}
for FILE in data proc story init.txt; do
  cp -a "bin/${FILE}" "%{buildroot}%{_datadir}/%{name}/${FILE}"
done

install -m 755 -d %{buildroot}%{_datadir}/applications
desktop-file-install linux-packaging/%{name}.desktop \
  --dir=%{buildroot}%{_datadir}/applications/

install -m 755 -d %{buildroot}%{_metainfodir}
cp -a linux-packaging/%{name}.appdata.xml %{buildroot}%{_metainfodir}/%{name}.appdata.xml

for ICONSIZE in 16 32 256; do
  ICONDIR="%{buildroot}%{_datadir}/icons/hicolor/${ICONSIZE}x${ICONSIZE}/apps"
  install -m 755 -d "${ICONDIR}"
  cp -a "linux-packaging/icon-${ICONSIZE}px.png" "${ICONDIR}/%{name}.png"
done

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files
%doc bin/Manual.html
%license LICENSE.md
%{_bindir}/%{name}
%{_libexecdir}/%{name}
%{_datadir}/applications/%{name}.*
%{_metainfodir}/%{name}.*
%{_datadir}/icons/hicolor/**/apps/%{name}.png

%files data
%license bin/licence.txt
%{_datadir}/%{name}

%changelog
%autochangelog
