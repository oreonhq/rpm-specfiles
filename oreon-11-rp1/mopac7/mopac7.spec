%global source0_hash 6d7ac5d78522db70f7794fd816cea32829cfa9e93774202fe80ba5a54375fbaa

Name:           mopac7
Summary:        Semi-empirical quantum mechanics suite
Version:        1.15
Release:        51%{?dist}
# https://gitlab.com/fedora/legal/fedora-license-data/-/merge_requests/554
# SPDX confirmed
License:        LicenseRef-Fedora-Public-Domain
URL:            http://sourceforge.net/projects/mopac7/
Source0:        http://bioinformatics.org/ghemical/download/current/mopac7-%{version}.tar.gz
# Support C99, support -Werror=implicit-function-declaration
Patch0:         mopac7-1.15-c99-function-prototype.patch
# Some type size fix
Patch1:         mopac7-1.15-type-size.patch
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-gfortran
BuildRequires:  libtool
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
MOPAC7 is a semi-empirical quantum-mechanics code written by James
J. P. Stewart and co-workers. The purpose of this project is to
maintain MOPAC7 as a stand-alone program as well as a library that
provides the functionality of MOPAC7 to other programs.

%package        libs
Summary:        Dynamic libraries from %{name}

%description    libs
Dynamic libraries from %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
perl -pi -e "s#-lg2c##g" libmopac7.pc.in

%patch -P0 -p1
%patch -P1 -p1

%build
autoreconf -fiv
%set_build_flags

%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%make_install
# make install does not actually install the main binary
# chrpath --delete     fortran/.libs/%{name}
install -pDm0755 fortran/.libs/%{name} %{buildroot}%{_bindir}/%{name}
# install a convenience fortran wrapper for the main binary
sed "s;./fortran;%{_bindir};" run_mopac7 > %{buildroot}%{_bindir}/run_mopac7
chmod 755 %{buildroot}%{_bindir}/run_mopac7
# kill off the .la files
find %{buildroot}%{_libdir} -name *.la -delete -print
# kill off the makefiles in tests directory so we can use them as samples in %doc
find tests -name 'Makefile*' -delete -print

%ldconfig_scriptlets libs

%files
%doc tests
%{_bindir}/mopac7
%{_bindir}/run_mopac7

%files libs
%license COPYING
%{_libdir}/libmopac7.so.1*

%files devel
%doc AUTHORS ChangeLog NEWS README
%{_includedir}/mopac7/
%{_libdir}/libmopac7.so
%{_libdir}/pkgconfig/libmopac7.pc

%changelog
%autochangelog
