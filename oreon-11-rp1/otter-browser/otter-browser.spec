%global source0_hash 2b07d22a5d921ec0b3d29a680eb913c3fe0713ca7d10e37873a3802d1a5154a3
%global __cmake_in_source_build 1
%if ! 0%{?qt5_qtwebengine_arches:1}
%global qt5_qtwebengine_arches %{ix86} x86_64 %{arm} aarch64 mips mipsel mips64el
%endif
%global usesnapshot 0
%if 0%{?usesnapshot}
%global commit0 3dc40e89dc538abe712a65d02ec3d4e3851ab1fb
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global snapshottag .git%{shortcommit0}
%endif
Name:           otter-browser
Summary:        Web browser controlled by the user, not vice-versa
License:        GPL-3.0-or-later AND LicenseRef-Callaway-BSD
%if 0%{?usesnapshot}
Version:        1.0.81
Release:        1%{?dist}
%else
Version:        1.0.03
Release:        1%{?dist}
%endif
URL:            http://otter-browser.org/
Epoch:          1
%if 0%{?usesnapshot}
Source0:        https://github.com/OtterBrowser/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%else
%endif
%ifarch %{qt5_qtwebengine_arches}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  hunspell-devel
BuildRequires:  libappstream-glib
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qtsensors-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  qt5-qtxmlpatterns-devel
# /oreon:deps
%description
Web browser aiming to recreate classic Opera (12.x) UI using Qt5.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?usesnapshot}
%autosetup -n %{name}-%{commit0}
%else
%autosetup -n %{name}-%{version}
%endif

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake .
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/{applications,appdata}
install -Dm 0644 packaging/otter-browser.appdata.xml %{buildroot}%{_datadir}/appdata/otter-browser.appdata.xml
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
   %{name}.desktop
%find_lang %{name} --with-qt
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
