%global source0_hash 7f422096b40498b1389093955825f141bb67ed6014249d884009463dc7846879
Name:           ffcall
Version:        2.5
Release:        1%{?dist}
Summary:        Libraries for foreign function call interfaces
License:        GPL-2.0-or-later
URL:            https://www.gnu.org/software/libffcall/
VCS:            git:https://git.savannah.gnu.org/git/libffcall.git
Source0:        https://ftp.gnu.org/gnu/libffcall/lib%{name}-%{version}.tar.gz
Patch:          configure.patch
Patch:          %{name}-ppc64le.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnulib-devel
BuildRequires:  make
# /oreon:deps
%description
This is a collection of four libraries which can be used to build foreign
function call interfaces in embedded interpreters.  The four packages are:
 - avcall: calling C functions with variable arguments
 - vacall: C functions accepting variable argument prototypes
 - trampoline: closures as first-class C functions
 - callback: closures with variable arguments as first-class C functions (a
   reentrant combination of vacall and trampoline)

%package devel
Summary:        Files needed to develop programs with %{name}
License:        GPL-2.0-or-later AND (GPL-2.0-or-later OR GFDL-1.2-no-invariants-or-later)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Files needed to develop programs with %{name}.

%package static
Summary:        Static libraries for foreign function call interfaces
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%description static
Static libraries for foreign function call interfaces.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir lib%{name}-%{version}
%oreon_prep
%build

%configure
make # %{?_smp_mflags}
%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}
%make_install
rm -fr $RPM_BUILD_ROOT%{_datadir}/html
chmod a+x $RPM_BUILD_ROOT%{_libdir}/lib*.so.*
pushd $RPM_BUILD_ROOT%{_mandir}/man3
for page in *; do
  mv $page %{name}-$page
done
popd
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ffcall-devel -f %{oreon_filedir}/ffcall-devel.list
%files -n ffcall-static -f %{oreon_filedir}/ffcall-static.list

%changelog

%autochangelog
