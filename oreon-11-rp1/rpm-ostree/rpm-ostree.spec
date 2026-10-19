%global source0_hash a9b4fb9809e688d5345b901d557304d4c059ad8c93bf24dd374a803d620f126e
Summary:        Hybrid image/package system
Name: rpm-ostree
Version: 2026.3
Release:        1%{?dist}
License: LGPL-2.0-or-later
URL: https://github.com/coreos/rpm-ostree
Source0:        https://github.com/coreos/rpm-ostree/releases/download/v%{version}/rpm-ostree-%{version}.tar.xz
%if 0%{?fedora} || 0%{?rhel} >= 10 || (0%{?oreon} >= 11)
ExcludeArch:    %{ix86}
%endif
%if 0%{?rhel} || (0%{?oreon} >= 11)
%else
%endif
%bcond_with sanitizers
%bcond_with bin_unit_tests
%if 0%{?rhel} >= 10 || 0%{?fedora} > 41 || (0%{?oreon} >= 11)
    %bcond_with ostree_ext
%else
    %bcond_without ostree_ext
%endif
%if 0%{?rhel} && ! 0%{?centos} || (0%{?oreon} >= 11)
%bcond_without rhsm
%else
%bcond_with rhsm
%endif
%if 0%{?rhel} || (0%{?oreon} >= 11)
%bcond_with zchunk
%else
%bcond_without zchunk
%endif
%global libsolv_version 0.7.21
%global libmodulemd_version 2.13.0
%global librepo_version 1.18.0
%if %{with rhsm}
%endif
%if %{with zchunk}
%endif
Requires:       libmodulemd%{?_isa} >= %{libmodulemd_version}
Requires:       libsolv%{?_isa} >= %{libsolv_version}
Requires:       librepo%{?_isa} >= %{librepo_version}
%if 0%{?fedora} >= 43 || 0%{?rhel} >= 11 || (0%{?oreon} >= 11)
Requires:       rpm-libs%{?_isa} >= 5.99.90
%endif
Requires: ostree
Requires: bubblewrap
%if %{defined rhel} && 0%{?rhel} < 10 || (0%{?oreon} >= 11)
Requires: fuse
%else
Requires: fuse3
%endif
Requires: skopeo
Requires: bootc
%if %{without ostree_ext}
Requires: ostree-cli(ostree-container)
%endif
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  /usr/bin/g-ir-scanner
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  gtk-doc
BuildRequires:  jq
BuildRequires:  libattr-devel
BuildRequires:  libcap-devel
BuildRequires:  libsolv-devel
BuildRequires:  libtool
BuildRequires:  libzstd-devel
BuildRequires:  make
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(librepo)
BuildRequires:  pkgconfig(libsolv)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(modulemd-2.0)
BuildRequires:  pkgconfig(ostree-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(rpm)
BuildRequires:  pkgconfig(smartcols)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zck)
BuildRequires:  python3-devel
BuildRequires:  rpm-devel
BuildRequires:  rust
BuildRequires:  rustc
# /oreon:deps
%description
rpm-ostree is a hybrid image/package system.  It supports
"composing" packages on a build server into an OSTree repository,
which can then be replicated by client systems with atomic upgrades.
Additionally, unlike many "pure" image systems, with rpm-ostree
each client system can layer on additional packages, providing
a "best of both worlds" approach.

%package libs
Summary: Shared library for rpm-ostree
%description libs
The %{name}-libs package includes the shared library for %{name}.

%package devel
Summary: Development headers for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package includes the header files for %{name}-libs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git -n %{name}-%{version} -p1
%if 0%{?__isa_bits} == 32
sed -ie 's,^lto = true,lto = false,' Cargo.toml
%endif
%oreon_vendor_cargo
%build

env NOCONFIGURE=1 ./autogen.sh
%if 0%{?build_rustflags:1}
export RUSTFLAGS="%{build_rustflags}"
%endif
%configure --disable-silent-rules --enable-gtk-doc %{?rpmdb_default} %{?with_sanitizers:--enable-sanitizers}  %{?with_bin_unit_tests:--enable-bin-unit-tests} \
  %{?with_rhsm:--enable-featuresrs=rhsm}
%make_build
%if 0%{?fedora} || 0%{?rhel} >= 10 || (0%{?oreon} >= 11)
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%cargo_vendor_manifest
sed -i -e '/https:\/\//d' cargo-vendor.txt
%endif
%install
%make_install INSTALL="install -p -c"
%if %{without ostree_ext}
rm -vrf $RPM_BUILD_ROOT/usr/libexec/libostree/ext
%endif
find $RPM_BUILD_ROOT -name '*.la' -delete
cat > autofiles.py <<EOF
import os,sys,glob
os.chdir(os.environ['RPM_BUILD_ROOT'])
for line in sys.argv[1:]:
    if line == '':
        break
    if line[0] != '/':
        sys.stdout.write(line + '\n')
    else:
        files = glob.glob(line[1:])
        if len(files) > 0:
            sys.stderr.write('{0} matched {1} files\n'.format(line, len(files)))
            sys.stdout.write(line + '\n')
        else:
            sys.stderr.write('{0} did not match any files\n'.format(line))
EOF
PYTHON='%{python3}'
if ! test -x '%{python3}'; then
    PYTHON=python2
fi
$PYTHON autofiles.py > files \
  '%{_bindir}/*' \
  '%{_libdir}/%{name}' \
  '%{_mandir}/man*/*' \
  '%{_datadir}/dbus-1/system.d/*' \
  '%config(noreplace) %{_sysconfdir}/rpm-ostreed.conf' \
  '%{_prefix}/lib/systemd/system/*' \
  '%{_prefix}/lib/kernel/install.d/*' \
  '%{_libexecdir}/rpm-ostree*' \
%if %{with ostree_ext}
  '%{_libexecdir}/libostree/ext/*' \
%endif
  '%{_datadir}/polkit-1/actions/*.policy' \
  '%{_datadir}/dbus-1/system-services/*' \
  '%{_datadir}/bash-completion/completions/*'
$PYTHON autofiles.py > files.lib \
  '%{_libdir}/*.so.*' \
  '%{_libdir}/girepository-1.0/*.typelib'
$PYTHON autofiles.py > files.devel \
  '%{_libdir}/lib*.so' \
  '%{_includedir}/*' \
  '%{_datadir}/dbus-1/interfaces/org.projectatomic.rpmostree1.xml' \
  '%{_libdir}/pkgconfig/*' \
  '%{_datadir}/gtk-doc/html/*' \
  '%{_datadir}/gir-1.0/*-1.0.gir'
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%systemd_post rpm-ostree-countme.timer
if [ -e /run/ostree-booted ]; then
    ln -snf /usr/lib/systemd/system/rpm-ostree-fix-shadow-mode.service  /usr/lib/systemd/system/multi-user.target.wants/
fi
%preun

%systemd_preun rpm-ostree-countme.timer
%postun

%systemd_postun_with_restart rpm-ostree-countme.timer
%files -f %{oreon_filedir}/main.list
%files -n rpm-ostree-libs -f %{oreon_filedir}/rpm-ostree-libs.list
%files -n rpm-ostree-devel -f %{oreon_filedir}/rpm-ostree-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2026.1-1
- Import
