%global source0_hash none

#global rctag rc8

# for fortran nested functions that (still in 2026) in gfortran implementation uses
# trampolines that require executable stack
%undefine _hardened_linker_errors

Name:		wsjtx
Version:	3.0.0~rc1
Release:	3%{?dist}
Summary:	Weak Signal communication by K1JT

License:	GPL-3.0-or-later

URL:		https://sourceforge.net/projects/wsjt/
Source0:	https://sourceforge.net/projects/wsjt/files/%{name}-%{version}%{?rctag:-%{rctag}}/%{name}-%{version}%{?rctag:-%{rctag}}.tgz
Source100:	edu.princeton.physics.WSJTX.metainfo.xml

ExcludeArch:    i686

BuildRequires:	cmake
BuildRequires:	dos2unix
BuildRequires:	tar
BuildRequires:	gcc-c++
BuildRequires:	gcc-gfortran

BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-linguist
BuildRequires:	qt5-qtserialport-devel
BuildRequires:	qt5-qtmultimedia-devel
BuildRequires:	qt5-qtwebsockets-devel
BuildRequires:	desktop-file-utils
BuildRequires:	hamlib-devel
BuildRequires:	fftw-devel
BuildRequires:	libusbx-devel
BuildRequires:	systemd-devel
%if 0%{?rhel} && 0%{?rhel} < 9
BuildRequires:	boost169-devel
%else
BuildRequires:	boost-devel
%endif
BuildRequires:	portaudio-devel
%if 0%{?fedora}
BuildRequires:	asciidoc
BuildRequires:	rubygem-asciidoctor
BuildRequires:	libappstream-glib
%endif
# Sent upstream
# https://www.mail-archive.com/wsjt-devel@lists.sourceforge.net/msg28480.html
Patch0:		wsjtx-3.0.0-rename-split.patch
# Temporal fix, problem reported upstream
# https://www.mail-archive.com/wsjt-devel@lists.sourceforge.net/msg28480.html
Patch1:		wsjtx-3.0.0-path-fix.patch

%description
WSJT-X is a computer program designed to facilitate basic amateur radio
communication using very weak signals. It implements communication protocols
or "modes" called JT4, JT9, JT65, QRA64, ISCAT, MSK144, and WSPR, as well as
one called Echo for detecting and measuring your own radio signals reflected
from the Moon.

%prep
%setup -q -n %{name}-%{version}

# Remove bundled hamlib
rm -f src/hamlib*.tgz* src/hamlib*.tar.gz*

# Extract wsjtx source and clean up
tar -xzf src/%{name}.tgz
rm -f src/wsjtx.tgz*
find ./ -type f -exec chmod -x {} \;

cd %{name}

%if ! 0%{?rhel} < 8
# remove bundled boost. EL 7 is not required version.
rm -rf boost
%endif

# convert CR + LF to LF
dos2unix *.ui *.iss *.txt
find ./ -type f -name '*.cpp' -exec dos2unix {} \;

%patch -P0 -p1 -b .external-split
%patch -P1 -p1 -b .path-fix

%build
# The fortran code in this package is not type safe and will thus not work
# with LTO.  Additionally there are numerous bogus strncat calls that also
# need to be fixed for this package to work with LTO
%define _lto_cflags %{nil}

# -fcommon is a workaround for build with gcc-10, reported upstream
export CFLAGS="%{build_cflags} -fcommon -Wno-error=maybe-uninitialized"
# reported upstream
export CXXFLAGS="%{build_cxxflags} -Wno-error=maybe-uninitialized"
export LDFLAGS="%{build_ldflags}"
# workaround for hamlib check, i.e. for hamlib_LIBRARY_DIRS not to be empty
export PKG_CONFIG_ALLOW_SYSTEM_LIBS=1

cd %{name}
%cmake -Dhamlib_STATIC=FALSE \
       -DBoost_NO_SYSTEM_PATHS=FALSE \
%if 0%{?rhel}
       -DBOOST_INCLUDEDIR=%{_includedir}/boost169 \
       -DBOOST_LIBRARYDIR=%{_libdir}/boost169 \
       -DWSJT_GENERATE_DOCS=FALSE \
       -DWSJT_SKIP_MANPAGES=TRUE
%endif

%cmake_build

%install
cd %{name}
%cmake_install

dos2unix %{buildroot}%{_datadir}/applications/message_aggregator.desktop

# Make sure the right style is used.
desktop-file-edit --set-key=Exec --set-value="wsjtx --style=fusion" \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop
# desktop files
desktop-file-validate %{buildroot}%{_datadir}/applications/wsjtx.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/message_aggregator.desktop

%if 0%{?fedora}
# metainfo file
mkdir -p %{buildroot}%{_metainfodir}
install -pm 0644 %{SOURCE100} %{buildroot}%{_metainfodir}/
%endif

# fix docs
install -p -m 0644 -t %{buildroot}%{_datadir}/doc/%{name} GUIcontrols.txt jt9.txt \
  v1.7_Features.txt wsjtx_changelog.txt

# drop wsjtx hamlib bins
rm -f %{buildroot}%{_bindir}/rigctl*-wsjtx

%if 0%{?fedora}
%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%endif

%files
%license COPYING
%doc %{_datadir}/doc/%{name}
%{_bindir}/cablog
%{_bindir}/echosim
%{_bindir}/fcal
%{_bindir}/fmeasure
%{_bindir}/fmtave
%{_bindir}/fst4sim
%{_bindir}/hash22calc
%{_bindir}/jt4code
%{_bindir}/jt65code
%{_bindir}/jt9
%{_bindir}/jt9code
%{_bindir}/ft8code
%{_bindir}/message_aggregator
%{_bindir}/msk144code
%{_bindir}/q65sim
%{_bindir}/q65code
%{_bindir}/udp_daemon
%{_bindir}/wsjtx
%{_bindir}/wsjtx_app_version
%{_bindir}/wsprd
%{_bindir}/EchoCallSim
%{_bindir}/ft8sim
%{_bindir}/testEchoCall
%{?fedora:%{_mandir}/man1/*.1.gz}
%{?fedora:%{_metainfodir}/*.xml}
%{_datadir}/applications/wsjtx.desktop
%{_datadir}/applications/message_aggregator.desktop
%{_datadir}/pixmaps/wsjtx_icon.png
%{_datadir}/%{name}

%changelog
%autochangelog
