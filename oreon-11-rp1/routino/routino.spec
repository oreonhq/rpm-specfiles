%global source0_hash 4eba067d32c97ca9388ad6e97c0f5a3c10d48829367240d78c51375d8cc11e54

Name: routino
Summary: Router for OpenStreetMap Data
Version: 3.4.3
Release: 3%{?dist}
License: AGPL-3.0-or-later AND MIT
URL: http://www.routino.org/
Source0: http://www.routino.org/download/routino-%{version}.tgz
# documentation for how to set up Routino for use with Marble
Source1: README-MARBLE.txt
# https://github.com/sharkcz/routino/commits/fedora
Patch0: routino-3.4-fedora.patch
BuildRequires: make
BuildRequires: gcc
BuildRequires: bzip2-devel
BuildRequires: xz-devel
BuildRequires: zlib-devel
BuildRequires: perl-generators
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
Routino is a command-line application for finding a route between two points
using the dataset of topographical information collected by OpenStreetMap. It
can be used as a routing tool in Marble.

%package libs
Summary: Routing library for OpenStreetMap Data
Requires: %{name}-data = %{version}-%{release}

%description libs
The Routino library is a library for finding a route between two points using
the dataset of topographical information collected by OpenStreetMap. It can be
used by applications to embed Routino, as long as the application's license is
compatible with the AGPLv3.

%package data
Summary: Data files for %{name} and %{name}-libs
BuildArch: noarch

%description data
This package contains the architecture-independent data files used by %{name}
and %{name}-libs.

%package doc
Summary: Documentation files for %{name} and %{name}-libs
BuildArch: noarch
# ensure the version matches the actual library (and application if installed)
Requires: %{name}-libs = %{version}-%{release}

%description doc
This package contains the architecture-independent documentation files for
%{name} and %{name}-libs.

%package devel
Summary: Development files for %{name}-libs
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains the files required to compile applications that use
%{name}-libs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

cp -p %{SOURCE1} doc/

# Get rid of installation documentation which is not applicable to the RPM
rm -f INSTALL*.txt doc/INSTALL*.txt doc/html/installation.html
# The web stuff needs more work to be packaged. The makefiles will copy things
# into the web directory if it's present, so get rid of it now.
rm -rf web
# Upstream builds but does not install extras. Don't waste build time, nor
# bother fixing the parallel make breakage there.
rm -rf extras

%build
%make_build libdir=%{_libdir}

%install
%make_install libdir=%{_libdir}

%files
%{_bindir}/%{name}-*

%files libs
%{_libdir}/lib%{name}*.so.*

%files data
%license agpl-3.0.txt
%{_datadir}/%{name}/

%files doc
%{_docdir}/%{name}/

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}*.so

%changelog
%autochangelog
