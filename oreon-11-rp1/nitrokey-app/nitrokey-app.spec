%global source0_hash 9b0da3e560e0448c743bebc017440f004ec68b3504d5a2af594f4ed1bc9135a7
Name:           nitrokey-app
Version:        1.4.2
Release:        1%{?dist}
Summary:        Nitrokey's Application
License:        GPL-3.0-or-later
URL:            https://github.com/Nitrokey/nitrokey-app
Source0:        https://github.com/Nitrokey/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0001:      0001-don-t-show-information-about-3rd-party-licenses.patch
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  cmake
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(cppcodec-1)
BuildRequires:  pkgconfig(libnitrokey-1)
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Remove 3rdparty libraries
rm -vr 3rdparty
# Unbundle libnitrokey
rm -vr libnitrokey

%build

%cmake %{_vpath_srcdir} -B%{_vpath_builddir} -GNinja \
  -DADD_GIT_INFO=FALSE \
  %{nil}
%ninja_build -C %{_vpath_builddir}
%install
%ninja_install -C %{_vpath_builddir}
rm -vr %{buildroot}%{_datadir}/icons/ubuntu*
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/com.nitrokey.%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
