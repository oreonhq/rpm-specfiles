%global source0_hash 2d9608fc303d5ecc3f451c8a658057526f3a70f9e84659be13ed16938425dace

%bcond check 0

%global forgeurl https://github.com/pydicom/pynetdicom

%global _description %{expand:
pynetdicom is a pure Python package that implements the DICOM
networking protocol. Working with pydicom, it allows the easy creation of 
DICOM Service Class Users (SCUs) and Service Class Providers (SCPs).}

Name:           python-pynetdicom
Version:        3.0.4

%forgemeta

Release:        1%{?dist}
Summary:        A Python implementation of the DICOM networking protocol

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

# Downstream-only: remove the upper bound on the version of pydicom,
# specifically allowing version 3. Upstream is also working toward a release
# with pydicom 3 support; see the comment in
# https://github.com/pydicom/pynetdicom/pull/965.
# Patch:          pynetdicom-2.1.1-pydicom-3.patch

BuildArch:      noarch

BuildRequires:  python3-devel

# Test dependencies; see the test extra in pyproject.toml, which also has
# unwanted coverage-analysis dependencies.
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pyfakefs}
# (Also required to import some modules for “smoke tests”)
BuildRequires:  %{py3_dist sqlalchemy}
# Otherwise, pydicom test data would have to be downloaded.
BuildRequires:  %{py3_dist pydicom-data}

%description %_description

%package -n python3-pynetdicom
Summary:        %{summary}

%description -n python3-pynetdicom %_description

%package -n python3-pynetdicom-utils
Summary:        Some commands based on pynetdicom
Conflicts:      dcmtk
Requires:       python3-pynetdicom = %{version}-%{release}

%description -n python3-pynetdicom-utils
Some commands based on pynetdicom

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1
%py3_shebang_fix .

# allow newer poetry-core
sed -i "s/poetry-core >=1.8,<2/poetry-core >=1.8,<3/" pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L pynetdicom
# pynetdicom 2.1.1 installs LICENSE file into site-packages/
# https://github.com/pydicom/pynetdicom/issues/966
# this file is wrongly copied with poetry-core<2
rm -f %{buildroot}%{python3_sitelib}/LICENCE

# Remove commands already provided by dcmtk with the same name
# https://github.com/pydicom/pynetdicom/issues/968
# rm -rf %{buildroot}%{_bindir}

%check
%{pyproject_check_import \
    -e 'pynetdicom.tests*' \
    -e 'pynetdicom.apps.tests*' \
    -e 'pynetdicom.benchmarks*'}
%if %{with check}
# tests in the apps/ part not reliable, upstream advice to disable them
# https://github.com/pydicom/pynetdicom/issues/498
ignore="${ignore-} --deselect=pynetdicom/apps/tests"

# TODO: Why does this fail (even without pydicom 3.0.0)?
# >       assert self.fsm._changes[:5] == [
#             ("Sta1", "Evt1", "AE-1"),
#             ("Sta4", "Evt2", "AE-2"),
#             ("Sta5", "Evt3", "AE-3"),
#             ("Sta6", "Evt12", "AR-2"),
#             ("Sta8", "Evt16", "AA-3"),
#         ]
# E       AssertionError: assert [('Sta1', 'Evt1', 'AE-1'), ('Sta4', 'Evt2',
#         'AE-2'), ('Sta5', 'Evt3', 'AE-3'), ('Sta6', 'Evt12', 'AR-2')] ==
#         [('Sta1', 'Evt1', 'AE-1'), ('Sta4', 'Evt2', 'AE-2'), ('Sta5', 'Evt3',
#         'AE-3'), ('Sta6', 'Evt12', 'AR-2'), ('Sta8', 'Evt16', 'AA-3')]
# E
# E         Right contains one more item: ('Sta8', 'Evt16', 'AA-3')
k="${k-}${k+ and }not (TestState08 and test_evt16)"

