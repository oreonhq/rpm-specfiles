%global source0_hash deeed4a9ea87f62437990ddfb3c7c10e736010789fef81c04d93b371b0d2bb14

%global maj_ver 0
%global min_ver 9

Name:           dataquay
Version:        0.9.5
Release:        %autorelease
Summary:        Simple RDF for C++ and Qt applications

License:        X11-distribute-modifications-variant
URL:            https://www.breakfastquay.com/dataquay/
Source0:        https://www.breakfastquay.com/files/releases/dataquay-%{version}.tar.bz2

BuildRequires:  qt6-qtbase-devel
BuildRequires:  redland-devel
BuildRequires:  Xvfb xauth
BuildRequires:  make

%description
Dataquay is a free open source library that provides a friendly C++
interface to an RDF datastore using Qt classes and
containers. Supported datastores are the popular and feature-complete
Redland and the lightweight Sord.

Dataquay is simple to use and easy to integrate. It is principally
aimed at Qt-based applications that would like to use an RDF datastore
as backing for in-memory project data, to avoid having to invent file
formats or XML schemas and to make it easy to augment the data with
descriptive metadata pulled in from external sources. It's also useful
for applications with ad-hoc needs for metadata management using RDF
sources.

Dataquay does not use a separate database, instead using in-memory
storage with separate file import and export facilities. Although it
offers a choice of datastore implementations, the choice is made at
compile time: there is no runtime module system to take into account
when deploying your application.

The Fedora package is configured to use Redland, as recommended by the
developers for general use.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       redland-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# patch for multilib
%{__sed} -i.multilib 's|$${PREFIX}/lib|$${PREFIX}/%{_lib}|' lib.pro
%{__sed} -i.multilib 's|${exec_prefix}/lib|${exec_prefix}/%{_lib}|' \
         deploy/dataquay.pc.in
# patch declared version
%{__sed} -i.version 's|Version: 0.9.1|Version: %{version}|' \
         deploy/dataquay.pc.in

%build
%{qmake_qt6} dataquay.pro PREFIX=%{_prefix}
xvfb-run -a -w 1 make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}
# actually copy .pc file
%{__cp} -p deploy/dataquay.pc %{buildroot}%{_libdir}/pkgconfig/
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%license COPYING
%doc CHANGELOG README.txt
%{_libdir}/*.so.%{maj_ver}
%{_libdir}/*.so.%{maj_ver}.%{min_ver}
%{_libdir}/*.so.%{version}

%files devel
%doc examples
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
