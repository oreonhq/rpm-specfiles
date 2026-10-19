%global source0_hash a0b2ba91caf68ec4ee7705d5063bc542ac8aea4d421451103245c69d272bf19f
Name:           qdirstat
Version:        2.0
Release:        1%{?dist}
Summary:        Qt-based directory statistics
License:        GPL-2.0-only
URL:            https://github.com/shundhammer/qdirstat
Source0:        https://github.com/shundhammer/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(Qt6Core5Compat)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
QDirStat is a graphical application to show where your disk space has gone and
to help you to clean it up.

It shows the total size of directories and of their files both in a traditional
tree view and in a colored treemap graphics where a large file is shown as a
large rectangle, and small files are shown as small rectangles. Click on it, and
you will see where in the tree the file is, and you can instantly move it to the
trash if you like. The color corresponds to the file type: Images, videos or
whatever.

This is a Qt-only port of the old Qt3/KDE3-based KDirStat, now based on the
latest Qt6. It does not need any KDE libs or infrastructure. It runs on every
X11-based desktop on Linux, BSD and other Unix-like systems, and in a Docker
container.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%qmake_qt6
%make_build
%install
%make_install INSTALL_ROOT=%{buildroot}
install -Dp -m 644 metainfo/io.github.shundhammer.qdirstat.metainfo.xml \
    %{buildroot}%{_datadir}/metainfo/io.github.shundhammer.qdirstat.metainfo.xml
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
