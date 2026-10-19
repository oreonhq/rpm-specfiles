%global source1_hash 5dafec078151018da7aaf3c941bd31f246f590bc34fa3fef29ce77a773db16a6
%global source0_hash 868b611b5f8a3a73809436c9072db50db4975615905f0bd5fb7b1432e6d24b37
%bcond tests 1
%global forgeurl  https://github.com/NIFTI-Imaging/nifti_clib/
Name:           nifticlib
Version:        3.0.1
Release:        1%{?dist}
Summary:        A set of i/o libraries for reading and writing files in the nifti-1 data format
%forgemeta
License:        LicenseRef-Fedora-Public-Domain
URL:            %forgeurl
Source0:        %{forgeurl}archive/v%{version}/nifti_clib-%{version}.tar.gz
Source1:        https://github.com/NIFTI-Imaging/nifti-test-data/archive/v3.0.2.tar.gz
Patch:          0001-dont-get-version-from-git.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  patch
BuildRequires:  zlib-devel
# /oreon:deps
%description
Nifticlib is a set of C i/o libraries for reading and writing files in
the nifti-1 data format. nifti-1 is a binary file format for storing
medical image data, e.g. magnetic resonance image (MRI) and functional
MRI (fMRI) brain images.

%package devel
Summary: Libraries and header files for nifticlib development
Requires: %{name} = %{version}-%{release}
%description devel
The nifticlib-devel package contains the header files and libraries
necessary for developing programs that make use of the nifticlib library.

%package docs
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch:  noarch
%description docs
The package contains documentation and example files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -S patch

# remove hidden file that's installed
rm -fv ./real_easy/parent_project_demo/.gitignore

%build

%cmake \
    -DGIT_REPO_VERSION:STRING="%{version}" \
    -DBUILD_SHARED_LIBS=ON \
    -DNIFTI_BUILD_APPLICATIONS=ON \
    -DNIFTI_BUILD_TESTING=ON \
    -DNIFTI_INSTALL_NO_DOCS=OFF \
    -DBUILD_TESTING=ON \
    -DDOWNLOAD_TEST_DATA=OFF \
    -DUSE_NIFTI2_CODE=ON \
    -DUSE_CIFTI_CODE=ON \
    -DUSE_FSL_CODE=OFF \
    -DNIFTI_INSTALL_LIBRARY_DIR=%{_lib} \
    -DNIFTI_INSTALL_DOC_DIR=%{_docdir}/%{name}/ \
    -Dfetch_testing_data_SOURCE_DIR:PATH=%{_builddir}/nifti-test-data-3.0.2 \
    .
%cmake_build
%install
rm -rf $RPM_BUILD_ROOT
%cmake_install
pushd $RPM_BUILD_ROOT/%{_mandir}/man1/
for f in nifti*
do
    chmod 0644 $f
    rename "_manpage" "" $f
done
ls -lash
popd
pushd $RPM_BUILD_ROOT/%{_datadir}/cmake/NIFTI/
for f in ./NIFTI*.cmake
do
    echo "*** $f ***"
    cat "$f"
done
popd
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
pushd %{_builddir}/
    %__rpmuncompress -x %SOURCE1
popd
export PATH=$PATH:$RPM_BUILD_ROOT/%{_bindir}
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$RPM_BUILD_ROOT/%{_libdir}/
%ctest --output-on-failure
%endif
%files -f %{oreon_filedir}/main.list
%files -n nifticlib-devel -f %{oreon_filedir}/nifticlib-devel.list
%files -n nifticlib-docs -f %{oreon_filedir}/nifticlib-docs.list

%changelog

%autochangelog
