%global source0_hash 6cd53e2f4ad0aa68348901bf12fe146335812ee1d85bf272ae0c2bbd76faf1ae
%global		module		Vol
Name:		coin-or-%{module}
Summary:        Vol (Volume Algorithm)
Version:	1.5.4
Release:        1%{?dist}
License:	EPL-1.0
URL:		http://projects.coin-or.org/%{module}
Source0:        http://www.coin-or.org/download/pkgsource/%{module}/%{module}-%{version}.tgz
Patch0:		%{name}-docdir.patch
Patch1: coin-or-Vol-configure-c99.patch
# oreon:deps
BuildRequires:  coin-or-Osi-devel
BuildRequires:  coin-or-Osi-doc
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles coin-or-Vol-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles coin-or-Vol-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n coin-or-Vol-devel -f %{oreon_filedir}/coin-or-Vol-devel.list
%files -n coin-or-Vol-doc -f %{oreon_filedir}/coin-or-Vol-doc.list

%changelog

%autochangelog
