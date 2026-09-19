%global source0_hash 2add2083365eee2f966db826c3967f030d949b2b5aad59e738ba3b782587ad93

%global  basever 0.8.18

Name:           compizconfig-python
Version:        0.8.18
Release:        20%{?dist}
Epoch:          1
Summary:        Python bindings for the Compiz Configuration System
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://gitlab.com/compiz/%{name}
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  libcompizconfig-devel >= %{basever}
BuildRequires:  glib2-devel
BuildRequires:  python3-devel
BuildRequires:  python3-Cython
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires: make

Requires:       compiz >= %{basever}

%description
The Compiz Project brings 3D desktop visual effects that improve
usability of the X Window System and provide increased productivity
though plugins and themes contributed by the community giving a
rich desktop experience.

This package contains bindings to configure Compiz's
plugins and the composite window manager.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-v%{version}

%build
export PYTHON=python3

./autogen.sh
%configure --disable-static

make %{?_smp_mflags} V=1

%install
%{make_install}
find %{buildroot} -type f -name "*.a" -o -name "*.la" | xargs rm -f

%files
%doc COPYING NEWS
%{python3_sitearch}/compizconfig.so
%exclude %{_libdir}/pkgconfig/compizconfig-python.pc

%changelog
%autochangelog
