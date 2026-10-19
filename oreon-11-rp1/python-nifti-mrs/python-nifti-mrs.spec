%global source0_hash 81847f4e450cb09d14851ec418513554277e7f5b541a128fe9d87dc3a52d8ef8
%bcond doc %{defined fc42}
%global std_version 0.10
Name:           python-nifti-mrs
Version:        1.4.1
Release:        1%{?dist}
Summary:        Software tools for the NIfTI-MRS data format
License:        BSD-3-Clause AND Unlicense AND CC-BY-4.0
URL:            https://github.com/wtclarke/nifti_mrs_tools
Source0:        https://github.com/wtclarke/nifti_mrs_tools/archive/%{version}/nifti_mrs_tools-%{version}.tar.gz
%global std_url https://github.com/wtclarke/mrs_nifti_standard
Source1:        %{std_url}/archive/v%{std_version}/mrs_nifti_standard-%{std_version}.tar.gz
Source10:       mrs_tools.1
Source11:       mrs_tools-conjugate.1
Source12:       mrs_tools-info.1
Source13:       mrs_tools-merge.1
Source14:       mrs_tools-reorder.1
Source15:       mrs_tools-reshape.1
Source16:       mrs_tools-split.1
Source17:       mrs_tools-vis.1
%global debug_package %{nil}
ExcludeArch:    %{ix86}
%if %{with doc}
%endif
%global common_description %{expand:
This package contains python-based tools for representing, validating, and
manipulating the NIfTI-MRS format. NIfTI-MRS is a standardized format for
storing Magnetic Resonance Spectroscopy data.
These tools are used extensively in the spec2nii format conversion program and
the FSL-MRS analysis software. However, this library can also be used as a
stand-alone set of tools.
If you use these tools please cite: Clarke, WT, Bell, TK, Emir, UE, et al.
NIfTI-MRS: A standard data format for magnetic resonance spectroscopy. Magn
Reson Med. 2022; 88: 2358- 2370. doi:10.1002/mrm.29418}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-nifti-mrs = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n     python3-nifti-mrs
Summary:        Software tools for the NIfTI-MRS data format
License:        BSD-3-Clause AND Unlicense
BuildArch:      noarch
%py_provides python3-mrs-tools
Provides:       bundled(mrs_nifti_standard) = %{std_version}
Provides:       mrs_tools = %{version}-%{release}
Obsoletes:      mrs_tools < 1.3.0-3
%if %{without doc}
Obsoletes:      python-nifti-mrs-doc < 1.3.3-5
%endif
%description -n python3-nifti-mrs %{common_description}

# We don’t generate a metapackage for the “VIS” extra because it requires
# fsl-mrs, which (1) is not packaged, (2) is not on PyPI, (3) is non-free
# (non-commercial use only).

%if %{with doc}
%package        doc
Summary:        Documentation for python-nifti-mrs
License:        BSD-3-Clause
BuildArch:      noarch
%description    doc %{common_description}
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n nifti_mrs_tools-%{version}
%setup -q -T -D -b 1 -n nifti_mrs_tools-%{version}
# Upstream uses a git submodule. Since "exclude src/nifti_mrs/standard/*/*"
# appears in MANIFEST.in, which means only top-level contents of the submodule
# appear in the sdist, we imitate this with the find command.
find ../mrs_nifti_standard-%{std_version} -mindepth 1 -maxdepth 1 -type f \
    -exec ln '{}' src/nifti_mrs/standard/ ';'
# We do also want to package a copy of the license text for the standard.
ln ../mrs_nifti_standard-%{std_version}/LICENSE LICENSE-mrs_nifti_standard

%build

%pyproject_wheel
%if %{with doc}
PYTHONPATH="${PWD}/src" %make_build -C apidoc latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C apidoc/_build/latex LATEXMKOPTS='-quiet'
%endif
%install
%pyproject_install
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}' '%{SOURCE13}' '%{SOURCE14}' \
    '%{SOURCE15}' '%{SOURCE16}' '%{SOURCE17}'
%oreon_autofiles python3-nifti-mrs usr/lib/python3*/site-packages/nifti_mrs* usr/lib64/python3*/site-packages/nifti_mrs* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/nifti_mrs* usr/lib64/python3*/site-packages/nifti_mrs* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ifarch s390x
k="${k-}${k+ and }not test_nifti_mrs_save"
k="${k-}${k+ and }not test_merge"
k="${k-}${k+ and }not test_split"
k="${k-}${k+ and }not test_reorder"
k="${k-}${k+ and }not test_reshape"
k="${k-}${k+ and }not test_conjugate"
%endif
m="${m-}${m+ and }not with_fsl_mrs"
%pytest -k "${k-}" -m "${m-}" -v
%files
%files -n python3-nifti-mrs -f %{oreon_filedir}/python3-nifti-mrs.list
%files -n python-nifti-mrs-doc -f %{oreon_filedir}/python-nifti-mrs-doc.list

%changelog

%autochangelog
