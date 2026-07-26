%global source0_hash 647aca4d494315905d236504576e35b7568a4d702e56aa4590295a9f6a7259bd

Name:              zathura
Version:           0.5.14
Release:           2%{?dist}
Summary:           A lightweight document viewer
License:           Zlib
URL:               http://pwmt.org/projects/%{name}/
Source0:           http://pwmt.org/projects/%{name}/download/%{name}-%{version}.tar.xz

%if %{undefined flatpak}
BuildRequires:     bash-completion
%endif
#BuildRequires:     binutils
BuildRequires:     cairo-devel
#BuildRequires:     cmake
BuildRequires:     desktop-file-utils
# Needed for mime-type detection : `libmagic` from file
BuildRequires:     file-devel
%if %{undefined flatpak}
BuildRequires:     fish
%endif
BuildRequires:     cmake
BuildRequires:     gcc
BuildRequires:     gettext
BuildRequires:     girara-devel >= 0.4.5
BuildRequires:     glib2-devel >= 2.72
BuildRequires:     gtk3-devel >= 3.24
BuildRequires:     intltool
# Needed to validate appdata
BuildRequires:     appstream
BuildRequires:     librsvg2-tools
BuildRequires:     libseccomp-devel
BuildRequires:     meson >= 0.61
# Needed to build man pages (/doc subdir)
BuildRequires:     python3-sphinx
BuildRequires:     sqlite-devel >= 3.6.23
BuildRequires:     texlive-lib-devel
BuildRequires:     zsh
# Tests
BuildRequires:     pkgconfig(check) >= 0.11
Buildrequires:     xorg-x11-server-Xvfb
Buildrequires:     weston

Suggests:          zathura-cb
Suggests:          zathusa-djvu
# poppler is preferred over mupdf
Suggests:          zathura-pdf-poppler
Suggests:          zathura-ps

Suggests:          zathura-bash-completion
Suggests:          zathura-fish-completion
Suggests:          zathura-zsh-completion

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
# poppler is preferred over mupdf
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

%autosetup

%build
%meson -Dsynctex=enabled -Dseccomp=enabled -Dtests=enabled
%meson_build

%install
%meson_install
# This duplicates meson_test validate-appdata:
appstreamcli validate --no-net %{buildroot}%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%find_lang org.pwmt.zathura

%check
# Leave out flaky sandbox test which is either skipped or fails strangely:
%meson_test validate-desktop validate-appdata document types utils xvfb_session weston_session

%files -f org.pwmt.zathura.lang
%license LICENSE
%doc README.md
%{_bindir}/*
%{_mandir}/man*/*
%{_datadir}/applications/*
#Directories without known owners: /usr/share/dbus-1, /usr/share/dbus-1/interfaces.  Would Requires dbus ?
%{_datadir}/dbus-1/interfaces/org.pwmt.zathura.xml
%{_datadir}/icons/hicolor/*/apps/org.pwmt.zathura.png
%{_datadir}/icons/hicolor/*/apps/org.pwmt.zathura.svg
%{_datadir}/metainfo/org.pwmt.zathura.appdata.xml

%files devel
%{_includedir}/zathura
%{_libdir}/pkgconfig/zathura.pc

%files plugins-all

%files bash-completion
%{_datadir}/bash-completion/completions/zathura

%files fish-completion
%{_datadir}/fish/vendor_completions.d/zathura.fish

%files zsh-completion
%{_datadir}/zsh/site-functions/_zathura

%changelog
%autochangelog
