%global source0_hash 1cf833257a9a849bbb880228565aafc625a842999c3ff322f34f0b352892798b
%global		module		DyLP
Name:		coin-or-%{module}
Summary:        Implementation of the dynamic simplex algorithm
Version:	1.10.4
Release:        1%{?dist}
License:	EPL-1.0
URL:		https://projects.coin-or.org/%{module}
Source0:        http://www.coin-or.org/download/pkgsource/%{module}/%{module}-%{version}.tgz
Patch0:		%{name}-docdir.patch
Patch1:		%{name}-seqpoint.patch
Patch2:		%{name}-configure-c99.patch
Patch3:		%{name}-isfinite.patch
Patch4:		%{name}-math-macros.patch
Patch5:           %{name}-fix_GCC15.patch
# oreon:deps
BuildRequires:  coin-or-Data-Netlib
BuildRequires:  coin-or-Osi-devel
BuildRequires:  coin-or-Osi-doc
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
DyLP is an implementation of the dynamic simplex algorithm. Briefly, dynamic
simplex attempts to work with an active constraint system which is a subset
of the full constraint system. It alternates between primal and dual simplex
phases. Between simplex phases, it deactivates variables and constraints
which are not currently useful, and scans the full constraint system to
activate variables and constraints which have become useful.

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

# Set the path to the error text message file
sed -i 's,\(DYLP_ERRMSGDIR=\).\$abs_source_dir.*,\1"%{_datadir}/coin/",' \
    configure

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
rm -f %{buildroot}%{_docdir}/%{name}/{LICENSE,dylp_addlibs.txt}
cp -a doxydoc/{html,*.tag} %{buildroot}%{_docdir}/%{name}
sed -i 's/ -lm//' %{buildroot}%{_libdir}/pkgconfig/dylp.pc
mkdir -p %{buildroot}%{_datadir}/coin
cp -p src/Dylp/dy_errmsgs.txt %{buildroot}%{_datadir}/coin
%oreon_autofiles coin-or-DyLP-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles coin-or-DyLP-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test DYLP_ERRMSGDIR=$PWD/src/Dylp/
%files -f %{oreon_filedir}/main.list
%files -n coin-or-DyLP-devel -f %{oreon_filedir}/coin-or-DyLP-devel.list
%files -n coin-or-DyLP-doc -f %{oreon_filedir}/coin-or-DyLP-doc.list

%changelog

%autochangelog
