%global source0_hash a3536243772002d17b9c5fcfd616844134bcfe126ce7b7b24eb971ba1f63365d
Summary:        Graphical front-end for Wine
Name:          playonlinux
Version:       4.4
Release:        1%{?dist}
License:       GPL-3.0-only AND GPL-2.0-or-later AND MIT
URL:           https://www.playonlinux.com/
Source0:        https://github.com/PlayOnLinux/POL-POM-4/archive/%{version}/POL-POM-4-%{version}.tar.gz
Patch0:        https://github.com/PlayOnLinux/POL-POM-4/compare/4.4...76a6580.patch#/playonlinux-4.4-git76a6580.patch
Requires:      python3
Requires:      python3-natsort
Requires:      python3-wxpython4
Requires:      nc
Requires:      tar
Requires:      cabextract
Requires:      ImageMagick
Requires:      wget
Requires:      curl
Requires:      gnupg2
Requires:      xterm
Requires:      gettext
Requires:      icoutils
Requires:      wine
Requires:      unzip
Requires:      jq
Requires:      p7zip-plugins
ExclusiveArch: %{arm} aarch64 %{ix86} x86_64
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gzip
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-natsort
BuildRequires:  python3-wxpython4
# /oreon:deps
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
%global oreon_srcdir POL-POM-4-%{version}
%oreon_prep
%build

%make_build \
  CFLAGS="$RPM_OPT_FLAGS $RPM_LD_FLAGS" \
  PYTHON="%{__python3} -m py_compile"
%install
%make_install
sed '1{/^#!\//d}' -i %{buildroot}%{_datadir}/%{name}/python/setupwindow/gui_server.py
rm -rf %{buildroot}%{_datadir}/%{name}/{bin,tests,CHANGELOG.md,LICENCE,README.md,TRANSLATORS}
rm -f %{buildroot}%{_datadir}/%{name}/etc/PlayOnLinux.{appdata.xml,desktop}
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/%{name}/python/
%find_lang pol
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/PlayOnLinux.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/PlayOnLinux.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
