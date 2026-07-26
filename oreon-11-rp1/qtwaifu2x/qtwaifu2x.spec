%global source0_hash fe6fe3701cdde45eb7f7fcef74b71792fd90462d6a3771c5992dcbbe02c89f0e

%global commit          2973f6fc99b62346ac954a1192059d3f1c5ede61
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global snapshotdate    20200709

Name:           qtwaifu2x
Version:        0
Release:        0.21.%{snapshotdate}git%{shortcommit}%{?dist}
Summary:        Frontend for waifu2x-converter-cpp

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://github.com/cmdrkotori/qtwaifu2x
Source0:        %url/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        qtwaifu2x.desktop
# Fix noise-scale flag
Patch0:         https://patch-diff.githubusercontent.com/raw/cmdrkotori/qtwaifu2x/pull/3.patch#/0001-Fix-noise-scale-flag.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  qt5-qtbase-devel
Requires:       hicolor-icon-theme
Requires:       waifu2x-converter-cpp

%description
Frontend for waifu2x-converter-cpp.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit}

%build
%qmake_qt5
%make_build

%install
install -Dpm 0755 qtwaifu2x %{buildroot}%{_bindir}/qtwaifu2x
install -Dpm 0644 images/icon.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/qtwaifu2x.png

desktop-file-install                                        \
    --dir=%{buildroot}%{_datadir}/applications              \
    %{SOURCE1}

%files
%license LICENSE
%doc README.md
%{_bindir}/qtwaifu2x
%{_datadir}/applications/qtwaifu2x.desktop
%{_datadir}/icons/hicolor/512x512/apps/qtwaifu2x.png

%changelog
%autochangelog
