%global source0_hash cb89a553ee202b0a941605072a857102376ae44b0ccd225e4fa0e0e0b9708bf0
Name:           alglib
Version:        4.08.0.solver
Release:        1%{?dist}
Summary:        A numerical analysis and data processing library
License:        GPL-2.0-or-later
URL:            http://www.alglib.net/
Source0:        http://www.alglib.net/translator/re/%{name}-%{version}.cpp.gpl.tgz
Source1:        CMakeLists.txt
Source2:        bsd.txt
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
ALGLIB is a cross-platform numerical analysis and data processing library.
ALGLIB features include:
 - Data analysis (classification/regression, including neural networks)
 - Optimization and nonlinear solvers
 - Interpolation and linear/nonlinear least-squares fitting
 - Linear algebra (direct algorithms, EVD/SVD), direct and iterative linear
   solvers, Fast Fourier Transform and many other algorithms (numerical
   integration, ODEs, statistics, special functions)

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        API documentation for %{name}
License:        ALGLIB-Documentation
BuildArch:      noarch
%description    doc
The %{name}-doc package contains the %{name} API documentation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-cpp
cp %{SOURCE1} .
cp %{SOURCE2} .

# Fix permissions and line endings
find -type f -exec chmod 0644 {} \;
sed -i 's|\r||g' manual.cpp.html

%build

%cmake -DALGLIB_VERSION=%{version}
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
