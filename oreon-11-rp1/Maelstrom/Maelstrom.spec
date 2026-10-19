%global source0_hash 93680322f4b04d4727ea8e0b461f259b604dc69e7465cb91d2b9aad378a9a036
Name:           Maelstrom
Version:        4.0.2
Release:        1%{?dist}
Summary:        A space combat game
License:        GPL-2.0-or-later AND CC-BY-3.0
URL:            http://www.libsdl.org/projects/Maelstrom/
Source0:        http://www.libsdl.org/projects/Maelstrom/src/Maelstrom-%{version}.tar.gz
Source1:        maelstrom.png
Source2:        Maelstrom.desktop
Source3:        Maelstrom-Content-License.txt
Source4:        Maelstrom.appdata.xml
Patch:          setgid.patch
Patch:          gcc34.patch
Patch:          64bit.patch
Patch:          install.patch
Patch:          gcc5.patch
Patch:          netd-c99.patch
Patch:          Makefile.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  SDL2_net-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
Maelstrom is a space combat game, originally ported from the Macintosh 
platform. Brave pilots get to dodge asteroids and fight off other ships 
at the same time.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
cp %{SOURCE3} .

%build

export CXXFLAGS="$RPM_OPT_FLAGS -Wno-write-strings"
%configure
make %{?_smp_mflags}
%install
%make_install
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE2}
rm -f %{buildroot}%{_bindir}/{Maelstrom-netd,macres,playwave,snd2wav}
mkdir -p -m 755 %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
mkdir -p -m 755 %{buildroot}%{_datadir}/appdata
install -m 644 %{SOURCE4} %{buildroot}%{_datadir}/appdata
find %{buildroot} -name "Makefile*" -exec rm -f {} \;
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
