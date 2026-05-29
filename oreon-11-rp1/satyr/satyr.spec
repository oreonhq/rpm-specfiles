%global source0_hash b001c90b404308d962858b95cbd7cb1e7f13bd5bcf2249a66321d4db406b4268

%if 0%{?fedora} || 0%{?rhel} > 7
# Enable python3 build by default
%bcond_without python3
%else
%bcond_with python3
%endif

%if 0%{?suse_version}
  %define libdw_devel libdw-devel
  %define libelf_devel libelf-devel
%else
  %define libdw_devel elfutils-devel
  %define libelf_devel elfutils-libelf-devel
%endif

%define glib_ver 2.43.4

Name: satyr
Version: 0.43
Release: 10%{?dist}
Summary: Tools to create anonymous, machine-friendly problem reports
License: GPL-2.0-or-later
URL: https://github.com/abrt/satyr
Source0:        https://github.com/abrt/satyr/releases/download/0.43/satyr-0.43.tar.gz

# Avoid the multiprocessing forkserver method
# Fix needed for Python 3.14
# https://bugzilla.redhat.com/2325452
Patch: https://github.com/abrt/satyr/pull/343.patch

%if %{with python3}
BuildRequires: python3-devel
%endif
BuildRequires: %{libdw_devel}
BuildRequires: %{libelf_devel}
BuildRequires: binutils-devel
BuildRequires: rpm-devel
BuildRequires: libtool
BuildRequires: doxygen
BuildRequires: pkgconfig
BuildRequires: make
BuildRequires: automake
BuildRequires: gcc-c++
BuildRequires: gdb
BuildRequires: gperf
BuildRequires: json-c-devel
BuildRequires: glib2-devel
%if %{with python3}
BuildRequires: python3-sphinx
%endif
Requires: json-c%{?_isa}
Requires: glib2%{?_isa} >= %{glib_ver}

%description
Satyr is a library that can be used to create and process microreports.
Microreports consist of structured data suitable to be analyzed in a fully
automated manner, though they do not necessarily contain sufficient information
to fix the underlying problem. The reports are designed not to contain any
potentially sensitive data to eliminate the need for review before submission.
Included is a tool that can create microreports and perform some basic
operations on them.

%package devel
Summary: Development libraries for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries and headers for %{name}.

%if %{with python3}
%package -n python3-satyr
%{?python_provide:%python_provide python3-satyr}
Summary: Python 3 bindings for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n python3-satyr
Python 3 bindings for %{name}.
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
autoreconf

%configure \
%if %{without python3}
        --without-python3 \
%endif
        --disable-static \
        --enable-doxygen-docs

%make_build

%install
%make_install

# Remove all libtool archives (*.la) from modules directory.
find %{buildroot} -name "*.la" -delete

%check
make check|| {
    # find and print the logs of failed test
    # do not cat tests/testsuite.log because it contains a lot of bloat
    cat tests/test-suite.log
    find tests/testsuite.dir -name "testsuite.log" -print -exec cat '{}' \;
    exit 1
}

%if 0%{?fedora} > 27
# ldconfig is not needed
%else
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%files
%doc README.md NEWS
%license COPYING
%{_bindir}/satyr
%{_mandir}/man1/%{name}.1*
%{_libdir}/lib*.so.*

%files devel
# The complex pattern below (instead of simlpy *) excludes Makefile{.am,.in}:
%doc apidoc/html/*.{html,png,css,js}
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%if 0%{?with_python3}
%files -n python3-satyr
%dir %{python3_sitearch}/%{name}
%{python3_sitearch}/%{name}/*
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.43-10
- Prepare for Oreon 11 (RP1)
