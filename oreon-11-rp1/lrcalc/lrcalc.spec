%global source0_hash 996ac00e6ea8321ef09b34478f5379f613933c3254aeba624b6419b8afa5df57

Name:		lrcalc
Version:	2.1
Release:	15%{?dist}
License:	GPL-3.0-or-later
Summary:	Littlewood-Richardson Calculator
URL:		https://sites.math.rutgers.edu/~asbuch/lrcalc/
Source0:	https://sites.math.rutgers.edu/~asbuch/lrcalc/%{name}-%{version}.tar.gz
Source1:	lrcalc.module.in
Requires:	environment(modules)

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:	%{ix86}

BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	python3-devel
BuildRequires:	%{py3_dist cython}

%description
The "Littlewood-Richardson Calculator" is a package of C and Maple programs
for computing Littlewood-Richardson coefficients. The C programs form the
engine of the package, providing fast calculation of single LR coefficients,
products of Schur functions, and skew Schur functions. The Maple code mainly
gives an interface which makes it possible to use the C programs from Maple.
This interface uses the same notation as the SF package of John Stembridge, to
make it easier to use both packages at the same time.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package -n	python3-lrcalc
Summary:	Python interface to lrcalc
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n python3-lrcalc
Python interface to the Littlewood-Richardson Calculator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%generate_buildrequires
cd python
%pyproject_buildrequires

%build
%configure --bindir=%{_libdir}/%{name} --enable-shared --disable-static
# Kill rpaths
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool

%make_build

# Build the python interface
sed -e "/libraries/i\                  extra_link_args=['-L$PWD/src/.libs']," \
    -e 's/long_description_type/long_description_content_type/' \
    -i python/setup.py
cd python
ln -s ../src lrcalc
%pyproject_wheel
cd -

%install
%make_install
rm -rf %{buildroot}%{_datadir}/%{name}

mkdir -p %{buildroot}%{_datadir}/modulefiles
sed 's#@BINDIR@#'%{_libdir}/%{name}'#g;' < %{SOURCE1} > \
    %{buildroot}%{_datadir}/modulefiles/%{name}-%{_arch} 

cd python
%pyproject_install
%pyproject_save_files lrcalc
cd -

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir}: make check

%files
%doc AUTHORS ChangeLog README
%license COPYING LICENSE
%{_libdir}/%{name}/
%{_libdir}/lib%{name}.so.2{,.*}
%{_datadir}/modulefiles/%{name}-%{_arch}

%files		devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so

%files -n	python3-lrcalc -f %{pyproject_files}

%changelog
%autochangelog
