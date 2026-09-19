%global source0_hash 06579d1721483ef9a77ad56994b5a346288bed3972f2e072dc97a9921d535a2f

%global real_name DICOMAnonymizer
%global forgeurl https://github.com/mmiv-center/%{real_name}
%global commit f0762643caab3d84e522b99cdec4b8d271b12039
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20210920

# debugsourcefiles.list is empty
%global debug_package %{nil}

Name:    dicomanonymizer
Version: 1

Release: 0.20.%{gitdate}git%{shortcommit}%{dist}
Summary: A multi-threaded anonymizer for DICOM files

%forgemeta

License: Unlicense and MIT
URL:     %{forgeurl}
Source:  %{forgesource}

# https://github.com/mmiv-center/DICOMAnonymizer/issues/3
Patch0: 0001-use-system-gdcm.patch
# https://github.com/mmiv-center/DICOMAnonymizer/issues/14
Patch1: 0002-timeval.patch

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: make
BuildRequires: gdcm-devel
BuildRequires: zlib-devel
BuildRequires: libxml2-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libxslt-devel

%description
A multi-threaded anonymizer for DICOM files implementing most of DICOM PS 3.15
AnnexE. Entries such as uid entries are replaced with hash values. This ensures
that partial runs of a studies DICOM files can be merged afterwards. This
project is written in C++ using the gdcm library and multiple threads to
accelerate processing. Warning: The operation performed by this tool is a 'soft'
de-identification. Instead of a white list of allowed tags the tool keeps a list
of tags known to frequently contain personal identifying information (PII) and
replaces only those. On the command line you specify a patient identifier
(PatientID/PatientName). Only if you do not keep a mapping of the new and the
old identifier this is considered an anonymization. If such a list exists the
operation performed is a de-identification (permits a later re-identification).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{real_name}-%{commit}

%build
%cmake -DCMAKE_EXE_LINKER_FLAGS="%{optflags} -fPIE"
%cmake_build

%install
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 %{_vpath_builddir}/anonymize %{buildroot}%{_bindir}/dicomanonymize

%files
%license LICENSE
%doc README.md
%{_bindir}/dicomanonymize

%changelog
%autochangelog
