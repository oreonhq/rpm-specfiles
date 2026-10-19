%global source0_hash 21f771efc756fcb183a2fc6dcbbf3c55220290c62a77522113e68c7883663fa0
%global _docdir_fmt %{name}
Epoch:         1
Summary:        Python bindings for Caja
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/%{shortver}/%{name}-%{version}.tar.xz
Patch1:        python-caja-1.26-python313.patch
# oreon:deps
BuildRequires:  caja-devel
BuildRequires:  make
BuildRequires:  mate-common
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3-devel
# /oreon:deps
%description
Python bindings for Caja

%package -n python3-caja
Summary:        %summary
%{?python_provide:%python_provide python3-caja}
%description -n python3-caja
Python bindings for Caja

%package devel
Summary:        Python bindings for Caja
Requires:       python3-caja%{?_isa} = %{epoch}:%{version}-%{release}
%description devel
Python bindings for Caja

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export PYTHON=python3
%configure \
     --disable-static
make %{?_smp_mflags}
%install
%{make_install}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/caja-python/extensions
find $RPM_BUILD_ROOT -name '*.la' -delete
rm $RPM_BUILD_ROOT%{_docdir}/python-caja/README
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles python3-caja usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n python3-caja -f %{oreon_filedir}/python3-caja.list
%files -n python-caja-devel -f %{oreon_filedir}/python-caja-devel.list

%changelog

%autochangelog
