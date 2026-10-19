%global source0_hash 98105aff5f78d1dfd66f8e9674b2e465d0bcbcb656b0749291d70b5793861af3
%bcond test_data 0
Name:           spec2nii
Version:        0.8.15
Release:        1%{?dist}
Summary:        Multi-format in vivo MR spectroscopy conversion to NIFTI
License:        BSD-3-Clause
URL:            https://github.com/wtclarke/spec2nii
Source0:        https://github.com/wtclarke/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%if %{with test_data}
%global test_data_url https://git.fmrib.ox.ac.uk/wclarke/spec2nii_test_data
%global test_data_commit 1594c2625a53a877670f9dd0492c0e1b6f3471d5
%global test_data_dir spec2nii_test_data-%{test_data_commit}
Source1:        %{test_data_url}/-/archive/%{test_data_commit}/%{test_data_dir}.tar.bz2
%endif
Source100:      spec2nii.1
Source101:      spec2nii-auto.1
Source102:      spec2nii-twix.1
Source103:      spec2nii-dicom.1
Source104:      spec2nii-rda.1
Source105:      spec2nii-uih.1
Source106:      spec2nii-philips.1
Source107:      spec2nii-philips_dl.1
Source108:      spec2nii-philips_dcm.1
Source109:      spec2nii-ge.1
Source110:      spec2nii-text.1
Source111:      spec2nii-jmrui.1
Source112:      spec2nii-raw.1
Source113:      spec2nii-bruker.1
Source114:      spec2nii-varian.1
Source115:      spec2nii-anon.1
Source116:      spec2nii-dump.1
Source117:      spec2nii-extract.1
Source118:      spec2nii-insert.1
%global debug_package %{nil}
ExcludeArch:    %{ix86}
%ifarch s390x
%endif
%py_provides python3-spec2nii
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-spec2nii = %{version}-%{release}
# /oreon:deps
%package -n       python3-spec2nii+dev
Summary:        Metapackage for python3-spec2nii dev extras
Requires:       python3-spec2nii = %{version}-%{release}
Requires:       python3dist(setuptools-scm) >= 8
Provides:       python3dist(spec2nii[dev]) = %{version}-%{release}

%description -n python3-spec2nii+dev
Metapackage for python3-spec2nii dev extras.

%description
A program for multi-format conversion of in vivo MRS to the NIfTI-MRS format
(https://github.com/wexeee/mrs_nifti_standard).

This program was inspired by the imaging DICOM to NIfTI converter dcm2niix,
developed by Chris Rorden. All MRS(I) orientations are tested with images
converted using dcm2niix.

%prep

%if %{with test_data}
%setup -q -T -D -a 1 -c -n %{name}-%{version}
rmdir tests/spec2nii_test_data
mv %{test_data_dir} tests/spec2nii_test_data
%endif

%ifarch s390x
# PyMapVBVD assumes the platform is little-endian
# https://bugzilla.redhat.com/show_bug.cgi?id=2225518
# Most of the functionality in this package is still available without it, so
# we can remove the dependency and still get a generally usable package.
sed -r -i 's/^([[:blank:]]*)?(-[[:blank:]]+)?(pyMapVBVD)\b/\1# \2\3/' \
    requirements.yml
%endif

%install
%pyproject_install
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE100}' '%{SOURCE101}' '%{SOURCE102}' '%{SOURCE103}' \
    '%{SOURCE104}' '%{SOURCE105}' '%{SOURCE106}' '%{SOURCE107}' \
    '%{SOURCE108}' '%{SOURCE109}' '%{SOURCE110}' '%{SOURCE111}' \
    '%{SOURCE112}' '%{SOURCE113}' '%{SOURCE114}' '%{SOURCE115}' \
    '%{SOURCE116}' '%{SOURCE117}' '%{SOURCE118}'
%oreon_autofiles main

%build

%pyproject_wheel
%check

%if %{with test_data}
k="${k-}${k+ and }not test_fid"
k="${k-}${k+ and }not test_2dseq"
k="${k-}${k+ and }not orientation"
%pytest -k "${k-}" tests -v
%endif
%files

%changelog

%autochangelog
