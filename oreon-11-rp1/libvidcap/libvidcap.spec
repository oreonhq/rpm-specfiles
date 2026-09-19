%global source0_hash 50bdabe1bb809e52677c3d5a02e118ce4a6d22828e42aebc8741e5b9a042741a

Name:		libvidcap
Version:	0.2.1
Release:	37%{?dist}
Summary:	Cross-platform video capture library
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
URL:		http://libvidcap.sourceforge.net/
Source0:	http://downloads.sourceforge.net/libvidcap/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:	kernel-headers, pkgconfig
BuildRequires: make

%description
A cross-platform library for capturing video from webcams and other video 
capture devices.

%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install INSTALL="%{_bindir}/install -p" DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc COPYING.LESSER
%{_libdir}/libvidcap.so.*

%files devel
%{_libdir}/libvidcap.so
%{_libdir}/pkgconfig/vidcap.pc
%{_includedir}/vidcap/

%changelog
%autochangelog
