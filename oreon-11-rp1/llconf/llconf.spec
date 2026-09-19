%global source0_hash e7c22541f64fb6f60d790efc7a7f6867867e091ca2d45c89eecb3fa73a62097f

Name:       llconf
Version:    0.4.6
Release:    31%{?dist}
Summary:    Loss-less configuration file parser
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:    LicenseRef-Callaway-LGPLv2+
# The code.google.com home is dead. There is
# <https://github.com/lipnitsk/llconf> but its 0.4.6 archive contains some
# additional files (e.g. src/parsers/cron.c copied into src/cron.c with
# changes license text.)
URL:        http://code.google.com/p/%{name}/
Source0:    http://%{name}.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:     llconf-0.4.6-Install-parsers-headers-into-subdirectory.patch
Patch1:     llconf-0.4.6-Unify-paths-in-examples.patch
# Fix a use-after-free in cnf_del_branch(),
# <https://github.com/lipnitsk/llconf/commit/aa33098dbe1246bc4d19843a63f25f799442f74a>
Patch2:     llconf-0.4.6-llconf-entry-fix-use-after-free-condition.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
Requires:   %{name}-libs%{?_isa} = %{version}-%{release}

%description
llconf (loss-less configuration) tool is meant as a middle ware to unify
control over configuration files. It tries to parse different
configuration files using different modules, and rewrite them after
applying changes, without destroying user changes and comments, so
that it is still possible to edit the files with a common text editor.

%package libs
Summary:    Loss-less configuration file parser library

%description libs
llconf (loss-less configuration) is meant as a middle ware to unify
control over configuration files. It tries to parse different
configuration files using different modules, and rewrite them after
applying changes, without destroying user changes and comments, so
that it is still possible to edit the files with a common text editor.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}-libs%{?_isa} = %{version}-%{release}
Requires:   pkgconfig

%description devel
Libraries and header files needed for developing applications that use
%{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
# Update libtool not to inject useless RPATH into resulting executable
libtoolize -fi
autoreconf -i
chmod -x examples/wizard

%build
%configure --disable-static
make %{?_smp_mflags}
make -C doc doxygen

%install
make install DESTDIR=$RPM_BUILD_ROOT
find "$RPM_BUILD_ROOT" -name '*.la' -delete

%ldconfig_scriptlets libs

%files
%doc examples/etc examples/wizard README.llconf
%{_bindir}/*

%files libs
%doc COPYING README 
%{_libdir}/*.so.*

%files devel
%doc examples/example.c doc/html
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
