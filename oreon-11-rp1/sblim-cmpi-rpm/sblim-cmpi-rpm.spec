%global source0_hash 0cbbe5dc15ba6b89c17f834127531d5a96d7163ce41c23b49cddd94bf2a65a9e

Name:           sblim-cmpi-rpm
Version:        1.0.1
Release:        42%{?dist}
Summary:        CIM access to installed software packages (currently RPMs)

License:        CPL-1.0
URL:            http://sblim.wiki.sourceforge.net/ProviderCmpiRpm
Source0:        http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
Patch0:         sblim_cmpi_rpm_ldl_library.patch
Patch1:         sblim-cmpi-rpm-1.0.1-docdir.patch
Patch2:         sblim-cmpi-rpm-1.0.1-page-size.patch
Patch3:         sblim-cmpi-rpm-configure-c99.patch
Patch4:         sblim-cmpi-rpm-1.0.1-gcc14-fix.patch
BuildRequires: make
BuildRequires:  sblim-cmpi-base-devel sblim-cmpi-devel rpm-devel
BuildRequires:  gcc
Requires:       sblim-cmpi-base
Requires:       cim-server

%description
These providers list the software packages installed in a GNU/Linux system
and provide some more details about them. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Patch added to fix the missing definitions of dlopen, dlsym, dlerror.
%autopatch -p1

%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make
#make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/cmpi/*.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la 

%files
%{_libdir}/libcimrpm.so.0
%{_libdir}/libcimrpm.so.0.0.0
%{_libdir}/libcimrpmv4.so.0
%{_libdir}/libcimrpmv4.so.0.0.0
%{_libdir}/libcimrpm.so
%{_libdir}/libcimrpmv4.so
%{_libdir}/cmpi/libcmpiOSBase_RpmAssociatedFileProvider.so.0
%{_libdir}/cmpi/libcmpiOSBase_RpmAssociatedFileProvider.so.0.0.0
%{_libdir}/cmpi/libcmpiOSBase_RpmFileCheckProvider.so.0
%{_libdir}/cmpi/libcmpiOSBase_RpmFileCheckProvider.so.0.0.0
%{_libdir}/cmpi/libcmpiOSBase_RpmPackageProvider.so.0
%{_libdir}/cmpi/libcmpiOSBase_RpmPackageProvider.so.0.0.0
%{_libdir}/cmpi/libcmpiOSBase_RpmAssociatedFileProvider.so
%{_libdir}/cmpi/libcmpiOSBase_RpmFileCheckProvider.so
%{_libdir}/cmpi/libcmpiOSBase_RpmPackageProvider.so
%{_datarootdir}/sblim-cmpi-rpm/Linux_RpmPackage.mof
%{_datarootdir}/sblim-cmpi-rpm/Linux_RpmPackage.registration
%{_datarootdir}/sblim-cmpi-rpm/provider-register.sh
%{_includedir}/sblim/cimrpm.h
%{_includedir}/sblim/cimrpmfp.h
%doc COPYING NEWS INSTALL README AUTHORS

%global SCHEMA %{_datadir}/%{name}/Linux_RpmPackage.mof
%global REGISTRATION %{_datadir}/%{name}/Linux_RpmPackage.registration

%pre     
function unregister()
{
  %{_datadir}/%{name}/provider-register.sh -d \
        $1 \
        -m %{SCHEMA} \
        -r %{REGISTRATION} > /dev/null 2>&1 || :;
  # don't let registration failure when server not running fail upgrade!
}

# If upgrading, deregister old version
if [ $1 -gt 1 ]
then
        unregistered=no
        if [ -e /usr/sbin/cimserver ]; then
           unregister "-t pegasus";
           unregistered=yes
        fi  
         
        if [ -e /usr/sbin/sfcbd ]; then
           unregister "-t sfcb";
           unregistered=yes
        fi  
         
        if [ "$unregistered" != yes ]; then
           unregister
        fi  
fi

%post    
function register()
{        
  # The follwoing script will handle the registration for various CIMOMs.
  %{_datadir}/%{name}/provider-register.sh \
        $1 \
        -m %{SCHEMA} \
        -r %{REGISTRATION} > /dev/null 2>&1 || :;
  # don't let registration failure when server not running fail install!
}        
         
/sbin/ldconfig
if [ $1 -ge 1 ]
then     
        registered=no
        if [ -e /usr/sbin/cimserver ]; then
          register "-t pegasus";
          registered=yes
        fi
         
        if [ -e /usr/sbin/sfcbd ]; then
          register "-t sfcb";
          registered=yes
        fi
         
        if [ "$registered" != yes ]; then
          register
        fi
fi

%preun   
function unregister()
{        
  %{_datadir}/%{name}/provider-register.sh -d \
        $1 \
        -m %{SCHEMA} \
        -r %{REGISTRATION} > /dev/null 2>&1 || :;
  # don't let registration failure when server not running fail erase!
}        
         
if [ $1 -eq 0 ]
then     
        unregistered=no
        if [ -e /usr/sbin/cimserver ]; then
          unregister "-t pegasus";
          unregistered=yes
        fi
         
        if [ -e /usr/sbin/sfcbd ]; then
          unregister "-t sfcb";
          unregistered=yes
        fi
         
        if [ "$unregistered" != yes ]; then
          unregister
        fi
fi       
         
%postun -p /sbin/ldconfig

%changelog
%autochangelog
