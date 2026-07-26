%global source0_hash 506f83a9e778ad4f204446e99509cb2bdf5539de8beccc260a014bd560237be1

# Use lower fortification level
# https://github.com/stevengj/nlopt/issues/563
%global _fortify_level 2

# Prevent accidental soname bumps.
%global sover        1

# Conditionals controlling the build.
%global with_guile   1
%global with_octave  1
%global with_py3     1

# Guile version
%if 0%{?fedora}
%global guile_ver    3.0
%endif
%global guile_pkg    %(echo guile%{?guile_ver} | sed -e 's!\\\.!!g')

%global relversion 2.10.0
Name:              NLopt
Version:           2.10.0
%global tag        v%{version}
Release:           9%{?dist}
Summary:           Open-Source library for nonlinear optimization

# Get a lowercase name for virtual provides.
%global lc_name    %{lua:print(string.lower(rpm.expand("%{name}")))}

# The detailed license-breakdown of the sources is:
#
# BSD (2 clause)
# --------------
# util/mt19937ar.c
#
#
# BSD (3 clause)
# --------------
# slsqp/*
#
#
# LGPL (v2 or later)
# ------------------
# luksan/*
#
# MIT/X11 (BSD like)
# ------------------
# api/*    auglag/*  bobyqa/*      cdirect/*  cobyla/*
# cquad/*  crs/*     direct/*      esch/*     isres/*
# mlsl/*   mma/*     neldermead/*  newuoa/*   octave/*
# stogo/*  tensor/*  test/*        util/* (ex. util/mt19937ar.c)
#
#
# Public Domain
# -------------
# praxis/*  subplex/*
#
# Automatically converted from old format: BSD and LGPLv2+ and MIT and Public Domain - review is highly recommended.
License:           LicenseRef-Callaway-BSD AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-Public-Domain
URL:               http://ab-initio.mit.edu/%{lc_name}
Source0:           https://github.com/stevengj/%{lc_name}/archive/%{tag}/%{lc_name}-%{version}.tar.gz

# Kill RPATH.
Patch0:            nlopt-2.9.1-kill_rpath.patch
# Enable build for Octave
# https://github.com/stevengj/nlopt/pull/597
# backported to release 2.10.0
Patch1:            octave-build.patch

BuildRequires:     cmake3
BuildRequires:     gcc
BuildRequires:     gcc-c++
BuildRequires:     gcc-gfortran
BuildRequires:     make
BuildRequires:     ncurses-devel

# The "gnulib" is a copylib and has a wildcard-permission from FPC.
# See: https://fedorahosted.org/fpc/ticket/174
Provides:          bundled(gnulib)
Provides:          %{lc_name}                                      =  %{version}-%{release}
Provides:          %{lc_name}%{?_isa}                              =  %{version}-%{release}

%description
NLopt is a library for nonlinear local and global optimization, for
functions with and without gradient information.  It is designed as
as simple, unified interface and packaging of several free/open-source
nonlinear optimization libraries.

It features bindings for GNU Guile, Octave and Python.  This build has
been made with C++-support enabled.

%package devel
Summary:           Development files for %{name}

Requires:          %{name}%{?_isa}                                 =  %{version}-%{release}
Provides:          %{lc_name}-devel                                =  %{version}-%{release}
Provides:          %{lc_name}-devel%{?_isa}                        =  %{version}-%{release}

%description devel
This package contains development files for %{name}.

%package doc
Summary:           Documentation files for %{name}
BuildArch:         noarch
Provides:          %{lc_name}-doc                                  =  %{version}-%{release}

%description doc
This package contains documentation files for %{name}.

%if 0%{?with_guile}
%package -n guile-%{name}
%{!?guile_pkgconf: %global guile_pkgconf %(%___build_pre; pkg-config --list-all | grep guile%{?guile_ver:-%{guile_ver}} | sed -e 's! .*$!!g')}
%{!?guile_sitedir: %global guile_sitedir %(%___build_pre; pkg-config --variable=sitedir %{guile_pkgconf})}
%{!?guile_extdir:  %global guile_extdir  %(%___build_pre; pkg-config --variable=extensiondir %{guile_pkgconf})}

Summary:           Guile bindings for %{name}

BuildRequires:     %{guile_pkg}-devel
BuildRequires:     pkgconfig
BuildRequires:     swig

Requires:          %{guile_pkg}%{?_isa}
Requires:          %{name}%{?_isa}                                 =  %{version}-%{release}

Provides:          guile-%{lc_name}                                =  %{version}-%{release}
Provides:          guile-%{lc_name}%{?_isa}                        =  %{version}-%{release}

%description -n guile-%{name}
This package contains Guile bindings for %{name}.
%endif

%if 0%{?with_octave}
%package -n octave-%{name}
%global octpkg %{name}
Summary:           Octave bindings for %{name}

BuildRequires:     octave-devel

Requires:          %{name}%{?_isa}                                 =  %{version}-%{release}
Requires:          octave
Requires(post):    octave
Requires(postun):  octave

