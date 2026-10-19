%global source0_hash 44b23f81481ac4d076fabc6059d0d41c9892974e8e22864b97de3f37d91d5e23
%global build_number 914-2404
ExcludeArch: %{ix86}
Name:    web-eid
Version: 2.8.0
Release:        1%{?dist}
Summary:        Web eID browser extension helper application
License: MIT
URL:     https://github.com/web-eid/web-eid-app
Source0:        https://github.com/%{name}/%{name}-app/releases/download/v%{version}/%{name}_%{version}.%{build_number}.tar.xz
Requires: hicolor-icon-theme
Requires: mozilla-filesystem
Requires: qt6-qtbase
Requires: qt6-qtsvg
Provides: bundled(libelectronic-id)
# oreon:deps
BuildRequires:  bash
BuildRequires:  clang
BuildRequires:  desktop-file-utils
BuildRequires:  git
BuildRequires:  git-clang-format
BuildRequires:  gtest
BuildRequires:  gtest-devel
BuildRequires:  openssl-devel
BuildRequires:  pcsc-lite
BuildRequires:  pcsc-lite-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  valgrind
# /oreon:deps
%description
The Web eID application performs cryptographic digital signing and
authentication operations with electronic ID smart cards for the Web eID
browser extension (it is the native messaging host for the extension). Also
works standalone without the extension in command-line mode.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}
%oreon_prep
%build

%cmake -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}
%cmake_build
%install
%cmake_install
install -m 644 -Dt %{buildroot}/%{_sysconfdir}/chromium/native-messaging-hosts %{buildroot}/%{_datadir}/web-eid/eu.webeid.json
install -m 644 -Dt %{buildroot}/%{_sysconfdir}/opt/chrome/native-messaging-hosts %{buildroot}/%{_datadir}/web-eid/eu.webeid.json
rm -f %{buildroot}/%{_datadir}/web-eid/eu.webeid.json
%oreon_autofiles main

%check

export QT_QPA_PLATFORM='offscreen' # needed for running headless tests
%ctest
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%post

/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
%postun

if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
%posttrans

/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
