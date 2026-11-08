# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 931b44eabdd5f7d170803f3476397c8e9dea07209589e1194ff8379429991ccb

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
  %global meson_python_flags -Dwith_py2=false -Dwith_py3=true
  %global build_python2 0
  %global build_python3 1

  %global meson_accept_overflowed_buildorder_flag -Daccept_overflowed_buildorder=true

%global upstream_name libmodulemd


Name:           %{upstream_name}%{?v2_suffix}
Version:        2.15.3
Release:        1%{?dist}
Summary:        Module metadata manipulation library

# COPYING:      MIT
## not in any binary package
# contrib/coverity-modeling.c:  GPL-2.0-or-later
# contrib/release-tools/semver: GPL-3.0-only
# modulemd/tests/test_data/f29.yaml:            Apache-2.0
# modulemd/tests/test_data/f29-updates.yaml:    Apache-2.0
# xml_specs/reduced/tests/good/module_stream_build_license.xml: MIT AND GPL-3.0-or-later
License:        MIT
SourceLicense:  %{license} AND GPL-3.0-only AND GPL-3.0-or-later AND GPL-2.0-or-later AND Apache-2.0
URL:            https://github.com/oreon-modularity/libmodulemd
Source0:        https://github.com/fedora-modularity/libmodulemd/releases/download/%{version}/modulemd-%{version}.tar.xz
Source1:        modulemd-2.15.3.tar.xz.asc
# Key exported from Petr Pisar's keyring
Source2:        gpgkey-E3F42FCE156830A80358E6E94FD1AEC3365AF7BF.gpg

BuildRequires:  gnupg2
BuildRequires:  meson >= 0.47
BuildRequires:  pkgconfig
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  glib2-doc
BuildRequires:  rpm-devel
%if %{build_python2}
BuildRequires:  python2-devel
BuildRequires:  python-gobject-base
%endif
%if %{build_python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-gobject-base
BuildRequires:  oreon-rpm-macros
%endif


%description
C library for manipulating module metadata files.
See https://github.com/oreon-modularity/libmodulemd/blob/main/README.md for
more details.


%if %{build_python2}
%package -n python2-%{name}
Summary:        Python 2 bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python-gobject-base

%description -n python2-%{name}
Python 2 bindings for %{name}.
%endif


%if %{build_python3}
%package -n python%{python3_pkgversion}-%{name}
Summary:        Python 3 bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python%{python3_pkgversion}-gobject-base

%description -n python%{python3_pkgversion}-%{name}
Python %{python3_pkgversion} bindings for %{name}.
%endif


%package devel
Summary:        Development files for libmodulemd
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel
Development files for %{name}.


%prep
%oreon_sha256

%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1 -n modulemd-%{version}


%build
%meson \
    %{meson_accept_overflowed_buildorder_flag} \
    -Drpmio=enabled \
    -Dskip_introspection=false \
    -Dtest_installed_lib=false \
    -Dwith_docs=true \
    -Dwith_manpages=enabled \
    %{meson_python_flags}
%meson_build


%check
export LC_CTYPE=C.utf8
# The tests sometimes time out in CI, so give them a little extra time
%{__meson} test -C %{_vpath_builddir} %{?_smp_mesonflags} --print-errorlogs -t 5


%install
%meson_install



%ldconfig_scriptlets


%files
%license COPYING
%doc NEWS README.md
%{_bindir}/modulemd-validator%{?v2_suffix}
%{_mandir}/man1/modulemd-validator%{?v2_suffix}.1*
%{_libdir}/%{upstream_name}.so.2*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Modulemd-2.0.typelib


%files devel
%{_libdir}/%{upstream_name}.so
%{_libdir}/pkgconfig/modulemd-2.0.pc
%{_includedir}/modulemd-2.0/
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Modulemd-2.0.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/modulemd-2.0/


%if %{build_python2}
%files -n python2-%{name}
%{python2_sitearch}/gi/overrides/
%endif


%if %{build_python3}
%files -n python%{python3_pkgversion}-%{name}
%{python3_sitearch}/gi/overrides/
%endif


