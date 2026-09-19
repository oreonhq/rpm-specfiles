%global source0_hash 50b6d76d0ced00d96c6e7a805777960e4cc8ad450295e3dbdc88b036db48476e

%global commit dae177189b12f74ea01ac2389b76326c06d9be78
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20190925
%global patch 1

Name:           non-ntk
Version:        1.3.1000
Release:        0.17.%{commitdate}git%{shortcommit}%{?dist}
Summary:        A fork of FLTK for the non audio suite

# themes are GPLv2+, FLTK derived code is LGPLv2+
License:        LGPL-2.0-or-later WITH FLTK-exception AND GPL-2.0-or-later
URL:            http://non.tuxfamily.org/
Source0:        %{name}-%{commitdate}-git%{shortcommit}.%{patch}.tar.xz
# script to create source tarball from git
# sh non-snapshot.sh $(rev)
Source1:        %{name}-snapshot.sh
# No desktop file in tarball
Source2:        ntk-fluid.desktop
# Appdata for ntk-fluid
Source3:        ntk-fluid.appdata.xml
# Desktop file for ntk-chtheme
Source4:        ntk-chtheme.desktop
# Fix wrong FSF address
Patch0:         %{name}-fsf.patch
# Use system provided scandir
Patch1:         %{name}-scandir.patch
# Delete wrong compiler flags
Patch2:         %{name}-flags.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cairo-devel >= 1.10.0
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig(libpng)
BuildRequires:  python3
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(xft)

%description
%{name} is a fork of the FLTK UI toolkit. It employs cairo support and
other additions not accepted upstream. It is currently used by the non-*
audio suite of programs.

%package devel
Summary:        Development files for the non-ntk GUI library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for the Non-ntk GUI library

%package fluid
Summary: Fast Light User Interface Designer
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description fluid
%{summary}, an interactive GUI designer for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n non-ntk-%{commitdate}

%build
%set_build_flags
python3 ./waf -v configure --prefix=%{_prefix} \
  --libdir=%{_libdir} --enable-gl
python3 ./waf -v %{?_smp_mflags}

%install
# Do not run ldconfig
export DESTDIR="%{buildroot}"

python3 ./waf -v install --destdir=%{buildroot}

# Install desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
 %{SOURCE2} %{SOURCE4}

# Install appdata file
install -d -m755 %{buildroot}%{_metainfodir}
install -p -m644 %{SOURCE3} %{buildroot}%{_metainfodir}

# Delete static libraries
rm %{buildroot}%{_libdir}/libntk*.a*

%check
# Validate desktop files
desktop-file-validate %{buildroot}%{_datadir}/applications/ntk-fluid.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/ntk-chtheme.desktop

# Validate appdata
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/ntk-fluid.appdata.xml

%files
%doc README
%license COPYING
%{_libdir}/libntk*.so.1*

%files devel
%{_libdir}/libntk.so
%{_libdir}/libntk_images.so
%{_libdir}/libntk_gl.so
%{_includedir}/ntk
%{_libdir}/pkgconfig/*

%files fluid
%{_datadir}/applications/ntk-fluid.desktop
%{_datadir}/applications/ntk-chtheme.desktop
%{_metainfodir}/ntk-fluid.appdata.xml
%{_bindir}/ntk-*

%changelog
%autochangelog
