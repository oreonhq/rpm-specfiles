%global source0_hash 9efc4a92f8b2d03e5a1b80756d3ae4249d8d6efdb10e311795e8cdd8e35a9f87
Name:              zathura
Version:           2026.07.18
Release:        1%{?dist}
Summary:        A lightweight document viewer
License:           Zlib
URL:               http://pwmt.org/projects/%{name}/
Source0:        http://pwmt.org/projects/%{name}/download/%{name}-%{version}.tar.xz
%if %{undefined flatpak}
%endif
%if %{undefined flatpak}
%endif
Suggests:          zathura-cb
Suggests:          zathusa-djvu
Suggests:          zathura-pdf-poppler
Suggests:          zathura-ps
Suggests:          zathura-bash-completion
Suggests:          zathura-fish-completion
Suggests:          zathura-zsh-completion
# oreon:deps
BuildRequires:  appstream
BuildRequires:  bash-completion
BuildRequires:  cairo-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  file-devel
BuildRequires:  fish
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  girara-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  librsvg2-tools
BuildRequires:  libseccomp-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(check)
BuildRequires:  python3-sphinx
BuildRequires:  sqlite-devel
BuildRequires:  texlive-lib-devel
BuildRequires:  weston
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  zsh
# /oreon:deps
%description
Zathura is a highly customizable and functional document viewer.
It provides a minimalistic and space saving interface as well as
an easy usage that mainly focuses on keyboard interaction.

Zathura requires plugins to support document formats.
For instance:
* zathura-pdf-poppler to open PDF files,
* zathura-ps to open PostScript files,
* zathura-djvu to open DjVu files, or
* zathura-cb to open comic book files.

All of these are available as separate packages in Fedora.
A zathura-plugins-all package is available should you want
to install all available plugins.

%package devel
Summary:           Development files for the zathura PDF viewer
Requires:          %{name}%{?_isa} = %{version}-%{release}
Requires:          pkgconfig
%description devel
libraries and header files for the zathura PDF viewer.

%package plugins-all
Summary:           Zathura plugins (all plugins)
Requires:          zathura-cb
Requires:          zathura-djvu
Requires:          zathura-pdf-poppler
Requires:          zathura-ps
%description plugins-all
This package installs all available Zathura plugins.

%package bash-completion
Summary:           bash-completion files for zathura
BuildArch:         noarch
Requires:          bash-completion
Requires:          %{name} = %{version}-%{release}
%description bash-completion
This package provides %{summary}.

%package fish-completion
Summary:           fish-completion files for zathura
BuildArch:         noarch
Requires:          fish
Requires:          %{name} = %{version}-%{release}
%description fish-completion
This package provides %{summary}.

%package zsh-completion
Summary:           zsh-completion files for zathura
BuildArch:         noarch
Requires:          zsh
Requires:          %{name} = %{version}-%{release}
%description zsh-completion
This package provides %{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dsynctex=enabled -Dseccomp=enabled -Dtests=enabled
%meson_build
%install
%meson_install
appstreamcli validate --no-net %{buildroot}%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%find_lang org.pwmt.zathura
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test validate-desktop validate-appdata document types utils xvfb_session weston_session
%files -f %{oreon_filedir}/main.list
%files -n zathura-devel -f %{oreon_filedir}/zathura-devel.list
%files -n zathura-plugins-all -f %{oreon_filedir}/zathura-plugins-all.list
%files -n zathura-bash-completion -f %{oreon_filedir}/zathura-bash-completion.list
%files -n zathura-fish-completion -f %{oreon_filedir}/zathura-fish-completion.list
%files -n zathura-zsh-completion -f %{oreon_filedir}/zathura-zsh-completion.list

%changelog

%autochangelog
