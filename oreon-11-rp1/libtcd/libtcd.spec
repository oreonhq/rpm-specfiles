%global source0_hash e1dde9aafb771eab57c676a99b4b79d61c6800990a0e72782bc20057a8a2d877

%global		postver	-r3
%global		postrpmver	%(echo "%postver" | sed -e 's|-|.|g' | sed -e 's|^\.||')

%global		mainver		2.2.7

%global		baserelease	12
%global		rpmrel		%{baserelease}%{?postver:.%postrpmver}

Name:		libtcd
Version:	%{mainver}
Release:	%{rpmrel}%{?dist}
Summary:	Tide Constituent Database Library
BuildRequires:	gcc
BuildRequires:	make

# https://gitlab.com/fedora/legal/fedora-license-data/-/merge_requests/553
# SPDX confirmed
License:	LicenseRef-Fedora-Public-Domain
URL:		http://www.flaterco.com/xtide/
Source0:	ftp://ftp.flaterco.com/xtide/%{name}-%{version}%{?postver}.tar.xz

%description
libtcd provides a software API for reading and writing Tide
Constituent Database (TCD) files.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags} -k

%install
make \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL="install -p" \
	install

# remove unneeded files
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.{a,la}
# This file is to be installed later
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/*html

%ldconfig_scriptlets

%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc *.html

%{_includedir}/*.h
%{_libdir}/*.so

%changelog
%autochangelog
