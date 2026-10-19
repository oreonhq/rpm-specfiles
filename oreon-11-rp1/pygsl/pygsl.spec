%global source1_hash 214c2ff76492bfc0bdc7eb18afdd4b62e5b64c34745852c6e0df8633788d1ae7
%global source0_hash 05474ecef352e388fceeb2ab4d83ca08cef2246ac4b7c49043ba97ea09bd04fb
%global sum GNU Scientific Library Interface for python
%global _docdir_fmt %{name}
%global _python_bytecompile_errors_terminate_build 0
Name:           pygsl
Version:        2.6.6
Release:        1%{?dist}
Summary:        GNU Scientific Library Interface for python
License:        GPL-2.0-or-later
URL:            https://github.com/pygsl/pygsl
VCS:            git:%{url}.git
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://www.gnu.org/software/gsl/doc/html/objects.inv
Patch:          %{name}-flexiblas.patch
Patch:          %{name}-rng-test.patch
Patch:          %{name}-incompatible-pointer.patch
Patch:          %{name}-format-mismatch.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  flexiblas-devel
BuildRequires:  gcc
BuildRequires:  gsl-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  swig
# /oreon:deps
%description
This project provides a python interface for the GNU scientific library (gsl).

%package -n python3-pygsl
Summary:       %{sum}
Obsoletes:     pygsl < 2.4.0-2
Provides:      pygsl = %{version}-%{release}
%description -n python3-pygsl
This project provides a python interface for the GNU scientific library (gsl).

%package -n python3-pygsl-devel
Summary:       Development files for pygsl
Requires:      python3-pygsl = %{version}-%{release}
Obsoletes:     pygsl-devel < 2.4.0-2
Provides:      pygsl-devel = %{version}-%{release}
%description -n python3-pygsl-devel
Development files for pygsl.

%package doc
Summary:       Reference manual for pygsl
License:       GFDL-1.1-no-invariants-or-later AND GPL-2.0-or-later
BuildArch:     noarch
%description doc
Reference manual for pygsl.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
fixtimestamp() {
  touch -r $1.orig $1
  rm $1.orig
}

# Fix character encodings
mv ChangeLog ChangeLog.orig
iconv -f ISO-8859-1 -t UTF-8 ChangeLog.orig > ChangeLog
fixtimestamp ChangeLog

# Fix end-of-line encodings
for f in api/pygsl.statistics ref/chebyshev ref/const ref/differentiation \
         ref/errors ref/histogram ref/ieee ref/index ref/old/ref_orig \
         ref/panda_rst/copyright ref/panda_rst/install ref/rng ref/sf \
         ref/statistics ref/sum ref-obsolete/copyright ref-obsolete/install \
         ref-obsolete/ref; do
  sed -i.orig 's/\r//g' doc/$f.rst
  fixtimestamp doc/$f.rst
done

sed -i.orig 's/\r//g' doc/win/pygsl_msys2_prepare.sh
fixtimestamp doc/win/pygsl_msys2_prepare.sh

# Use local objects.inv for intersphinx
sed -e "s|\('http://www.gnu.org/software/gsl/doc/html/', \)None|\1'%{SOURCE1}'|" \
    -i doc/conf.py

# Don't invoke python via env
%py3_shebang_fix pygsl typemaps/c.py

%build -p

export GSL_CBLAS_LIB=-lflexiblas
%install
%pyproject_install
chmod 0755 %{buildroot}%{python3_sitearch}/pygsl/{_generic_solver,block,chebyshev,fit,gsl_function,integrate,interpolation,minimize,monte,multi{fit{,_nlin},minimize,roots},odeiv,qrng,roots,siman,spline,vector}.py
mkdir %{buildroot}%{_includedir}
mv %{buildroot}%{python3_sitearch}/Include \
   %{buildroot}%{_includedir}/python%{python3_version}
sed -i '\%%cfg/__pycache__%%d' %{pyproject_files}
%{py3_test_envvars} sphinx-build -b html %{?_smp_mflags} doc html
rst2html --no-datestamp CREDITS.rst CREDITS.html
rst2html --no-datestamp README.rst README.html
rst2html --no-datestamp TODO.rst TODO.html
rm -fr html/.{buildinfo,doctrees}
%oreon_autofiles python3-pygsl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-pygsl-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export FLEXIBLAS=netlib
%pytest tests/
%files -f %{oreon_filedir}/main.list
%files -n python3-pygsl -f %{oreon_filedir}/python3-pygsl.list
%files -n python3-pygsl-devel -f %{oreon_filedir}/python3-pygsl-devel.list
%files -n pygsl-doc -f %{oreon_filedir}/pygsl-doc.list

%changelog

%autochangelog
