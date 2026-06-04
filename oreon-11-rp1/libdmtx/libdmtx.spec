%global source0_hash 2394bf1d1d693a5a4ca3cfcc1bb28a4d878bdb831ea9ca8f3d5c995d274bdc39

Name:           libdmtx
Version:        0.7.8
Release:        2%{?dist}
Summary:        Library for working with Data Matrix 2D bar-codes

License:        BSD-2-Clause-Views
URL:            https://github.com/dmtx
Source0:        https://github.com/dmtx/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make


%description
libdmtx is open source software for reading and writing Data Matrix 2D
bar-codes on Linux, Unix, OS X, Windows, and mobile devices. At its core
libdmtx is a shared library, allowing C/C++ programs to use its capabilities
without restrictions or overhead.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

./autogen.sh


%build
%configure --disable-static
%make_build


%install
%make_install


%check
make check
pushd test
for t in simple
do
    ./${t}_test/${t}_test
done
popd


%files
%license LICENSE
%doc AUTHORS ChangeLog KNOWNBUG README README.linux TODO
%{_libdir}/%{name}.so.*

%files devel
%doc
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/%{name}.3*


%changelog
* Sat Apr 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.8-2
- Import from Fedora dist-git f43 for Oreon 11
