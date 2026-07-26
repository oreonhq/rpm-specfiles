%global source0_hash 9b1e8e2aee2f0798c8399378dd6c2f5e9138017259aa18f18070cdf76b191d8e

%global minorver 1

Name:		ftplib
Version:	4.0
Release:	26%{?dist}
Summary:	Library of FTP routines
License:	LGPLv2+
URL:		http://nbpfaus.net/~pfau/ftplib-4/
Source0:	http://nbpfaus.net/~pfau/ftplib-4/%{name}-%{version}-%{minorver}.tar.gz
Patch0:		ftplib-3.1-1-modernize.patch
BuildRequires:	gcc
BuildRequires: make

%description
ftplib is a set of routines that implement the FTP protocol. They allow 
applications to create and access remote files through function calls 
instead of needing to fork and exec an interactive ftp client program.

%package devel
Summary:	Development files for ftplib
Requires:	ftplib = %{version}-%{release}

%description devel
Development libraries and headers for ftplib.

%package -n qftp
Summary:	Simple ftp client application
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later

%description -n qftp
Command line driven ftp file transfer program using ftplib.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}-%{minorver}
%patch -P0 -p1 -b .modern

%build
cd src/
make %{?_smp_mflags} DEBUG="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}
cd src/
make DESTDIR=$RPM_BUILD_ROOT LIBDIR="%{_libdir}" install

cd ${RPM_BUILD_ROOT}%{_libdir}
chmod +x libftp.so.4.0
ln -sf libftp.so.4.0 libftp.so.4
ln -sf libftp.so.4 libftp.so

cd ${RPM_BUILD_ROOT}%{_bindir}
for f in ftpdir ftpget ftplist ftprm ftpsend; do
	ln -s qftp $f
done

%ldconfig_scriptlets

%files
%doc CHANGES
%license LICENSE
%{_libdir}/libftp*.so.*

%files devel
%doc additional_rfcs README.ftplib* RFC959.txt html/
%{_includedir}/ftplib.h
%{_libdir}/libftp*.so

%files -n qftp
%doc README.qftp
%{_bindir}/ftpdir
%{_bindir}/ftpget
%{_bindir}/ftplist
%{_bindir}/ftprm
%{_bindir}/ftpsend
%{_bindir}/qftp

%changelog
%autochangelog
