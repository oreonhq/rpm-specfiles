%global source0_hash 6e4ecfc18b91586cc0c58e376a7e23a561cbd7e8756586e62d5d9450e1b42b25
%global libpkg libconcord
Name: concordance
Version: 1.5
Release:        1%{?dist}
Summary:        Software to program the Logitech Harmony remote control
License: GPL-3.0-or-later
URL: http://www.phildev.net/concordance/
Source0:        https://github.com/jaymzh/concordance/releases/download/v%{version}/%{name}-%{version}.tar.bz2
Requires: %{libpkg} = %{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-concordance = %{version}-%{release}
# /oreon:deps
%description
This software will allow you to program your Logitech Harmony universal
remote control.

%package -n %{libpkg}
Summary: Library to talk to Logitech Harmony universal remote controls
Requires: udev
Requires: dnsmasq
%description -n %{libpkg}
Library to talk to Logitech Harmony universal remote controls

%package -n %{libpkg}-devel
Summary: Development libraries for libconcord
Requires: %{libpkg} = %{version}-%{release}
%description -n %{libpkg}-devel
Development libraries for libconcord

%package -n python3-%{libpkg}
Summary: Python 3 bindings for libconcord
Requires: %{libpkg} = %{version}-%{release}
BuildArch: noarch
%description -n python3-%{libpkg}
Python 3 bindings for libconcord

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

cd %{libpkg}
%configure --disable-static --disable-mime-update
make %{_smp_mflags}
cd -
cd %{libpkg}/bindings/python
%pyproject_wheel
cd -
cd %{name}
export CFLAGS="%{optflags} -I../libconcord"
export LDFLAGS="%{__global_ldflags} -L../libconcord/.libs"
%configure --enable-shared
make %{_smp_mflags}
%install
cd %{libpkg}
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install_udev
find %{buildroot} -type f -name \*.a -exec %{__rm} -f {} \;
find %{buildroot} -type f -name \*.la -exec %{__rm}  -f {} \;
cd -
cd %{libpkg}/bindings/python
%pyproject_install
cd -
cd %{name}
make DESTDIR=%{buildroot} install
%oreon_autofiles libconcord usr/*/lib*.so.*
%oreon_autofiles libconcord-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles python3-libconcord usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%pyproject_check_import
%files
%files -n libconcord -f %{oreon_filedir}/libconcord.list
%files -n libconcord-devel -f %{oreon_filedir}/libconcord-devel.list
%files -n python3-libconcord -f %{oreon_filedir}/python3-libconcord.list

%changelog

%autochangelog
