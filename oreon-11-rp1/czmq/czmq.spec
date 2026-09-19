%global source0_hash 5d720a204c2a58645d6f7643af15d563a712dad98c9d32c1ed913377daa6ac39

Name:           czmq
Version:        4.2.1
Release:        %autorelease
Summary:        High-level C binding for 0MQ (ZeroMQ)

License:        MPL-2.0
URL:            http://czmq.zeromq.org
Source0:        https://github.com/zeromq/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libuuid-devel
BuildRequires:  pkgconfig(libzmq)
# --with-docs
BuildRequires:  perl-interpreter
BuildRequires:  perl(File::Basename)
BuildRequires:  asciidoc
BuildRequires:  xmlto
BuildRequires:  gcc-c++ cmake

%description
CZMQ has the following goals:
  i) To wrap the ZeroMQ core API in semantics that are natural and lead to
     shorter, more readable applications.
 ii) To hide the differences between versions of ZeroMQ.
iii) To provide a space for development of more sophisticated API semantics.

%package devel
Summary:        Development files for the czmq package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains files needed to develop applications using czmq.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# As of August 2021, the CMake build does not generate
# the documentation (man pages).
%configure --with-docs
%make_build

# Override the binary objects genrated by Autotools with CMake-built ones
%cmake -DCZMQ_BUILD_STATIC:BOOL=OFF
%cmake_build

%install
# For the doc and zproject - But it installs everything
%make_install install-dist_apiDATA

rm -f %{buildroot}%{_libdir}/libczmq.{a,la}

# Override the installation with CMake-build
%cmake_install

%check
#%%ctest

%files
%doc AUTHORS NEWS LICENSE
%{_libdir}/*.so.4*

%files devel
%doc CONTRIBUTING.md README.md
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/cmake/%{name}/
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*
%{_mandir}/man7/*.7*
%{_datarootdir}/zproject/

%changelog
%autochangelog
