%global source0_hash none

%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%{!?tcl_sitelib: %global tcl_sitelib %{_datadir}/tcl%{tcl_version}}
%global tixmajor 8.4
%global tcltkver 1:8.4.13

Summary: A set of extension widgets for Tk
Name: tix
Epoch: 1
Version: %{tixmajor}.3
Release: 46%{?dist}
License: TCL
URL: http://tix.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/Tix%{version}-src.tar.gz
#  0: Fixes BZ#81297 (soname of libraries)
Patch0: tix-8.4.2-link.patch
Patch1: tix-8.4.3-tcl86.patch
Patch2: tix-8.4.3-covscan-fixes.patch
Patch3: tix-implicit-int.patch
Patch4: tix-configure-c99.patch
Patch5: tix-c89.patch
Requires: tcl(abi) = 8.6
Requires: ((tcl >= %{tcltkver} with tcl < 1:9) or tcl8 >= %{tcltkver})
Requires: ((tk >= %{tcltkver} with tk < 1:9) or tk8 >= %{tcltkver})
Requires: /etc/ld.so.conf.d
BuildRequires: make
BuildRequires: (tcl-devel >= %{tcltkver} with tcl-devel < 1:9)
BuildRequires: (tk-devel >= %{tcltkver} with tk-devel < 1:9)
BuildRequires: libX11-devel
BuildRequires: gcc

%description
Tix, the Tk Interface eXtension, is a powerful set of user interface
components that expands the capabilities of your Tcl/Tk and Python
applications. Using Tix together with Tk will greatly enhance the
appearance and functionality of your application.

%package devel
Summary: Tk Interface eXtension development files
Requires: tix = %{epoch}:%{version}-%{release}

%description devel
Tix, the Tk Interface eXtension, is a powerful set of user interface
components that expands the capabilities of your Tcl/Tk and Python
applications. Using Tix together with Tk will greatly enhance the
appearance and functionality of your application.

This package contains the tix development files needed for building
tix applications.

%package doc
Summary: Tk Interface eXtension documentation
Requires: tix = %{epoch}:%{version}-%{release}

%description doc
Tix, the Tk Interface eXtension, is a powerful set of user interface
components that expands the capabilities of your Tcl/Tk and Python
applications. Using Tix together with Tk will greatly enhance the
appearance and functionality of your application.

This package contains the tix documentation

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n Tix%{version}

# Remove executable permission of images in html documentation
chmod ugo-x docs/html/gif/tix/*.png docs/html/gif/tix/*.gif \
  docs/html/gif/tix/*/*.gif

# Fix end-of-line encoding
sed -i 's/\r//' docs/Release-8.4.0.txt

%build
%configure --with-tcl=%{_libdir} --with-tk=%{_libdir} --libdir=%{tcl_sitearch}
%make_build all PKG_LIB_FILE=libTix.so

%install
%make_install PKG_LIB_FILE=libTix.so

# move shared lib to tcl sitearch
mv $RPM_BUILD_ROOT%{tcl_sitearch}/Tix%{version}/libTix.so \
	$RPM_BUILD_ROOT%{tcl_sitearch}
pwd
# make links
ln -sf ../libTix.so \
	$RPM_BUILD_ROOT%{tcl_sitearch}/Tix%{version}/libTix.so
ln -sf tcl%{tcl_version}/Tix%{version}/libTix.so $RPM_BUILD_ROOT%{_libdir}/libTix.so
ln -sf tcl%{tcl_version}/Tix%{version}/libTix.so $RPM_BUILD_ROOT%{_libdir}/libtix.so

# install demo scripts
mkdir -p $RPM_BUILD_ROOT%{tcl_sitelib}/Tix%{tixmajor}
cp -a demos $RPM_BUILD_ROOT%{tcl_sitelib}/Tix%{tixmajor}

# the header and man pages were in the previous package, keeping for now...
mkdir -p $RPM_BUILD_ROOT%{_includedir}
install -m 0644 generic/tix.h $RPM_BUILD_ROOT%{_includedir}/tix.h
mkdir -p $RPM_BUILD_ROOT%{_mandir}/mann
cp man/*.n $RPM_BUILD_ROOT%{_mandir}/mann

# Handle unique library path (so apps can actually find the library)
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d
echo "%{tcl_sitearch}" > $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d/tix-%{_arch}.conf

# ship docs except pdf
rm -rf docs/pdf
find docs -name .cvsignore -exec rm '{}' ';'

# these files end up in the doc directory
rm -f $RPM_BUILD_ROOT%{_libdir}/Tix%{tixmajor}/README.txt
rm -f $RPM_BUILD_ROOT%{_libdir}/Tix%{tixmajor}/license.terms

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{tcl_sitearch}/libTix.so
%{tcl_sitearch}/Tix%{version}
%{_sysconfdir}/ld.so.conf.d/*
%doc *.txt *.html license.terms

%files devel
%{_includedir}/tix.h
%{_libdir}/libtix.so
%{_libdir}/libTix.so
%{_mandir}/mann/*.n*

%files doc
%doc docs/*
%doc %{tcl_sitelib}/Tix%{tixmajor}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:8.4.3-46
- Import
