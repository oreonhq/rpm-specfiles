%global source0_hash 9b0da3e560e0448c743bebc017440f004ec68b3504d5a2af594f4ed1bc9135a7

Name:           nitrokey-app
Version:        1.4.2
Release:        14%{?dist}
Summary:        Nitrokey's Application

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/Nitrokey/nitrokey-app
Source0:        %{url}/archive/v%{version_no_tilde -}/%{name}-%{version}.tar.gz
# Non-upstreamable, required to unbundle libraries
Patch0001:      0001-don-t-show-information-about-3rd-party-licenses.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.1.0
BuildRequires:  ninja-build
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(libnitrokey-1) >= 3.5
BuildRequires:  pkgconfig(cppcodec-1)
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  /usr/bin/appstream-util
Requires:       hicolor-icon-theme

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

# We don't need ubuntu icons
rm -vr %{buildroot}%{_datadir}/icons/ubuntu*

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/com.nitrokey.%{name}.appdata.xml

%files
%license LICENSES/GPLv3
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/com.nitrokey.%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.png
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}

%changelog
%autochangelog
