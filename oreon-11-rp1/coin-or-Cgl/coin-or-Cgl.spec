%global source0_hash 558421ccd6aa91d6922dd1baa04e37aa4c75ba0472118dc11779e5d6a19bfb38

%global		module		Cgl

Name:		coin-or-%{module}
Summary:	Cut Generation Library
Version:	0.60.9
Release:	6%{?dist}

# The project as a whole is licensed EPL-2.0.  However, many source files still
# claim to be licensed EPL-1.0.  This is probably an upstream oversight.
License:	EPL-2.0 AND EPL-1.0
URL:		https://github.com/coin-or/%{module}
VCS:		git:%{url}.git
Source0:	%{url}/archive/releases/%{version}/%{module}-%{version}.tar.gz
BuildRequires:	coin-or-CoinUtils-doc
BuildRequires:	doxygen
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	pkgconfig(clp)
BuildRequires:	pkgconfig(dylp)
BuildRequires:	pkgconfig(vol)

# Install documentation in standard rpm directory
Patch0:		%{name}-docdir.patch

# Fix use of uninitialized variables
Patch1:		%{name}-uninit.patch

# Avoid implicit function declarations in the configure script
Patch2:		%{name}-configure-c99.patch

# Soplex lets a macro named EPS leak into the global namespace
Patch3:		%{name}-undef-EPS.patch

%description
The COIN-OR Cut Generation Library (Cgl) is a collection of cut generators
that can be used with other COIN-OR packages that make use of cuts, such as,
among others, the linear solver Clp or the mixed integer linear programming
solvers Cbc or BCP.

%package	devel
Summary:	Development files for %{name}
Requires:	coin-or-Osi-devel%{?_isa}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	doc
Summary:	Documentation files for %{name}
Requires:	coin-or-CoinUtils-doc
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
This package contains the documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{module}-releases-%{version}

%build
export CPPFLAGS='-DNDEBUG'
%configure

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build all doxydoc

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_docdir}/%{name}/{LICENSE,cgl_addlibs.txt}
cp -a README.md doxydoc/{html,*.tag} %{buildroot}%{_docdir}/%{name}

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test

%files
%license LICENSE
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/README.md
%{_libdir}/libCgl.so.1
%{_libdir}/libCgl.so.1.*

%files		devel
%{_includedir}/coin/*
%{_libdir}/libCgl.so
%{_libdir}/pkgconfig/cgl.pc

%files		doc
%{_docdir}/%{name}/html
%{_docdir}/%{name}/cgl_doxy.tag

%changelog
%autochangelog
