%global source0_hash 6e4ecfc18b91586cc0c58e376a7e23a561cbd7e8756586e62d5d9450e1b42b25

%global libpkg libconcord

Name: concordance
Version: 1.5
Release: 19%{?dist}
Summary: Software to program the Logitech Harmony remote control

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: http://www.phildev.net/concordance/
Source0: https://github.com/jaymzh/concordance/releases/download/v%{version}/%{name}-%{version}.tar.bz2

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: hidapi-devel
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libcurl-devel
BuildRequires: libtool
BuildRequires: libzip-devel
BuildRequires: make
Requires: %{libpkg} = %{version}-%{release}

%description
This software will allow you to program your Logitech Harmony universal
remote control.

%package -n %{libpkg}
Summary: Library to talk to Logitech Harmony universal remote controls
Requires: udev
# For usbnet-based remotes: 900, 1000, 1100
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

%generate_buildrequires
cd %{libpkg}/bindings/python
%pyproject_buildrequires

%build
cd %{libpkg}

%configure --disable-static --disable-mime-update
make %{_smp_mflags}
cd -

# python bindings
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

# python bindings
cd %{libpkg}/bindings/python
%pyproject_install
%pyproject_save_files libconcord
cd -

cd %{name}
make DESTDIR=%{buildroot} install

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%pyproject_check_import

%files
%doc Changelog CodingStyle LICENSE SubmittingPatches TODO 
%doc README.md %{name}/INSTALL.linux
%attr(0755, root, root) %{_bindir}/*
%{_mandir}/man1/*

%files -n %{libpkg}
%doc Changelog CodingStyle LICENSE SubmittingPatches
%doc %{libpkg}/README %{libpkg}/INSTALL.linux
/lib/udev/rules.d/*.rules
/lib/udev/*.sh
%{_datadir}/mime/packages/%{libpkg}.xml
%{_libdir}/*.so.*

%files -n %{libpkg}-devel
%doc TODO
%{_includedir}/*.h
%{_libdir}/*.so

%files -n python3-%{libpkg} -f %{pyproject_files}
%doc %{libpkg}/bindings/python/README

%changelog
%autochangelog
