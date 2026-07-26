%global source0_hash a3536243772002d17b9c5fcfd616844134bcfe126ce7b7b24eb971ba1f63365d

Summary:       Graphical front-end for Wine
Name:          playonlinux
Version:       4.4
Release:       18%{?dist}
# playonlinux itself is GPL-3.0-only but uses other source codes, breakdown:
# GPL-2.0-or-later: python/{configurewindow/ConfigureWindow,debug,mainwindow,options,wrapper}.py
# GPL-2.0-or-later: python/{install/InstallWindow,setupwindow/{POL_SetupFrame,gui_server}}.py
# GPL-2.0-or-later: python/wine_versions/WineVersionsWindow.py
# MIT: src/check_direct_rendering.c
License:       GPL-3.0-only AND GPL-2.0-or-later AND MIT
URL:           https://www.playonlinux.com/
Source0:       https://github.com/PlayOnLinux/POL-POM-4/archive/%{version}/POL-POM-4-%{version}.tar.gz
# Upstream changes since last release
Patch0:        https://github.com/PlayOnLinux/POL-POM-4/compare/4.4...76a6580.patch#/playonlinux-4.4-git76a6580.patch
BuildRequires: gcc
BuildRequires: make
BuildRequires: gzip
BuildRequires: mesa-libGL-devel
BuildRequires: python3
BuildRequires: python3-devel
BuildRequires: python3-natsort
BuildRequires: python3-wxpython4
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: libappstream-glib
Requires:      python3
Requires:      python3-natsort
Requires:      python3-wxpython4
# Required by python/mainwindow.py
Requires:      nc
Requires:      tar
Requires:      cabextract
Requires:      ImageMagick
Requires:      wget
Requires:      curl
Requires:      gnupg2
Requires:      xterm
%if 0%{?fedora} || 0%{?rhel} > 9
Requires:      gettext-runtime
%else
Requires:      gettext
%endif
Requires:      icoutils
Requires:      wine
Requires:      unzip
Requires:      jq
Requires:      p7zip-plugins
# Wine supported on these arches
ExclusiveArch: %{arm} aarch64 %{ix86} x86_64

%description
New users can often find Wine to be intimidating and difficult to use.

PlayOnLinux is a graphical front-end for Wine which allows to easily
install and use numerous games and applications designed to run with
Microsoft Windows.

PlayOnLinux has the database of Windows applications from which the user
can install desired application with a few clicks. It will automatically
setup the Wine prefix and download any required Windows libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n POL-POM-4-%{version}

%build
%make_build \
  CFLAGS="$RPM_OPT_FLAGS $RPM_LD_FLAGS" \
  PYTHON="%{__python3} -m py_compile"

%install
%make_install

# Remove shebang from Python library
sed '1{/^#!\//d}' -i %{buildroot}%{_datadir}/%{name}/python/setupwindow/gui_server.py

# Remove misplaced files and directories
rm -rf %{buildroot}%{_datadir}/%{name}/{bin,tests,CHANGELOG.md,LICENCE,README.md,TRANSLATORS}
rm -f %{buildroot}%{_datadir}/%{name}/etc/PlayOnLinux.{appdata.xml,desktop}

# Byte compile importable Python modules outside of standard paths
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/%{name}/python/

%find_lang pol

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/PlayOnLinux.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/PlayOnLinux.appdata.xml

%files -f pol.lang
%license LICENCE doc/copyright
%doc CHANGELOG.md README.md TRANSLATORS
%{_bindir}/%{name}
%{_bindir}/%{name}-pkg
%{_libexecdir}/%{name}-check_dd
%{_datadir}/%{name}/
%{_datadir}/appdata/PlayOnLinux.appdata.xml
%{_datadir}/applications/PlayOnLinux.desktop
%{_datadir}/pixmaps/%{name}*.png
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-pkg.1*

%changelog
%autochangelog
