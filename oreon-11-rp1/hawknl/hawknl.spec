%global source0_hash 31a2883dbfe02937c9c862bb1aac0b89e465bbab822513c06bffa3f13e4c3c2e

Name:           hawknl
Version:        1.68
Release:        38%{?dist}
Summary:        Game oriented network library
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ 
URL:            http://www.hawksoft.com/hawknl/
Source0:        http://www.sonic.net/~philf/download/HawkNL168src.tar.gz
Patch0:         hawknl-64bit.patch
Patch1:         hawknl-nlinternal.h.patch

BuildRequires:  gcc
BuildRequires: make
%description
HawkNL is a free, open source, game oriented network API released under the 
GNU LGPL. HawkNL (NL) is a fairly low level API, a wrapper over Berkeley/Unix
Sockets and Winsock. But NL also provides other features.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}%{version}
# some fixups
sed -i 's|ln -s $(LIBDIR)/$(OUTPUT)|ln -s $(OUTPUT)|g' src/makefile.linux
sed -i 's|-soname,NL.so|-soname,libNL.so|' src/makefile.linux
sed -i 's|\r||g' src/readme.txt src/nlchanges.txt

%build
make %{?_smp_mflags} -f makefile.linux \
  OPTFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}/%{name}
make -f makefile.linux install LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
  INCDIR=$RPM_BUILD_ROOT%{_includedir}/%{name}
# some apps want this semi-private header
install -p -m 0644 src/nlinternal.h $RPM_BUILD_ROOT%{_includedir}/%{name}
# some cleanup
rm $RPM_BUILD_ROOT%{_libdir}/libNL.a $RPM_BUILD_ROOT%{_libdir}/NL.so \
  $RPM_BUILD_ROOT%{_libdir}/libNL.so.1

%ldconfig_scriptlets

%files
%doc src/readme.txt src/nlchanges.txt
%{_libdir}/libNL.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/libNL.so

%changelog
%autochangelog
