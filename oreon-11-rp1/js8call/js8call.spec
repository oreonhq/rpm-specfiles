%global source0_hash 9c4d65d6699e56d732bec2d250a34be3507b9c915da002707d957bf1920ebb48

%define _lto_cflags %{nil}

# Commit hash for tagged release
# https://bitbucket.org/widefido/js8call/downloads/?tab=tags
%global commit c5236ed22f06
%global project widefido

Name:           js8call
Version:        2.3.1
Release:        2%{?dist}
Summary:        Amateur Radio message passing using FT8 modulation

License:        GPL-3.0-or-later
URL:            http://js8call.com/

# Source archive from bitbucket includes project name and commit for directory.
# Use repack.sh to repack the archive.
Source0:        https://github.com/js8call/js8call/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        com.js8call.JS8Call.metainfo.xml

# js8call assumes it's using bundled hamlib and copies and installs binaries to
# new names.
Patch0:         js8call-hamlib.patch

ExcludeArch:    i686

BuildRequires:  cmake%{?rhel:3} gcc gcc-c++ gcc-gfortran tar
BuildRequires:  asciidoc dos2unix rubygem-asciidoctor
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
# Libraries and devel packages
BuildRequires:  hamlib hamlib-devel
BuildRequires:  boost-devel 
BuildRequires:  fftw-devel
BuildRequires:  pkgconfig(hamlib)
BuildRequires:  libusbx-devel
BuildRequires:  portaudio-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtserialport-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  systemd-devel

%description
JS8Call is software using the JS8 Digital Mode providing weak signal keyboard
to keyboard messaging to Amateur Radio Operators.

JS8Call is an experiment to test the feasibility of a digital mode with the
robustness of FT8, combined with a messaging and network protocol layer for
weak signal communication on HF, using a keyboard messaging style interface. It
is not designed for any specific purpose other than connecting amateur radio
operators who are operating under weak signal conditions. JS8Call is heavily
inspired by WSJT-X, Fldigi, and FSQCall and would not exist without the hard
work and dedication of the many developers in the amateur radio community.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# convert CR + LF to LF
dos2unix *.ui *.rc *.txt

# Don't specify gnu++11 when 14 is the compiler default.
%if 0%{?fedora}
sed -i 's/--std=gnu++11 //' CMakeLists.txt
%endif

%build
# Workaround for CMake 4
# https://bugzilla.redhat.com/show_bug.cgi?id=2380665
export CMAKE_POLICY_VERSION_MINIMUM=3.5

# Workaround for hamlib check, i.e. for hamlib_LIBRARY_DIRS not to be empty
export PKG_CONFIG_ALLOW_SYSTEM_LIBS=1

%cmake3 -DBoost_NO_SYSTEM_PATHS=FALSE \
        -Dhamlib_STATIC=FALSE

%cmake_build

%install
%cmake_install

# Install icon to proper place and use it in desktop file
install -D -p -m644 icons/Unix/js8call_icon.png \
    %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
desktop-file-edit --set-key=Icon --set-value="%{name}" \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop

# Install AppStream metainfo file
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE1} %{buildroot}%{_metainfodir}/

appstream-util validate-relax \
  --nonet %{buildroot}%{_metainfodir}/com.js8call.JS8Call.metainfo.xml

# Buttons don't look right with system default style.
desktop-file-edit --set-key=Exec --set-value="js8call --style=fusion" \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# Remove COPYING so it can be included with %%liecnse
rm -f %{buildroot}%{_datadir}/doc/JS8Call/COPYING
# Remove unneeded install file
rm -f %{buildroot}%{_datadir}/doc/JS8Call/INSTALL*

%files
%license COPYING
%doc %{_datadir}/doc/JS8Call
%{_bindir}/js8*
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/com.js8call.JS8Call.metainfo.xml
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/pixmaps/%{name}_icon.png
%{_datadir}/%{name}/

%changelog
%autochangelog
