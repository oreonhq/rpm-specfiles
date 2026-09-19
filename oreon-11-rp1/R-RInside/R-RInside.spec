%global source0_hash 0703843a3f1460c571650138e5846d96552d6541766c7df72c609cd3aaca1f24

Name:           R-RInside
Version:        0.2.19
Release:        %autorelease
Summary:        C++ Classes to Embed R in C++ (and C) Applications

License:        GPL-2.0-or-later
URL:            https://cran.r-project.org/package=RInside
Source0:        https://cran.r-project.org/src/contrib/RInside_%{version}.tar.gz
# Adapt RInsideLdFlags function to Fedora packaging (no static
# library, shared library moved to default library path)
Patch:          %{name}-LdFlags.patch

BuildRequires:  R-devel
Requires:       R-core-devel%{?_isa}
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-devel%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-devel <= 0.2.19

%description
The RInside packages makes it easier to have "R inside" your C++
application by providing a C++ wrapper class providing the R
interpreter.

%package examples
Summary:        RInside Examples
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description examples
Numerous examples are provided in the nine sub-directories of the
examples directory of the installed package: standard, mpi (for
parallel computing), qt (showing how to embed RInside inside a Qt GUI
application), wt (showing how to build a "web-application" using the
Wt toolkit), armadillo (for RInside use with RcppArmadillo), eigen
(for RInside use with RcppEigen) and 'c_interface' for a basic C
interface and 'Ruby' illustration.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c -p0

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install

rm %{buildroot}%{_R_libdir}/RInside/lib/libRInside.a
mv %{buildroot}%{_R_libdir}/RInside/lib/libRInside.so %{buildroot}%{_libdir}
rmdir %{buildroot}%{_R_libdir}/RInside/lib

%R_save_files
grep -v examples %{R_files} > %{R_files}.main
grep examples %{R_files} > %{R_files}.examples

%check
%R_check

%files -f %{R_files}.main
%{_libdir}/libRInside.so

%files examples -f %{R_files}.examples

%changelog
%autochangelog
