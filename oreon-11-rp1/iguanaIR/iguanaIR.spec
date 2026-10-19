%global source0_hash 0ff80e53b7e4e704cb26adb98e7246c79db2088bc4d8b51e33863343f53c4e29
%global commit6 e23b9d3726b010c9e747786ffe72e38debc8cfef
%global shortcommit %(c=%{commit6}; echo ${c:0:7})
%global repo https://github.com/iguanaworks/iguanair-lirc/archive
%global __python %{__python3}
Name:           iguanaIR
Version:        1.1.0
Release:        1%{?dist}
Epoch:          2
Summary:        Driver for Iguanaworks USB IR transceiver
License:        GPLv2 and LGPLv2
URL:            http://iguanaworks.net/ir
Source0:        http://iguanaworks.net/downloads/%{name}-%{version}.tar.bz2
Source1:        iguanaIR.service
Source2:        iguanaIR-rescan
Source3:        README.fedora
Source4:        patch-soname
Source5:        iguanaIR.logrotate
Source6:        %{repo}/%{commit6}/iguanair-lirc-%{shortcommit}.tar.gz
Patch1:         changeset_2710.patch
Patch2:         rpath.patch
Patch3:         cmake-args.patch
Source10:       0010-Change-iguanaIR.-iguanair.-to-match-other-plugins.patch
Source11:       0011-Rename-link-README-files-to-match-modified-install-r.patch
Source12:       0012-Makefile-Add-DESTDIR-support.patch
Source13:       0013-Convert-all-files-to-LF-line-endings-like-main-drive.patch
Source20:       0020-build-Fix-DESTDIR-dont-update-docs.patch
Source21:       0016-reflasher-Move-to-python3.patch
Requires:       udev
%{?systemd_requires}
Requires(post): systemd-sysv
%{?_without_clock_gettime: %define _disable_clock_gettime --disable-clock_gettime}
%global __provides_exclude_from ^%{_libdir}/lirc/plugins/.*$
# oreon:deps
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  libusb1-devel
BuildRequires:  popt-devel
BuildRequires:  systemd
# /oreon:deps
%description
This package provides igdaemon and igclient, the programs necessary to
control the Iguanaworks USB IR transceiver.

%package devel
Summary: Library and header files for iguanaIR
Requires: %{name} = %{epoch}:%{version}-%{release}
%description devel
The development files needed to interact with the iguanaIR igdaemon are
included in this package.

%package reflasher
Summary: Reflasher for Iguanaworks USB IR transceiver
BuildArch: noarch
%description reflasher
This package provides the reflasher/testing script and assorted firmware
versions for the Iguanaworks USB IR transceiver.  If you have no idea
what this means, you don't need it.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
%setup -q -T -D -a 6
%patch -P1 -p3
%patch -P2 -p1
%patch -P3 -p1
cp %{SOURCE3} README.fedora
cd iguanair-lirc-%{commit6}
patch -p1 < %{SOURCE10}
patch -p1 < %{SOURCE11}
patch -p1 < %{SOURCE12}
git apply --whitespace=fix %{SOURCE13}
dos2unix Makefile
patch -l -p2 --fuzz 2 < %{SOURCE20}
cd ..
patch  -p1 --fuzz 2 < %{SOURCE21}

%build

./runCmake -DLIBDIR="%{_libdir}"
cd build
make CFLAGS="%{optflags} -fpic -DFEDORA=1 -DHAVE_KERNEL_LIRC_H=1 -I.." %{?_smp_mflags}
cp %{SOURCE4} .
%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir} || :
cp -ar files/python/usr/share/iguanaIR-reflasher $RPM_BUILD_ROOT/%{_datadir}
mkdir -p $RPM_BUILD_ROOT/%{_bindir} || :
cp -ar files/python/usr/bin/* $RPM_BUILD_ROOT/%{_bindir}
cd build
make install PREFIX=$RPM_BUILD_ROOT/usr DESTDIR=$RPM_BUILD_ROOT \
    INLIBDIR=$RPM_BUILD_ROOT%{_libdir}
rm -rf $RPM_BUILD_ROOT/%{_libdir}/python%{python_version}/site-packages
install -m755 -d $RPM_BUILD_ROOT%{_localstatedir}/run/%{name}
pushd  $RPM_BUILD_ROOT%{_libdir}
rm libiguanaIR.so.0.3
mv libiguanaIR.so.0 libiguanaIR.so.0.3
ln -sf libiguanaIR.so.0.3 libiguanaIR.so.0
mkdir $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig || :
mv  $RPM_BUILD_ROOT/etc/default/iguanaIR \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
         chmod a-x $RPM_BUILD_ROOT%{_includedir}/%{name}.h \
         $RPM_BUILD_ROOT%{_datadir}/%{name}-reflasher/hex/*
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/init.d/
install -m644 -D %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -m755 -D %{SOURCE2} $RPM_BUILD_ROOT%{_libexecdir}/iguanaIR/rescan
install -m755 -d $RPM_BUILD_ROOT%{_localstatedir}/log/iguanaIR
install -m755 -d $RPM_BUILD_ROOT/%{_tmpfilesdir}
cat > $RPM_BUILD_ROOT/%{_tmpfilesdir}/%{name}.conf <<EOF
d   /run/%{name}    0755    iguanair   iguanair
EOF
install -m 755 -d $RPM_BUILD_ROOT/run/%{name}
install -m 644 -D %{SOURCE5} $RPM_BUILD_ROOT/etc/logrotate.d/%{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pre

getent group iguanair >/dev/null || groupadd -r iguanair
getent passwd iguanair >/dev/null || \
    useradd -r -g iguanair -d %{_localstatedir}/run/%{name} -s /sbin/nologin \
    -c "Iguanaworks IR Daemon" iguanair
exit 0
%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list
%files -n iguanaIR-devel -f %{oreon_filedir}/iguanaIR-devel.list
%files -n iguanaIR-reflasher -f %{oreon_filedir}/iguanaIR-reflasher.list

%changelog

%autochangelog
