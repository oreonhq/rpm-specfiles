%global source0_hash e9ef1b681c7c788023631ca13edb342d250cdbfe775f72f2907d7c1d5063ba10
%bcond check 0
%global upstream_owner    AdaCore
%global upstream_name     aunit
%global upstream_version  26.0.0
%global upstream_commit   cb7458f1a7f193e72526cb6bdd1a9a82ccfdd3f7
Name:           aunit
Epoch:          2
Version:        %{upstream_version}
Release:        1%{?dist}
Summary:        A unit testing framework for Ada
License:        GPL-3.0-or-later WITH GCC-exception-3.1
URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source0:        https://github.com/%{upstream_owner}/%{name}/archive/%{upstream_commit}.tar.gz#/%{name}-%{version}.tar.gz
Patch:          %{name}-disable-static.patch
Patch:          %{name}-fix-doc-build-path.patch
Patch:          %{name}-cb-examples-dir.patch
%if %{with check}
%endif
ExclusiveArch:  %{GPRbuild_arches}
%global common_description_en \
This is the Ada unit test framework AUnit, derived from the JUnit/CPPUnit \
frameworks for Java/C++.
# oreon:deps
BuildRequires:  diffutils
BuildRequires:  dos2unix
BuildRequires:  fedora-gnat-project-common
BuildRequires:  findutils
BuildRequires:  gcc-gnat
BuildRequires:  gprbuild
BuildRequires:  grep
BuildRequires:  make
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-latex
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  sed
BuildRequires:  tex(titleref.sty)
# /oreon:deps
%description %{common_description_en}

#################
## Subpackages ##
#################

%package devel
Summary:        Development files for AUnit
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common
Recommends:     %{name}-doc
%description devel %{common_description_en}

This package contains source code and linking information for developing
applications that use AUnit.

%package doc
Summary:        Documentation for AUnit
BuildArch:      noarch
License:        GFDL-1.3-no-invariants-or-later AND MIT AND BSD-2-Clause AND GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)
%description doc %{common_description_en}

This package contains the documentation in HTML and PDF, and some examples.

#############
## Prepare ##
#############

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstream_name}-%{upstream_commit}

# Version information in this file is used during the build.
echo '%{version}' > ./version_information

# Convert the line-endings in some GNAT project files.
find ./examples -name '*.gpr' -print0 \
    | xargs -0 dos2unix -ic0 \
    | xargs -0 dos2unix --keepdate

# One of the tests in the test suite fails because of a runtime accessibility
# check on line 101 of file `aunit-simple_test_cases.adb`. A workaround is to
# replace all runtime checks for anonymous access types with compile-time checks
# based on the "designated type model" (-gnatd_b). See also:
#
#   - https://github.com/AdaCore/aunit/issues/55
#   - https://blog.adacore.com/going-beyond-ada-2022

# Disable dynamic accessibility checks related to anonymous access types.
cat << EOF > gnat.adc
pragma Restrictions (No_Dynamic_Accessibility_Checks);
EOF

###########
## Build ##
###########

%build

%global GPRbuild_adc_flags -cargs -gnatec=gnat.adc -gnatd_b -gargs
gprbuild %{GPRbuild_flags} %{GPRbuild_adc_flags} \
         -XVERSION=%{version} -P lib/gnat/aunit.gpr
make -C doc html-all pdf-all
%install
%{GPRinstall} --no-build-var -XVERSION=%{version} -P lib/gnat/aunit.gpr
ln --symbolic --force lib%{name}.so.%{version} %{buildroot}%{_libdir}/lib%{name}.so
mv --no-target-directory \
   %{buildroot}%{_datadir}/examples/%{name} \
   %{buildroot}%{_pkgdocdir}/examples
rmdir %{buildroot}%{_datadir}/examples
rm -r  %{buildroot}%{_pkgdocdir}/pdf/_static
find %{buildroot}%{_pkgdocdir}/pdf/ -type f -not -name 'aunit_cb.pdf' -delete
%if %{with check}
%global checkroot %{_builddir}/%{name}-%{version}/checkroot
mkdir %{checkroot}  # without --parents to not clobber any upstream directory
cp --recursive %{buildroot}/* %{checkroot}/
%endif
sed --regexp-extended --in-place \
    '--expression=1i with "directories";' \
    '--expression=/^--  This project has been generated/d' \
    '--expression=/package Linker is/,/end Linker/d' \
    '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/'%{name}'");|i' \
    '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
    '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/'%{name}'";|i' \
    %{buildroot}%{_GNAT_project_dir}/%{name}*.gpr
%oreon_autofiles aunit-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles aunit-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

export PATH=%{checkroot}%{_bindir}:$PATH
export LD_LIBRARY_PATH=%{checkroot}%{_libdir}:$LD_LIBRARY_PATH
export GPR_PROJECT_PATH=%{checkroot}%{_GNAT_project_dir}:$GPR_PROJECT_PATH
make -C test || { cat test/test.out.full >&2 ; false ; }
%endif
%files -f %{oreon_filedir}/main.list
%files -n aunit-devel -f %{oreon_filedir}/aunit-devel.list
%files -n aunit-doc -f %{oreon_filedir}/aunit-doc.list

%changelog

%autochangelog
