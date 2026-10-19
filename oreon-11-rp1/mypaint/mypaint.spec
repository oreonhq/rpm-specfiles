%global source0_hash f3e437d7cdd5fd28ef6532e8ab6b4b05d842bcdd644f16a0162dad3d8e57bb16
Name:           mypaint
Version:        2.0.1
Release:        1%{?dist}
Summary:        A fast and easy graphics application for digital painters
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-CC-BY
URL:            http://mypaint.org
Source0:        https://github.com/mypaint/mypaint/releases/download/v%{version}/%{name}-%{version}.tar.xz
Patch0:         0001-setuptools-fixes.patch
Patch1:         0002-python311.patch
Patch2:         0003-fix-deprecations.patch
Patch3:         0004-pygobject352.patch
Patch4:         0005-numpy23.patch
Requires:       python3
Requires:       python3-numpy%{?_isa}
Requires:       python3-protobuf
Requires:       python3-gobject%{?_isa}
Requires:       %{name}2-brushes
Requires:       %{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libmypaint)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(mypaint-brushes-2.0)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-scons
BuildRequires:  python3-setuptools
BuildRequires:  swig
# /oreon:deps
%description
MyPaint is a fast and easy graphics application for digital painters. It lets
you focus on the art instead of the program. You work on your canvas with
minimum distractions, bringing up the interface only when you need it.

%package        data
Summary:        Common data files for for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description    data
The %{name}-data package contains common data files for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# for 64 bit
sed -i 's|lib/mypaint|%{_lib}/mypaint|g' mypaint.py
sed -i "s|'lib', 'mypaint'|'%{_lib}', 'mypaint'|" mypaint.py

%build

%{__python3} setup.py build_ext
%{__python3} setup.py build_py
%{__python3} setup.py build_translations
%{__python3} setup.py build_config
%install
%{__python3} setup.py managed_install --prefix=%{buildroot}%{_prefix}
[[ %{_lib} != lib ]] && mv %{buildroot}%{_prefix}/lib %{buildroot}%{_prefix}/%{_lib}
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
   %{buildroot}%{_datadir}/applications/%{name}.desktop
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mypaint-data -f %{oreon_filedir}/mypaint-data.list
%files -n mypaint-devel -f %{oreon_filedir}/mypaint-devel.list

%changelog

%autochangelog
