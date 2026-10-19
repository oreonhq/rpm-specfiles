%global source0_hash 53e552d83e9294d67db37f0f4a23f15933a9ef698485301a18b98b40004cf0de
%global _fortify_level 2
%global sover        1
%global with_guile   1
%global with_octave  1
%global with_py3     1
%global guile_pkg    %(echo guile%{?guile_ver} | sed -e 's!\\\.!!g')
%global relversion 2.11.0
Name:              NLopt
Version:           2.11.0
%global tag        v%{version}
Release:        1%{?dist}
Summary:        Open-Source library for nonlinear optimization
%global lc_name    %{lua:print(string.lower(rpm.expand("%{name}")))}
License:           LicenseRef-Callaway-BSD AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-Public-Domain
URL:               http://ab-initio.mit.edu/%{lc_name}
Source0:        https://github.com/stevengj/nlopt/archive/%{tag}/nlopt-%{version}.tar.gz
Patch0:            nlopt-2.9.1-kill_rpath.patch
Patch1:            octave-build.patch
Provides:          bundled(gnulib)
Provides:          %{lc_name}                                      =  %{version}-%{release}
Provides:          %{lc_name}%{?_isa}                              =  %{version}-%{release}
# oreon:deps
BuildRequires:  cmake3
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  guile30-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  octave-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  swig
# /oreon:deps
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
find %{buildroot} -depth -name '*.*a' -print0 | xargs -0 rm -f
%if 0%{?with_octave}
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
%oreon_autofiles NLopt-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles NLopt-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles guile-NLopt usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles octave-NLopt usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-NLopt usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
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
%files -f %{oreon_filedir}/main.list
%files -n NLopt-devel -f %{oreon_filedir}/NLopt-devel.list
%files -n NLopt-doc -f %{oreon_filedir}/NLopt-doc.list
%files -n guile-NLopt -f %{oreon_filedir}/guile-NLopt.list
%files -n octave-NLopt -f %{oreon_filedir}/octave-NLopt.list
%files -n python3-NLopt -f %{oreon_filedir}/python3-NLopt.list

%changelog

%autochangelog
