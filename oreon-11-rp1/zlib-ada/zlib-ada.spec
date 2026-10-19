%global source0_hash 7b2ba39dc662684aa8780f0ce46f880ca3f2d359391a27dee7cee447041159b5
%bcond check 0
%global upstream_name         zlib-ada
%global upstream_version      1.4
%global upstream_commit_date  20210811
%global upstream_commit       ca39312ba02e84eb15799300ef83607a83402868
%global upstream_shortcommit  %(c=%{upstream_commit}; echo ${c:0:7})
Name:           zlib-ada
Version:        %{upstream_version}
Release:        1%{?dist}
Summary:        Zlib for Ada
Summary(sv):    Zlib för ada
License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-3.0-or-later WITH GNAT-exception
URL:            https://zlib-ada.sourceforge.net/
Source0:        https://sourceforge.net/code-snapshots/git/z/zl/%{name}/git.git/%{name}-git-%{upstream_commit}.zip
Source1:        build_zlib_ada.gpr
Source2:        zlib_ada.gpr
Patch:          %{name}-detect-end-of-zlib-stream-better.patch
Patch:          %{name}-properly-initialize-in_last.patch
ExclusiveArch:  %{GPRbuild_arches}
%global common_description_en \
Zlib-Ada is a thick Ada binding to the popular compression/decompression \
library Zlib.
%global common_description_sv \
Zlib-Ada är en tjock adabindning till det populära komprimerings- och \
avkomprimeringsbiblioteket Zlib.
# oreon:deps
BuildRequires:  fedora-gnat-project-common
BuildRequires:  gcc-gnat
BuildRequires:  gprbuild
BuildRequires:  zlib-devel
# /oreon:deps
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
%install
mv build_target/* --target-directory=%{buildroot}
mkdir --parents %{buildroot}%{_GNAT_project_dir}
cp --preserve=timestamps %{SOURCE2} %{buildroot}%{_GNAT_project_dir}/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

sed --in-place \
    --expression="156 { s,Ada.Text_IO.Get_Immediate (Dummy),delay 2.0, ; t; q1 }" \
    mtest.adb
gnatmake test.adb -largs -lz && ./test
gnatmake mtest.adb -largs -lz && ./mtest
%endif
%files -f %{oreon_filedir}/main.list
%files -n zlib-ada-devel -f %{oreon_filedir}/zlib-ada-devel.list

%changelog

%autochangelog
