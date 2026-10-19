%global source0_hash f7e9383b8c0baa81b687e5b5eecc01beefaf1b19b64151d95ed61647fe7a315c
%global develdocdir %{_docdir}/%{name}-devel
Name:           libevent
Version:        2.1.13
Release:        1%{?dist}
Summary:        Abstract asynchronous event notification library
License:        BSD-3-Clause AND ISC AND LicenseRef-Fedora-Public-Domain
URL:            http://libevent.org/
Source0:        https://github.com/libevent/libevent/releases/download/release-%{version}-stable/libevent-%{version}-stable.tar.gz
%if ! 0%{?_module_build}
%endif
Patch01: libevent-nonettests.patch
Patch02: 0001-build-do-not-try-install-doxygen-man-pages-if-they-w.patch
Patch03: 0001-build-add-doxygen-to-all.patch
Patch04: 0001-Revert-Fix-checking-return-value-of-the-evdns_base_r.patch
# oreon:deps
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
# /oreon:deps
%description
The libevent API provides a mechanism to execute a callback function
when a specific event occurs on a file descriptor or after a timeout
has been reached. libevent is meant to replace the asynchronous event
loop found in event driven network servers. An application just needs
to call event_dispatch() and can then add or remove events dynamically
without having to change the event loop.

%package devel
Summary: Development files for %{name}
License: BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the header files and libraries for developing
with %{name}.

%package doc
Summary: Development documentation for %{name}
License: BSD-3-Clause AND MIT AND Apache-2.0
BuildArch: noarch
%description doc
This package contains the development documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n libevent-%{version}-stable

%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -i %{__python3} -pn test/check-dumpevents.py \
                               event_rpcgen.py

%build

./autogen.sh
%configure \
%if ! 0%{?_module_build}
    --enable-doxygen-doc \
%endif
    --disable-dependency-tracking --disable-static
%make_build all
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
mv $RPM_BUILD_ROOT/%{_docdir}/%{name} $RPM_BUILD_ROOT/%{develdocdir}
mv $RPM_BUILD_ROOT%{_includedir}/event2/event-config.h \
   $RPM_BUILD_ROOT%{_includedir}/event2/event-config-%{__isa_bits}.h
cat > $RPM_BUILD_ROOT%{_includedir}/event2/event-config.h << EOF
EOF
mkdir -p $RPM_BUILD_ROOT/%{develdocdir}/sample
(cd sample; \
	install -p -m 644 *.c *.am $RPM_BUILD_ROOT/%{develdocdir}/sample)
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libevent-devel -f %{oreon_filedir}/libevent-devel.list
%files -n libevent-doc -f %{oreon_filedir}/libevent-doc.list

%changelog

%autochangelog
