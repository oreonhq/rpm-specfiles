%global source0_hash 0cbbe5dc15ba6b89c17f834127531d5a96d7163ce41c23b49cddd94bf2a65a9e
Name:           sblim-cmpi-rpm
Version:        1.0.1
Release:        1%{?dist}
Summary:        CIM access to installed software packages (currently RPMs)
License:        CPL-1.0
URL:            http://sblim.wiki.sourceforge.net/ProviderCmpiRpm
Source0:        http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
Patch0:         sblim_cmpi_rpm_ldl_library.patch
Patch1:         sblim-cmpi-rpm-1.0.1-docdir.patch
Patch2:         sblim-cmpi-rpm-1.0.1-page-size.patch
Patch3:         sblim-cmpi-rpm-configure-c99.patch
Patch4:         sblim-cmpi-rpm-1.0.1-gcc14-fix.patch
Requires:       sblim-cmpi-base
Requires:       cim-server
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  rpm-devel
BuildRequires:  sblim-cmpi-base-devel
BuildRequires:  sblim-cmpi-devel
# /oreon:deps
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
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/cmpi/*.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
%oreon_autofiles main

%pre     

function unregister()
{
  %{_datadir}/%{name}/provider-register.sh -d \
        $1 \
        -m %{SCHEMA} \
        -r %{REGISTRATION} > /dev/null 2>&1 || :;
}
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
  %{_datadir}/%{name}/provider-register.sh \
        $1 \
        -m %{SCHEMA} \
        -r %{REGISTRATION} > /dev/null 2>&1 || :;
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

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
