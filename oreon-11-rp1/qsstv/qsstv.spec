%global source0_hash c03f7fa5c680ced8fd331c25ff3e47440c9aedb48ec7b66255c6aa0ed88e7a68

Name:           qsstv
Version:        9.5.8
Release:        25%{?dist}
Summary:        Qt-based slow-scan TV and fax

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.qsl.net/on4qz/

Source0:        https://www.qsl.net/o/on4qz/qsstv/downloads/%{name}_%{version}.tar.gz
Source1:        qsstv.1
Source2:        net.qsl.QSSTV.metainfo.xml
Source3:        qsstv.png

Patch0:         qsstv-install.patch

ExcludeArch:    i686

BuildRequires:  gcc-c++ doxygen desktop-file-utils
BuildRequires:  make
BuildRequires:  libappstream-glib
BuildRequires:  fftw-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qwt-qt5-devel
BuildRequires:  hamlib-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  libv4l-devel

%description
Qsstv is a program for receiving slow-scan television and fax. These are
modes used by hamradio operators. Qsstv uses a soundcard to send and
receive images.

%package doc
Summary:             User manual for Qsstv.
BuildArch:           noarch
Requires:            %{name} = %{version}-%{release}

%description doc
User manual for Qsstv.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}

# Honor build flags...
sed -i "s/\-O0/\-O2/g" qsstv.pro

%build 
# mode_and_occupancy_code_table has different sizes  in its declaration
# vs its definition.  This is a hard error when using LTO and must be
# resolved before this package can use LTO
%define _lto_cflags %{nil}

qmake-qt5 PREFIX=%{_prefix} CONFIG+=debug QMAKE_CXXFLAGS+="-std=c++14 %{optflags}"
make %{?_smp_mflags}

%install
export INSTALL_ROOT=%{buildroot}
make install 

# Install icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
install -pm 0644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# Install man page borrowed from Debian
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/

# Install metainfo file
%if 0%{?fedora}
mkdir -p %{buildroot}%{_metainfodir}
install -pm 0644 %{SOURCE2} %{buildroot}%{_metainfodir}/
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%endif

find %{buildroot} -type f -name "*.a" -exec rm -f {} \;

%files
%license COPYING
%doc README.txt
%{_bindir}/* 
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/applications/*%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{?fedora:%{_metainfodir}/*.metainfo.xml}

%files doc
%{_pkgdocdir}/

%changelog
%autochangelog
