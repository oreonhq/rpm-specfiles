%global source0_hash 7b2ba39dc662684aa8780f0ce46f880ca3f2d359391a27dee7cee447041159b5

# The test suite is normally run. It can be disabled with "--without=check".
%bcond check 0

# Upstream source information.
%global upstream_name         zlib-ada
%global upstream_version      1.4
%global upstream_commit_date  20210811
%global upstream_commit       ca39312ba02e84eb15799300ef83607a83402868
%global upstream_shortcommit  %(c=%{upstream_commit}; echo ${c:0:7})

Name:           zlib-ada
Version:        %{upstream_version}
Release:        0.44.%{upstream_commit_date}git%{upstream_shortcommit}%{?dist}
Summary:        Zlib for Ada
Summary(sv):    Zlib för ada

License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-3.0-or-later WITH GNAT-exception
# Based on the header of zlib.ads.

URL:            https://zlib-ada.sourceforge.net/
Source0:        https://sourceforge.net/code-snapshots/git/z/zl/%{upstream_name}/git.git/%{upstream_name}-git-%{upstream_commit}.zip

# NOTE: The above link points to a source package that is generated on
# demand by opening the source code page in a browser (see [Code] below),
# selecting the correct commit and then clicking "Download Snapshot". The
# generated Zip-file will remain available at the mentioned location for some
# time (at most 24h, as it seems).
#
# See also:
#   [Code]     https://sourceforge.net/p/zlib-ada/git/ci/master/tree/
#   [Releases] https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

Source1:        build_zlib_ada.gpr
Source2:        zlib_ada.gpr

# The Ada Web Server bundles the Zlib-Ada library. The authors of the
# Ada Web Server found that a previous fix in the upstream source of
# Zlib-Ada did not solve all problems in the end-of-stream detection
# and therefore made additional improvements, but only in the bundled
# sources. The improvements have, for some reason, not been offered
# to/integrated into the upstream repository of Zlib-Ada on
# SourceForge. Tests have been added to the AWS test suite that
# explicitly test for the bug(s). As the Ada Web Server is packaged in
# Fedora (package "aws"), we apply these patches here as well.

# Adapted from: https://github.com/AdaCore/aws/commit/178767546df544388bb8a921d8314957b88a6ae0
Patch:          %{name}-detect-end-of-zlib-stream-better.patch
# Adapted from: https://github.com/AdaCore/aws/commit/76ae4648ee0e8c38e92b0ee71ae60db259ff27ce
Patch:          %{name}-properly-initialize-in_last.patch

BuildRequires:  gcc-gnat
# A fedora-gnat-project-common that contains GPRbuild_flags is needed.
BuildRequires:  fedora-gnat-project-common >= 3.17
BuildRequires:  gprbuild
BuildRequires:  zlib-devel

# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

%global common_description_en \
Zlib-Ada is a thick Ada binding to the popular compression/decompression \
library Zlib.

%global common_description_sv \
Zlib-Ada är en tjock adabindning till det populära komprimerings- och \
avkomprimeringsbiblioteket Zlib.

%description %{common_description_en}

%description -l sv %{common_description_sv}

#################
## Subpackages ##
#################

%package devel
Summary:        Development files for Zlib-Ada
Summary(sv):    Filer för programmering med Zlib-Ada
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fedora-gnat-project-common

%description devel %{common_description_en}

The %{name}-devel package contains source code and linking information for
developing applications that use Zlib-Ada.

%description devel -l sv %{common_description_sv}

Paketet %{name}-devel innehåller källkod och länkningsinformation som behövs
för att utveckla program som använder Zlib-Ada.

#############
## Prepare ##
#############

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{upstream_name}-git-%{upstream_commit}

# Remove bogus executable bits.
chmod a-x *

# Copy the GPRbuild-file with which we will build the library.
cp %{SOURCE1} .

###########
## Build ##
###########

%build
gprbuild %{GPRbuild_flags} -XVERSION=%{upstream_commit_date} \
         -XDESTDIR=build_target \
         -P build_zlib_ada.gpr

#############
## Install ##
#############

%install
mv build_target/* --target-directory=%{buildroot}

# Add the project file for projects that use this library.
mkdir --parents %{buildroot}%{_GNAT_project_dir}
cp --preserve=timestamps %{SOURCE2} %{buildroot}%{_GNAT_project_dir}/

###########
## Check ##
###########

%if %{with check}
%check

# Let the multithreading test run for a limited amount of time.
sed --in-place \
    --expression="156 { s,Ada.Text_IO.Get_Immediate (Dummy),delay 2.0, ; t; q1 }" \
    mtest.adb

# Build & run the tests.
gnatmake test.adb -largs -lz && ./test
gnatmake mtest.adb -largs -lz && ./mtest

%endif

###########
## Files ##
###########

%files
%doc readme.txt
%license COPYING3 COPYING.RUNTIME
%{_libdir}/*.so.*

%files devel
%doc test.adb mtest.adb read.adb buffer_demo.adb
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/zlib-ada
%{_GNAT_project_dir}/*

###############
## Changelog ##
###############

%changelog
%autochangelog
