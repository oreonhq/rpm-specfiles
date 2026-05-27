%global source0_hash 507eb7b8d1015fbec5b935f34ebed15bf346bed04a11ab82b8eee848c4205aea

%global source_dir  %{_datadir}/%{name}-source
%global inst_srcdir %{buildroot}/%{source_dir}

Name:             libev
Version:          4.33
Release:          15%{?dist}
Summary:          High-performance event loop/event model with lots of features

License:          BSD-2-Clause OR GPL-2.0-or-later
URL:              http://software.schmorp.de/pkg/libev.html
Source0:          http://dist.schmorp.de/libev/Attic/%{name}-%{version}.tar.gz

BuildRequires:    autoconf
BuildRequires:    automake
BuildRequires:    coreutils
BuildRequires:    findutils
BuildRequires:    gcc
BuildRequires:    libtool
BuildRequires:    make
BuildRequires:    tar

Provides:         bundled(libecb) = 1.05

%description
Libev is modeled (very loosely) after libevent and the Event Perl
module, but is faster, scales better and is more correct, and also more
featureful. And also smaller.

%package devel
Summary:          Development headers for libev
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development headers and libraries for libev.

%package libevent-devel
Summary:          Compatibility development header with libevent for %{name}.
Requires:         %{name}-devel%{?_isa} = %{version}-%{release}

# The event.h file actually conflicts with the one from libevent-devel
Conflicts:        libevent-devel

%description libevent-devel
This package contains a development header to make libev compatible with
libevent.

%package source
Summary:          High-performance event loop/event model with lots of features
BuildArch:        noarch
Provides:         bundled(libecb) = 1.05

%description source
This package contains the source code for libev.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p0
autoreconf -vfi

%build
%configure --disable-static --with-pic
%make_build

%check
make check

%install
%make_install
rm -vf %{buildroot}%{_libdir}/%{name}.la

# Make the source package
mkdir -p %{inst_srcdir}
find . -type f | grep -E '.*\.(c|h|am|ac|inc|m4|h.in|man.pre|pl|txt)$' | xargs tar cf - | (cd %{inst_srcdir} && tar xf -)
install -p -m 0644 Changes ev.pod LICENSE README %{inst_srcdir}

%ldconfig_scriptlets

%files
%license LICENSE
%doc Changes README
%{_libdir}/%{name}.so.4*

%files devel
%{_includedir}/ev++.h
%{_includedir}/ev.h
%{_libdir}/%{name}.so
%{_mandir}/man?/*

%files libevent-devel
%{_includedir}/event.h

%files source
%{source_dir}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.33-15
- Import