Provides:          octave-%{lc_name}                               =  %{version}-%{release}
Provides:          octave-%{lc_name}%{?_isa}                       =  %{version}-%{release}

%description -n octave-%{name}
This package contains the Octave bindings for %{name}.
%endif

%if 0%{?with_py3}
%package -n python%{python3_pkgversion}-%{name}
Summary:           Python3 bindings for %{name}

BuildRequires:     python%{python3_pkgversion}-devel
BuildRequires:     python%{python3_pkgversion}-numpy

Requires:          %{name}%{?_isa}                                 =  %{version}-%{release}

Provides:          python%{python3_pkgversion}-%{lc_name}          =  %{version}-%{release}
Provides:          python%{python3_pkgversion}-%{lc_name}%{?_isa}  =  %{version}-%{release}

%description -n python%{python3_pkgversion}-%{name}
This package contains Python3 bindings for %{name}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{lc_name}-%{version} -p 1

# Move all %%doc to topdir and append their belonging.
[[ -f README.md ]] &&  \
mv -f README.md README
_topdir="`pwd`"
for _dir in `find . -type d |                              \
  sed -e "/\.libs/d" -e "s/\.\///g" -e "/\./d" | sort -u`
do
  pushd ${_dir}
  for _file in 'AUTHOR*' 'COPY*' 'README*' '*[Pp][Dd][Ff]'
  do
    for _doc in `find . -maxdepth 1 -name "${_file}"`
    do
      mv -f ${_doc} ${_topdir}/${_doc}.`echo ${_dir} | sed -e "s/\//_/g"`
    done
  done
  popd
done

%build
%cmake3                                     \
  -DNLOPT_CXX=ON                            \
  -DNLOPT_FORTRAN=ON                        \
  -DNLOPT_PYTHON=ON                         \
  -DNLOPT_OCTAVE=ON                         \
  -DNLOPT_MATLAB=OFF                        \
  -DNLOPT_GUILE=ON                          \
  -DNLOPT_SWIG=ON                           \
  -DNLOPT_TESTS=ON                          \
  -DBUILD_SHARED_LIBS=ON                    \
  -DPYTHON_EXECUTABLE=%{__python3}          \
  -DINSTALL_PYTHON_DIR=%{python3_sitearch}  \
  -DINSTALL_M_DIR=%{octpkgdir}              \
  -DINSTALL_OCT_DIR=%{octpkglibdir}
%cmake3_build

%install
%cmake3_install

# We don't want these static-libs and libtool-dumplings
find %{buildroot} -depth -name '*.*a' -print0 | xargs -0 rm -f

%if 0%{?with_octave}
# Setup octave stuff properly.
mkdir -p %{buildroot}%{octpkgdir}/packinfo
chmod 0755 %{buildroot}%{octpkglibdir}/*.oct
install -pm 0644 COPYING %{buildroot}%{octpkgdir}/packinfo

cat > %{buildroot}%{octpkgdir}/packinfo/DESCRIPTION << EOF
Name: %{name}
Version: %{version}
Date: %(date +%Y-%m-%d)
Author: Steven G. Johnson <stevenj@alum.mit.edu>
Title: Open-Source library for nonlinear optimization
Description: NLopt is a library for nonlinear local and global
 optimization, for functions with and without gradient information.
 It is designed as as simple, unified interface and packaging of
 several free/open-source nonlinear optimization libraries.
Url: %{url}
EOF

cat > %{buildroot}%{octpkgdir}/packinfo/on_uninstall.m << EOF
function on_uninstall (desc)
  error ('Can not uninstall %s installed by the redhat package manager', desc.name);
endfunction
EOF
%endif

%check
%ctest3

%ldconfig_scriptlets

%if 0%{?with_octave}
%post -n octave-%{name}
%octave_cmd pkg rebuild

%preun -n octave-%{name}
%octave_pkg_preun

%postun -n octave-%{name}
%octave_cmd pkg rebuild
%endif

%files
%doc ChangeLog NEWS.md
%license COPY*
%{_libdir}/lib%{lc_name}.so.%{sover}*

%files devel
%doc %{_mandir}/man3/*
%{_includedir}/*
%{_libdir}/cmake/nlopt/
%{_libdir}/lib%{lc_name}.so
%{_libdir}/pkgconfig/%{lc_name}.pc

%files doc
%doc AUTHOR* ChangeLog NEWS.md README* TODO *.[Pp][Dd][Ff].*
%license COPY*

%if 0%{?with_guile}
%files -n guile-%{name}
%{guile_extdir}/*nlopt_guile.so
%{guile_sitedir}/*
%endif

%if 0%{?with_octave}
%files -n octave-%{name}
%{octpkglibdir}
%{octpkgdir}
%endif

%files -n python%{python3_pkgversion}-%{name}
%{python3_sitearch}/*.so*
%{python3_sitearch}/*.py*
%{python3_sitearch}/__pycache__/*.py*
%dir %{python3_sitearch}/%{lc_name}-%{relversion}.dist-info
%{python3_sitearch}/%{lc_name}-%{relversion}.dist-info/METADATA

%changelog
%autochangelog
