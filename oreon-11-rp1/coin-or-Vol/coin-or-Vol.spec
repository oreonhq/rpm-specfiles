%global source0_hash 6cd53e2f4ad0aa68348901bf12fe146335812ee1d85bf272ae0c2bbd76faf1ae

%global		module		Vol

Name:		coin-or-%{module}
Summary:	Vol (Volume Algorithm)
Version:	1.5.4
Release:	18%{?dist}
License:	EPL-1.0
URL:		http://projects.coin-or.org/%{module}
Source0:	http://www.coin-or.org/download/pkgsource/%{module}/%{module}-%{version}.tgz
BuildRequires:	coin-or-Osi-devel
BuildRequires:	coin-or-Osi-doc
BuildRequires:	doxygen
BuildRequires:	gcc-c++
BuildRequires:	make

# Install documentation in standard rpm directory
Patch0:		%{name}-docdir.patch
Patch1: coin-or-Vol-configure-c99.patch

%description
Vol (Volume Algorithm) is an open-source implementation of a subgradient
method that produces primal as well as dual solutions. The primal solution
comes from estimating the volumes below the faces of the dual problem. This
is an approximate method so the primal vector might have small infeasiblities
that are negligible in many practical settings. The original subgradient
algorithm produces only dual solutions.

%package	devel
Summary:	Development files for %{name}
Requires:	coin-or-Osi-devel%{?_isa}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	doc
Summary:	Documentation files for %{name}
Requires:	coin-or-Osi-doc
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
This package contains the documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{module}-%{version}

%build
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
rm -f %{buildroot}%{_docdir}/%{name}/{LICENSE,vol_addlibs.txt}
cp -a doxydoc/{html,*.tag} %{buildroot}%{_docdir}/%{name}

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test

%ldconfig_scriptlets

%files
%license LICENSE
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/AUTHORS
%doc %{_docdir}/%{name}/README
%{_libdir}/libOsiVol.so.1
%{_libdir}/libOsiVol.so.1.*
%{_libdir}/libVol.so.1
%{_libdir}/libVol.so.1.*

%files		devel
%{_includedir}/coin/*
%{_libdir}/libOsiVol.so
%{_libdir}/libVol.so
%{_libdir}/pkgconfig/osi-vol.pc
%{_libdir}/pkgconfig/vol.pc

%files		doc
%{_docdir}/%{name}/html
%{_docdir}/%{name}/vol_doxy.tag

%changelog
%autochangelog
