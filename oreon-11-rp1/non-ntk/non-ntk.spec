%global source0_hash 50b6d76d0ced00d96c6e7a805777960e4cc8ad450295e3dbdc88b036db48476e
%global commit dae177189b12f74ea01ac2389b76326c06d9be78
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20190925
%global patch 1
Name:           non-ntk
Version:        1.3.1000
Release:        1%{?dist}
Summary:        A fork of FLTK for the non audio suite
License:        LGPL-2.0-or-later WITH FLTK-exception AND GPL-2.0-or-later
URL:            http://non.tuxfamily.org/
Source0:        %{name}-%{commitdate}-git%{shortcommit}.%{patch}.tar.xz
Source1:        %{name}-snapshot.sh
Source2:        ntk-fluid.desktop
Source3:        ntk-fluid.appdata.xml
Source4:        ntk-chtheme.desktop
Patch0:         %{name}-fsf.patch
Patch1:         %{name}-scandir.patch
Patch2:         %{name}-flags.patch
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(xft)
BuildRequires:  python3
BuildRequires:  zlib-devel
# /oreon:deps
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
export DESTDIR="%{buildroot}"
python3 ./waf -v install --destdir=%{buildroot}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
 %{SOURCE2} %{SOURCE4}
install -d -m755 %{buildroot}%{_metainfodir}
install -p -m644 %{SOURCE3} %{buildroot}%{_metainfodir}
rm %{buildroot}%{_libdir}/libntk*.a*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/ntk-fluid.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/ntk-chtheme.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/ntk-fluid.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n non-ntk-devel -f %{oreon_filedir}/non-ntk-devel.list
%files -n non-ntk-fluid -f %{oreon_filedir}/non-ntk-fluid.list

%changelog

%autochangelog
