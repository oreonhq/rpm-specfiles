%if  0%{?rhel} && 0%{?rhel} <= 7
  # There is no python3-gobject-base in RHEL 7. But it exists in EPEL 7.
  %global meson_python_flags -Dwith_py2=true -Dwith_py3=true
  %global build_python2 1
  %global build_python3 1
%else
  %global meson_python_flags -Dwith_py2=false -Dwith_py3=true
  %global build_python2 0
  %global build_python3 1
%endif

%if (0%{?fedora} && 0%{?fedora} <= 50) || (0%{?rhel} && 0%{?rhel} <= 10)
  # Support RHEL 8 module builds with an invalid buildorder.
  %global meson_accept_overflowed_buildorder_flag -Daccept_overflowed_buildorder=true
%else
  %global meson_accept_overflowed_buildorder_flag -Daccept_overflowed_buildorder=false
%endif

%global upstream_name libmodulemd

%if (0%{?rhel} && 0%{?rhel} <= 7)
  %global v2_suffix 2
%endif

Name:           %{upstream_name}%{?v2_suffix}
Version:        2.15.2
Release:        7%{?dist}
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
URL:            https://github.com/fedora-modularity/libmodulemd
Source0:        https://github.com/fedora-modularity/libmodulemd/releases/download/2.15.2/modulemd-2.15.2.tar.xz
Source1:        https://github.com/fedora-modularity/libmodulemd/releases/download/2.15.2/modulemd-2.15.2.tar.xz.asc
# Key exported from Petr Pisar's keyring
Source2:        gpgkey-E3F42FCE156830A80358E6E94FD1AEC3365AF7BF.gpg
# Adapt tests to glib2-2.87.0, in upstream after 2.15.2, bug #2423153
Patch0:         modulemd-2.15.2-tests-Adapt-to-glib-2.87.0.patch
# Adapt tests to pygobject 3.55.0, in upstream after 2.15.2, bug #2440570
Patch1:         modulemd-2.15.2-tests-Adapt-to-pygobject-3.55.0.patch
# oreon url source checksums begin
%global source0_sha256 6fb926e270ba44d1981d1abadaa6728c5e357636eee3b3bb533e95b92d104970
%global source0_file modulemd-2.15.2.tar.xz
# oreon url source checksums end

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
%endif
%if 0%{?fedora} >= 40 && 0%{?fedora} < 42
# glib2 version with g_once_init_enter_pointer symbol, bug #2265336
Requires:       glib2 >= 2.79.0-2
%endif
Requires:       libyaml%{?_isa}


%description
C library for manipulating module metadata files.
See https://github.com/fedora-modularity/libmodulemd/blob/main/README.md for
more details.


%if %{build_python2}
%package -n python2-%{name}
Summary:        Python 2 bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python-gobject-base
Requires:       python-six

%description -n python2-%{name}
Python 2 bindings for %{name}.
%endif


%if %{build_python3}
%package -n python%{python3_pkgversion}-%{name}
Summary:        Python 3 bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python%{python3_pkgversion}-gobject-base
%if (0%{?rhel} && 0%{?rhel} <= 7)
# The py3_dist macro on EPEL 7 doesn't work right at the moment
Requires:       python3.6dist(six)
%else
Requires:       %{py3_dist six}
%endif

%description -n python%{python3_pkgversion}-%{name}
Python %{python3_pkgversion} bindings for %{name}.
%endif


%package devel
Summary:        Development files for libmodulemd
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if (0%{?rhel} && 0%{?rhel} <= 7)
Conflicts:      libmodulemd1-devel
Conflicts:      libmodulemd-devel
%endif


%description devel
Development files for %{name}.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/modulemd-2.15.2.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "6fb926e270ba44d1981d1abadaa6728c5e357636eee3b3bb533e95b92d104970" || { echo "oreon: Source0 SHA256 mismatch for modulemd-2.15.2.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
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

%if ( 0%{?rhel} && 0%{?rhel} <= 7)
# Don't conflict with modulemd-validator from 1.x included in the official
# RHEL 7 repos
mv %{buildroot}%{_bindir}/modulemd-validator \
   %{buildroot}%{_bindir}/modulemd-validator%{?v2_suffix}

mv %{buildroot}%{_mandir}/man1/modulemd-validator.1 \
   %{buildroot}%{_mandir}/man1/modulemd-validator%{?v2_suffix}.1
%endif


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


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.15.2-7
- Prepare for Oreon 11 (RP1)
