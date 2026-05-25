Name:           libzfcphbaapi
Summary:        HBA API for the zFCP device driver
Version:        3.0.3
Release:        3%{?dist}
License:        EPL-1.0
URL:            https://github.com/ibm-s390-linux/libzfcphbaapi
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         %{name}-3.0.2-fedora.patch

ExclusiveArch:  s390 s390x

BuildRequires:  gcc
BuildRequires:  automake autoconf libtool
BuildRequires:  doxygen
BuildRequires:  sg3_utils-devel
BuildRequires:  make
Requires(post): grep sed

%description
zFCP HBA API Library is an implementation of FC-HBA (see www.t11.org) for
the zFCP device driver.


%package devel
Summary:  Development files for zFCP HBA API Library
Requires: %{name} = %{version}-%{release}
Conflicts: libhbaapi-devel

%description devel
Development files for the zFCP HBA API Library.

%package docs
Summary:  Documentation for zFCP HBA API Library
Requires: %{name} = %{version}-%{release}

%description docs
Documentation in HTML format for the zFCP HBA API Library.


%prep
%autosetup


%build
autoreconf -vif

%configure --disable-static
%make_build EXTRA_CFLAGS="-fno-strict-aliasing"


%install
%makeinstall docdir=%{buildroot}%{_docdir}/%{name}
# keep only html docs
rm -rf %{buildroot}%{_docdir}/%{name}/latex


%post
# remove old entry from hba.conf on upgrade
if [ $1 == 2 -a -f /etc/hba.conf ]; then
    grep -q -e "^libzfcphbaapi" /etc/hba.conf &&
        sed -i.orig -e "/^libzfcphbaapi/d" /etc/hba.conf
fi
:


%files
%license LICENSE
%doc README COPYING ChangeLog AUTHORS
%{_bindir}/zfcp_ping
%{_bindir}/zfcp_show
%{_libdir}/%{name}.so.*
%{_mandir}/man3/libzfcphbaapi.3*
%{_mandir}/man3/SupportedHBAAPIs.3*
%{_mandir}/man3/UnSupportedHBAAPIs.3*
%{_mandir}/man8/zfcp_ping.8*
%{_mandir}/man8/zfcp_show.8*

%files devel
%{_mandir}/man3/hbaapi.h.3*
%{_libdir}/%{name}.so
%{_includedir}/hbaapi.h

%files docs
%{_docdir}/%{name}/html


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.3-3
- Import
