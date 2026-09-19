%global source0_hash bcc763e4c56cdce8c7b6b162462273a14dfb3c289b230a7a618d9de9598db629

%global commit6 e23b9d3726b010c9e747786ffe72e38debc8cfef
%global shortcommit %(c=%{commit6}; echo ${c:0:7})
%global repo https://github.com/iguanaworks/iguanair-lirc/archive
%global __python %{__python3}

Name:           iguanaIR
Version:        1.1.0
Release:        40%{?dist}
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
# https://iguanaworks.net/projects/IguanaIR/ticket/317
Patch1:         changeset_2710.patch
Patch2:         rpath.patch
Patch3:         cmake-args.patch

# https://github.com/iguanaworks/iguanair-lirc/pull/1 (Patch10..Patch13)
Source10:       0010-Change-iguanaIR.-iguanair.-to-match-other-plugins.patch
Source11:       0011-Rename-link-README-files-to-match-modified-install-r.patch
Source12:       0012-Makefile-Add-DESTDIR-support.patch
Source13:       0013-Convert-all-files-to-LF-line-endings-like-main-drive.patch

Source20:       0020-build-Fix-DESTDIR-dont-update-docs.patch
Source21:       0016-reflasher-Move-to-python3.patch

Requires:       udev

BuildRequires:  cmake gcc
BuildRequires:  dos2unix
BuildRequires:  git
BuildRequires:  libusb1-devel
%if 0%{?fedora} < 37
libusb-devel
%endif
BuildRequires:  popt-devel
BuildRequires:  systemd

%{?systemd_requires}
Requires(post): systemd-sysv

# some features can be disabled during the rpm build
%{?_without_clock_gettime: %define _disable_clock_gettime --disable-clock_gettime}

# Filter away versioned plugin deps (they only depend on ABI):
%global __provides_exclude_from ^%{_libdir}/lirc/plugins/.*$

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

%if 0%{fedora} > 23
%package -n lirc-drv-iguanair
Summary: lirc plugin for iguanair user-space driver
Requires: lirc >= 0.9.4
BuildRequires: lirc-devel >= 0.9.4
BuildRequires: make

%description -n lirc-drv-iguanair
lirc plugin providing full support for the iguanaIR userspace driver,
the same as was built in into the lirc releases up to 0.9.3.
%endif

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
%if 0%{fedora} > 23
cd iguanair-lirc-%{commit6}
PLUGINDOCS=$(pkg-config --variable=plugindocs lirc-driver)
make LDFLAGS="-liguanaIR -L../build" CFLAGS="%{optflags} \
    -fpic -I.. -DHAVE_KERNEL_LIRC_H=1 -DPLUGINDOCS=\\\"$PLUGINDOCS\\\"" \
    DESTDIR=$RPM_BUILD_ROOT install
cd ..
%endif

mkdir -p $RPM_BUILD_ROOT/%{_datadir} || :
cp -ar files/python/usr/share/iguanaIR-reflasher $RPM_BUILD_ROOT/%{_datadir}
mkdir -p $RPM_BUILD_ROOT/%{_bindir} || :
cp -ar files/python/usr/bin/* $RPM_BUILD_ROOT/%{_bindir}

cd build
make install PREFIX=$RPM_BUILD_ROOT/usr DESTDIR=$RPM_BUILD_ROOT \
    INLIBDIR=$RPM_BUILD_ROOT%{_libdir}
rm -rf $RPM_BUILD_ROOT/%{_libdir}/python%{python_version}/site-packages

install -m755 -d $RPM_BUILD_ROOT%{_localstatedir}/run/%{name}

%if 0%{fedora} > 30
rm -rf $RPM_BUILD_ROOT/%{_libdir}/python2.7/site-packages
%endif

# fix missing links
pushd  $RPM_BUILD_ROOT%{_libdir}
rm libiguanaIR.so.0.3
mv libiguanaIR.so.0 libiguanaIR.so.0.3
ln -sf libiguanaIR.so.0.3 libiguanaIR.so.0

# Use /etc/sysconfig instead of /etc/default
mkdir $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig || :
mv  $RPM_BUILD_ROOT/etc/default/iguanaIR \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig

# Fix up some stray file permissions issues
         chmod a-x $RPM_BUILD_ROOT%{_includedir}/%{name}.h \
         $RPM_BUILD_ROOT%{_datadir}/%{name}-reflasher/hex/*

# Remove the installed initfile and install the systemd support instead.
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/init.d/
install -m644 -D %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -m755 -D %{SOURCE2} $RPM_BUILD_ROOT%{_libexecdir}/iguanaIR/rescan

# Install private log dir, tmpfiles.d setup.
install -m755 -d $RPM_BUILD_ROOT%{_localstatedir}/log/iguanaIR

install -m755 -d $RPM_BUILD_ROOT/%{_tmpfilesdir}
cat > $RPM_BUILD_ROOT/%{_tmpfilesdir}/%{name}.conf <<EOF
d   /run/%{name}    0755    iguanair   iguanair
EOF
install -m 755 -d $RPM_BUILD_ROOT/run/%{name}
install -m 644 -D %{SOURCE5} $RPM_BUILD_ROOT/etc/logrotate.d/%{name}

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

%files
%license LICENSE LICENSE-LGPL
%doc README.txt WHY ChangeLog AUTHORS
%doc README.fedora
%{_bindir}/igdaemon
%{_bindir}/igclient
%{_bindir}/iguanaIR-rescan
%{_libdir}/lib%{name}.so.*
%{_libdir}/%{name}/*.so
%{_libexecdir}/%{name}/
%{_unitdir}/%{name}.service
%config(noreplace) /etc/logrotate.d/%{name}
/lib/udev/rules.d/80-%{name}.rules
%config(noreplace) /etc/sysconfig/%{name}
%{_tmpfilesdir}/%{name}.conf
%ghost %attr(755, iguanair, iguanair) /run/%{name}
%attr(775, iguanair, iguanair) %{_localstatedir}/log/%{name}

%if 0%{fedora} < 30
%{_libdir}/python2.7/*
%endif

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%files reflasher
%{_datadir}/%{name}-reflasher/
%{_bindir}/%{name}-reflasher

%if 0%{fedora} > 23
%files -n lirc-drv-iguanair
%config /etc/modprobe.d/60-blacklist-kernel-iguanair.conf
%{_libdir}/lirc/plugins/iguanair.so
%{_docdir}/lirc/plugindocs/iguanair.html
%{_datadir}/lirc/configs/iguanair.conf
%endif

%changelog
%autochangelog
