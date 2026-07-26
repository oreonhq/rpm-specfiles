%global source0_hash 5657f64f5ed8a349447197af9d72b965c5da61ca7f521f3a3ed23603c71648e0

%global icondir %{_datadir}/icons/hicolor
%global reponame danmaQ

Name:		danmaq
Version:	0.2.3.2
Release:	18%{?dist}
Summary:	A small client side Qt program to play danmaku on any screen

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		https://github.com/TUNA/%{reponame}
Source0:        %{url}/archive/v%{version}/%{reponame}-v%{version}.tar.gz

BuildRequires:	qt5-qtx11extras-devel
BuildRequires:	qt5-qtbase-devel
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:  libXext-devel

%description
DanmaQ is a small client side Qt program to play danmaku on any screen.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{reponame}-%{version}

%build
mkdir build && cd build
%cmake3 ..
# Since 0.2.3 it cannot be built in parallel. So use make instead of macro.
%cmake_build

%install
# install 
pushd build
%cmake_install
#install -Dm 0755 build/src/%{reponame} %{buildroot}%{_bindir}/%{reponame}
popd

# icon files
install -Dm0644 src/icons/statusicon.ico    %{buildroot}%{_datadir}/pixmaps/statusicon.ico
install -Dm0644 src/icons/statusicon.png    %{buildroot}%{_datadir}/pixmaps/statusicon.png
install -Dm0644 src/icons/statusicon_disabled.png    %{buildroot}%{_datadir}/pixmaps/statusicon_disabled.png
install -Dm0644 src/icons/statusicon.svg %{buildroot}%{icondir}/scalable/apps/statusicon.svg
install -Dm0644 src/resource/danmaQ.desktop %{buildroot}%{_datadir}/applications/%{reponame}.desktop
install -Dm0644 src/resource/danmaQ.png    %{buildroot}%{_datadir}/pixmaps/danmaQ.png
install -Dm0644 src/resource/danmaQ.svg %{buildroot}%{icondir}/scalable/apps/danmaQ.svg

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{reponame}.desktop

%post
/bin/touch --no-create %{_datadir}/icons/scalable &>/dev/null ||:

%postun
if [ $1 -eq 0 ]; then
  /bin/touch --no-create %{_datadir}/icons/scalable &>/dev/null ||:
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/scalable &>/dev/null ||:
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/scalable &>/dev/null ||:

%files
%doc README.md
%license LICENSE
%{_bindir}/%{reponame}
%{_mandir}/man1/%{reponame}.1.gz
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/%{reponame}.desktop

%changelog
%autochangelog
