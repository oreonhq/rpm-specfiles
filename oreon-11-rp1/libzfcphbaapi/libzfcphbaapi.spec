%global source0_hash 70cee88660334342b17e73d4b46f13f356332c04e7f07c09f6fc2d669b20ccca
Name:           libzfcphbaapi
Summary:        HBA API for the zFCP device driver
Version:        3.0.3
Release:        1%{?dist}
License:        EPL-1.0
URL:            https://github.com/ibm-s390-linux/libzfcphbaapi
Source0:        https://github.com/ibm-s390-linux/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         %{name}-3.0.2-fedora.patch
ExclusiveArch:  s390 s390x
Requires(post): grep sed
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  sg3_utils-devel
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -vif
%configure --disable-static
%make_build EXTRA_CFLAGS="-fno-strict-aliasing"
%install
%makeinstall docdir=%{buildroot}%{_docdir}/%{name}
rm -rf %{buildroot}%{_docdir}/%{name}/latex
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%post

if [ $1 == 2 -a -f /etc/hba.conf ]; then
    grep -q -e "^libzfcphbaapi" /etc/hba.conf &&
        sed -i.orig -e "/^libzfcphbaapi/d" /etc/hba.conf
fi
:
%files -f %{oreon_filedir}/main.list
%files -n libzfcphbaapi-devel -f %{oreon_filedir}/libzfcphbaapi-devel.list
%files -n libzfcphbaapi-docs -f %{oreon_filedir}/libzfcphbaapi-docs.list

%changelog

%autochangelog
