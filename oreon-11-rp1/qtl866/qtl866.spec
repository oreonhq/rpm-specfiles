%global source0_hash 7ab31536ef405d6ebf18dbad0a12c4b64f329f4146afc790e3dd48c9c4ce26c2
%global commit 544d42c6f4f56e641f179ba24b638d017e5ab217
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           qtl866
Version:        0
Release:        1%{?dist}
Summary:        GUI driver for the TL866 (MiniPRO) chip programmer
License:        GPL-3.0-or-later
URL:            https://github.com/wd5gnr/qtl866
Source0:        https://github.com/wd5gnr/%{name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Patch0:         https://github.com/lkundrak/qtl866/commit/6eb0fd70.patch#/0001-Fix-build.patch
Patch1:         https://github.com/lkundrak/qtl866/commit/cdcdc2c9.patch#/0002-Fix-a-typo.patch
Patch2:         https://github.com/lkundrak/qtl866/commit/42d15fb1.patch#/0003-Load-qtparts-on-build.patch
Patch3:         https://github.com/lkundrak/qtl866/commit/9f7553d4.patch#/0004-Add-a-desktop-file-and-an-icon.patch
Patch4:         https://github.com/lkundrak/qtl866/commit/7b3f233b.patch#/0005-Add-AppStream-metadata.patch
Patch5:         https://github.com/lkundrak/qtl866/commit/6a4fe197.patch#/0006-Use-my-clone-in-AppData-for-now.patch
Patch6:         https://github.com/lkundrak/qtl866/commit/006d5dfa.patch#/0007-Make-it-somehow-work-with-Wayland.patch
Requires:       minipro
Requires:       bless
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  git
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
GUI for a programming utility compatible with Minipro TL866CS and Minipro
TL866A chip programmers. Supports more than 13000 target devices
(including AVRs, PICs, various BIOSes and EEPROMs).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
# The binary patch needs to be applied with git
git --git-dir=. apply --unsafe-paths --directory=. --apply %{PATCH4}
%patch -P5 -p1
%patch -P6 -p1

%build

%{_qt5_qmake}
make %{?_smp_mflags}
%install
mkdir -p %{buildroot}%{_bindir}
install binhexedit %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -pm644 qtl866.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
desktop-file-install --dir=%{buildroot}%{_datadir}/applications qtl866.desktop
mkdir -p %{buildroot}%{_datadir}/appdata
install -pm644 qtl866.appdata.xml %{buildroot}%{_datadir}/appdata/
make install INSTALL_ROOT=%{buildroot}
%oreon_autofiles main

%check

appstream-util --nonet validate-relax %{buildroot}%{_datadir}/appdata/qtl866.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