# This fails with pydicom 3.0.0 because a deprecation warning replaces the
# expected output.
# >       assert (
#             "'dataset' is encoded as implicit VR little endian but the file "
#             "meta has a (0002,0010) Transfer Syntax UID of 'Explicit VR "
#             "Little Endian' - using 'Implicit VR Little Endian' instead"
#         ) in caplog.text
# E       assert "'dataset' is encoded as implicit VR little endian but the
#         file meta has a (0002,0010) Transfer Syntax UID of 'Explicit VR
#         Little Endian' - using 'Implicit VR Little Endian' instead" in
#         "WARNING pydicom:misc.py:82 'FileDataset.is_implicit_VR' will be
#         removed in v4.0, set the Transfer Syntax UID or use the 'implicit_vr'
#         argument with FileDataset.save_as() or dcmwrite() instead\nWARNING
#         pydicom:misc.py:82 'FileDataset.is_implicit_VR' will be removed in
#         v4.0, set the Transfer Syntax UID or use the 'implicit_vr' argument
#         with FileDataset.save_as() or dcmwrite() instead\nWARNING
#         pydicom:misc.py:82 'FileDataset.is_little_endian' will be removed in
#         v4.0, set the Transfer Syntax UID or use the 'little_endian' argument
#         with FileDataset.save_as() or dcmwrite() instead\nWARNING
#         pydicom:misc.py:82 'FileDataset.is_implicit_VR' will be removed in
#         v4.0, set the Transfer Syntax UID or use the 'implicit_vr' argument
#         with FileDataset.save_as() or dcmwrite() instead\nWARNING
#         pydicom:misc.py:82 'FileDataset.is_little_endian' will be removed in
#         v4.0, set the Transfer Syntax UID or use the 'little_endian' argument
#         with FileDataset.save_as() or dcmwrite() instead\n"
k="${k-}${k+ and }not (TestAssociationSendCStore and test_dataset_encoding_mismatch)"

# These fail with pydicom 3.0.0 due to differences in pretty-printed output, e.g.:
# _______________________ TestPrettyElement.test_seq_empty _______________________
#
# self = <pynetdicom.tests.test_dsutils.TestPrettyElement object at 0x7fc97b245270>
#
#     def test_seq_empty(self):
#         """Test empty sequence"""
#         ds = Dataset()
#         ds.EventCodeSequence = []
# >       assert (
#             "(0008,2135) SQ (Sequence with 0 items)                  # 0"
#             " EventCodeSequence"
#         ) == pretty_element(ds["EventCodeSequence"])
# E       AssertionError: assert '(0008,2135) SQ (Sequence with 0 items)                  # 0 EventCodeSequence' == '(0008,2135) SQ (Sequence with 0 item)                   # 1 EventCodeSequence'
# E
# E         - (0008,2135) SQ (Sequence with 0 item)                   # 1 EventCodeSequence
# E         ?                                                        -  ^
# E         + (0008,2135) SQ (Sequence with 0 items)                  # 0 EventCodeSequence
# E         ?                                     +                     ^
#
# pynetdicom/tests/test_dsutils.py:424: AssertionError
k="${k-}${k+ and }not (TestPrettyElement and test_seq_empty)"
k="${k-}${k+ and }not (TestPrettyElement and test_seq_vm_multi)"
k="${k-}${k+ and }not (TestPrettyDataset and test_sequence_empty)"
k="${k-}${k+ and }not (TestPrettyDataset and test_sequence_multi)"

%pytest ${ignore-} -k "${k-}" -rs -vv
%else
%endif

%files -n python3-pynetdicom -f %{pyproject_files}
%license LICENCE
%doc README.rst

%files -n python3-pynetdicom-utils
# No separate LICENSE file needed, since this depends on python3-pynetdicom
%{_bindir}/echoscp
%{_bindir}/echoscu
%{_bindir}/findscu
%{_bindir}/getscu
%{_bindir}/movescu
%{_bindir}/qrscp
%{_bindir}/storescp
%{_bindir}/storescu

%changelog
%autochangelog
