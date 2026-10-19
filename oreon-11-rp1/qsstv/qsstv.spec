%global source0_hash c03f7fa5c680ced8fd331c25ff3e47440c9aedb48ec7b66255c6aa0ed88e7a68
Name:           qsstv
Version:        9.5.8
Release:        1%{?dist}
Summary:        Qt-based slow-scan TV and fax
License:        GPL-2.0-or-later
URL:            https://www.qsl.net/on4qz/
Source0:        https://www.qsl.net/o/on4qz/qsstv/downloads/%{name}_%{version}.tar.gz
Source1:        qsstv.1
Source2:        net.qsl.QSSTV.metainfo.xml
Source3:        qsstv.png
Patch0:         qsstv-install.patch
ExcludeArch:    i686
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  fftw-devel
BuildRequires:  gcc-c++
BuildRequires:  hamlib-devel
BuildRequires:  libappstream-glib
BuildRequires:  libv4l-devel
BuildRequires:  make
BuildRequires:  openjpeg2-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qwt-qt5-devel
# /oreon:deps
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

%define _lto_cflags %{nil}
qmake-qt5 PREFIX=%{_prefix} CONFIG+=debug QMAKE_CXXFLAGS+="-std=c++14 %{optflags}"
make %{?_smp_mflags}
%install
export INSTALL_ROOT=%{buildroot}
make install 
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
install -pm 0644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/
find %{buildroot} -type f -name "*.a" -exec rm -f {} \;
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qsstv-doc -f %{oreon_filedir}/qsstv-doc.list

%changelog

%autochangelog
