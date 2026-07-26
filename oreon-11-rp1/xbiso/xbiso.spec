%global source0_hash 5d7a051e2dc3d7ff07ac75ce6e6625e7aaaed4ca439401275ce54e96dc531c92

Name:		xbiso
Version:	0.6.1
Release:	38%{?dist}
Summary:	ISO extraction utility for xdvdfs images
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://sourceforge.net/projects/xbiso/
Source0:	http://downloads.sourceforge.net/xbiso/%{name}-%{version}.tar.gz
Patch0:		xbiso-0.6.1-destdir.patch
Patch1:		xbiso-0.6.1-ftplib4.patch
Patch2:		xbiso-configure-c99.patch
Patch3:		xbiso-c99.patch
Patch4:		xbiso-c23.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:	ftplib-devel

%description
xbiso is an ISO extraction utility for xdvdfs images.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1 -b .ftplib4
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
make DESTDIR=$RPM_BUILD_ROOT install

%files
%doc CHANGELOG LICENSE README
%{_bindir}/xbiso

%changelog
%autochangelog
