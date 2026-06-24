%global source0_hash none

Name:           libtiger
Version:        0.3.4
Release:        35%{?dist}
Summary:        Rendering library for Kate streams using Pango and Cairo

License:        LGPL-2.1-or-later
URL:            https://code.google.com/archive/p/libtiger
Source0:        https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/libtiger/libtiger-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libkate-devel >= 0.2.7
BuildRequires:  pango-devel
%ifarch %{valgrind_arches}
BuildRequires:  valgrind
%endif
BuildRequires:  doxygen


%description
Libtiger is a rendering library for Kate streams using Pango and Cairo.
More information about Kate streams may be found at 
http://wiki.xiph.org/index.php/OggKate


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pango-devel
Requires:       libkate-devel >= 0.2.7

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains Documentation for %{name}.



%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q


%build
%configure --disable-static
%make_build


%install
rm -rf __doc
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Fix timestramps change
touch -r include/tiger/tiger.h.in %{buildroot}%{_includedir}/tiger/tiger.h

# Move docdir
mv %{buildroot}%{_docdir}/%{name} __doc



%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/*.so.5{,.*}

%files devel
%{_includedir}/tiger/
%{_libdir}/*.so
%{_libdir}/pkgconfig/tiger.pc

%files doc
%doc examples __doc/html


%changelog
%autochangelog

