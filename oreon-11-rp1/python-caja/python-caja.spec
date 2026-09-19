%global source0_hash 21f771efc756fcb183a2fc6dcbbf3c55220290c62a77522113e68c7883663fa0

# Without this, some documentation files end up in /usr/share/doc/python3-caja.
# They should all go in /usr/share/doc/python-caja.
%global _docdir_fmt %{name}

%global _description\
Python bindings for Caja

%define shortver        %(cut -d. -f1,2 <<< '%{version}')

Name:          python-caja
Version:       1.26.0
Release:       17%{?dist}
Epoch:         1
Summary:       Python bindings for Caja

# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/%{shortver}/%{name}-%{version}.tar.xz
Patch1:        python-caja-1.26-python313.patch

BuildRequires: python3-devel
BuildRequires: caja-devel
BuildRequires: pkgconfig(pygobject-3.0)
BuildRequires: make
BuildRequires: mate-common

%description
%_description

%package -n python3-caja
Summary:        %summary
%{?python_provide:%python_provide python3-caja}

%description -n python3-caja
%_description

%package devel
Summary:        Python bindings for Caja
Requires:       python3-caja%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
%_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
export PYTHON=python3

%configure \
     --disable-static

make %{?_smp_mflags}

%install
%{make_install}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/caja-python/extensions
find $RPM_BUILD_ROOT -name '*.la' -delete

# We use %%doc instead
rm $RPM_BUILD_ROOT%{_docdir}/python-caja/README

%find_lang %{name} --with-gnome --all-name

%files -n python3-caja -f %{name}.lang
%license COPYING
%doc README AUTHORS NEWS
%{_libdir}/caja/extensions-2.0/libcaja-python.so
%{_datadir}/caja/extensions/libcaja-python.caja-extension
%dir %{_datadir}/caja-python
%dir %{_datadir}/caja-python/extensions
%{_docdir}/python-caja/examples/

%files devel
%{_libdir}/pkgconfig/caja-python.pc

%changelog
%autochangelog
