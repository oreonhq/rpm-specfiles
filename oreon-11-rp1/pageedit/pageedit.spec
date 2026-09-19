%global source0_hash 44665e4e758559314687fa4535e0767fed4b1c7db2fe8f49e3492fecf37bb243

Name:           pageedit
Version:        2.7.6
Release:        1%{?dist}
Summary:        ePub visual XHTML editor

License:        GPL-3.0-or-later AND Apache-2.0
URL:            https://sigil-ebook.com/
Source0:        https://github.com/Sigil-Ebook/PageEdit/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  desktop-file-utils

Provides:       bundled(gumbo) = 0.9.2

ExclusiveArch: %{qt6_qtwebengine_arches}

%description
An ePub visual XHTML editor based on Sigil's Deprecated BookView.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n PageEdit-%{version}

%build
%cmake -DINSTALL_BUNDLED_DICTS=0 -DSHARE_INSTALL_PREFIX:PATH=%{_prefix}
%cmake_build

%install
%cmake_install

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license COPYING.txt
%doc ChangeLog.txt README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.svg

%changelog
%autochangelog
