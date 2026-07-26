%global source0_hash 868b611b5f8a3a73809436c9072db50db4975615905f0bd5fb7b1432e6d24b37

%bcond tests 1

%global forgeurl  https://github.com/NIFTI-Imaging/nifti_clib/

Name:           nifticlib
Version:        3.0.1
Release:        %autorelease
Summary:        A set of i/o libraries for reading and writing files in the nifti-1 data format
%forgemeta

License:        LicenseRef-Fedora-Public-Domain
URL:            %forgeurl
Source0:        %forgesource
# test data
Source1:        https://github.com/NIFTI-Imaging/nifti-test-data/archive/v3.0.2.tar.gz

# Stop CMake from trying to get a version from the `git describe` etc. commands
# We set it manually.
Patch:          0001-dont-get-version-from-git.patch

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  expat-devel
BuildRequires:  gcc gcc-c++
BuildRequires:  help2man
BuildRequires:  patch
BuildRequires:  zlib-devel

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
# check man pages
ls -lash
popd

# check cmake config
pushd $RPM_BUILD_ROOT/%{_datadir}/cmake/NIFTI/
for f in ./NIFTI*.cmake
do
    echo "*** $f ***"
    cat "$f"
done
popd

%check
%if %{with tests}

# extract test data
pushd %{_builddir}/
    %__rpmuncompress -x %SOURCE1
popd

export PATH=$PATH:$RPM_BUILD_ROOT/%{_bindir}
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$RPM_BUILD_ROOT/%{_libdir}/

# use -VV -j1 to debug in case of failures
%ctest --output-on-failure
%endif

%files
%doc README.md
%license LICENSE
%{_libdir}/libnifti2.so.2
%{_libdir}/libnifti2.so.2.1.0
%{_libdir}/libnifticdf.so.2
%{_libdir}/libnifticdf.so.2.1.0
%{_libdir}/libniftiio.so.2
%{_libdir}/libniftiio.so.2.1.0
%{_libdir}/libznz.so.3
%{_libdir}/libznz.so.3.0.0

%{_bindir}/afni_xml_tool
%{_bindir}/cifti_tool
%{_bindir}/nifti1_tool
%{_bindir}/nifti_stats
%{_bindir}/nifti_tool

%{_mandir}/man1/*.gz

%files devel
%{_libdir}/libcifti.so
%{_libdir}/libnifti2.so
%{_libdir}/libnifticdf.so
%{_libdir}/libniftiio.so
%{_libdir}/libznz.so
%{_includedir}/nifti/
%{_datadir}/cmake/NIFTI/

%files docs
%{_docdir}/%{name}

%changelog
%autochangelog
