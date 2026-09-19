%global source0_hash 79d4e1498e622fd937db5716aedf6b370ba4b1b259c5d04d88f976104ece8020

Name:		libax25
Version:        1.1.1
Release:        15%{?dist}
Summary:	AX.25 library for hamradio applications

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+

URL:		https://github.com/ve7fet/linuxax25

# git clone https://github.com/ve7fet/linuxax25.git
# cd linuxax25/libax25
# git archive --prefix=libax25-1.1.1/ -o ../libax25-1.1.1.tar.gz HEAD
Source0:	%{name}-%{version}.tar.gz

BuildRequires:  autoconf automake gcc libtool
BuildRequires:  gettext-devel
BuildRequires:  zlib-devel
BuildRequires: make

%description
libax25 is a library for ham radio applications that use the ax25 protocol. 
Included are routines to do ax25 address parsing, common ax25 application
config file parsing, etc. 

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
./autogen.sh
%configure --disable-static
%make_build

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Create /etc/ax25
mkdir -p %{buildroot}%{_sysconfdir}/ax25

# These headers conflict with glibc-headers.
rm -f %{buildroot}%{_includedir}/{netax25/ax25.h,netrom/netrom.h,netrose/rose.h}

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/*.so.*
%{_mandir}/man?/*
%dir %{_sysconfdir}/ax25

%files devel
%{_includedir}/*
%{_libdir}/*.so

%changelog
%autochangelog
