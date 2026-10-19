%global source0_hash e87dcaaa28e905b574ccf3d49e23e05c73edb3f99136dcd566bca16829ab6694
Name:           libcpucycles
Version:        20260105
Release:        1%{?dist}
Summary:        Library for counting CPU cycles
License:        LicenseRef-Fedora-Public-Domain OR 0BSD OR MIT-0 OR MIT
URL:            https://cpucycles.cr.yp.to/
Source0:        https://cpucycles.cr.yp.to/libcpucycles-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3
# /oreon:deps
%description
libcpucycles support several machine-level cycle counters and OS-level
mechanisms on many CPU architectures and auto-selects the best performing one
when it's initialized.

%package devel
Summary:        Development files for libcpucycles
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
libcpucycles headers and other development files.

%package static
Summary:        Static version of the libcpucycles library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%description static
Statically linkable version of the libcpucycles library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

cat compilers/default
echo '%{__cc} %{build_cflags} %{build_ldflags} -fPIC -fwrapv -fvisibility=hidden' > compilers/default
./configure --prefix=%{_prefix}
%make_build
echo '%{__cc} %{build_cflags} %{build_ldflags} -fPIE -fwrapv -fvisibility=hidden' > compilers/default
rm build/0/cpucycles/*.o
rm build/0/package/lib/libcpucycles.a
make -C build/0 package/lib/libcpucycles.a %{?_smp_mflags}
%install
%make_install
if [ %{buildroot}%{_prefix}/lib != %{buildroot}%{_libdir} ]; then
    mv %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir}
fi
chmod 755 %{buildroot}%{_libdir}/*.so.*
mkdir -p %{buildroot}%{_prefix}/share
mv %{buildroot}%{_prefix}/man %{buildroot}%{_prefix}/share
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

LD_LIBRARY_PATH=$PWD/build/0/package/lib ./build/0/package/bin/cpucycles-info
%files -f %{oreon_filedir}/main.list
%files -n libcpucycles-devel -f %{oreon_filedir}/libcpucycles-devel.list
%files -n libcpucycles-static -f %{oreon_filedir}/libcpucycles-static.list

%changelog

%autochangelog
