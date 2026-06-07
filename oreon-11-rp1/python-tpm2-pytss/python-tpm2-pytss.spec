%global source0_hash none

%global pypi_name tpm2-pytss
%global _name tpm2_pytss

Name:           python-%{pypi_name}
Version:        2.3.0
Release:        10%{?dist}
Summary:        TPM 2.0 TSS Bindings for Python

License:        BSD-2-Clause
URL:            https://github.com/tpm2-software/tpm2-pytss
Source:         %{pypi_source %{pypi_name}}
# https://github.com/tpm2-software/tpm2-pytss/pull/585
Patch1:         %{name}-2.3.0-secp192.patch
# https://github.com/tpm2-software/tpm2-pytss/pull/589
Patch2:         %{name}-bsd.patch
# https://github.com/tpm2-software/tpm2-pytss/pull/615
Patch3:         %{name}-gcc15.patch
# cryptograpy: add copy/deepcopy dunders for private keys
# cryptography >= 45.0.0 requires copy + deepcopy on private key impls (py3.14)
# https://github.com/tpm2-software/tpm2-pytss/commit/6ab4c74e6fb3da7cd38e97c1f8e92532312f8439
Patch4:         %{name}-copy-dunder.patch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%if %{undefined rhel} || (0%{?oreon} >= 11)
BuildRequires:  python3-pytest-xdist
%endif
BuildRequires:  tpm2-tss-devel >= 2.0.0
BuildRequires:  gcc
# for tests
BuildRequires:  swtpm
BuildRequires:  tpm2-tools

%global _description %{expand:
TPM2 TSS Python bindings for Enhanced System API (ESYS), Feature API (FAPI),
Marshaling (MU), TCTI Loader (TCTILdr) and RC Decoding (rcdecode) libraries.
It also contains utility methods for wrapping keys to TPM 2.0 data structures
for importation into the TPM, unwrapping keys and exporting them from the TPM,
TPM-less makecredential command and name calculations, TSS2 PEM Key format
support, importing Keys from PEM, DER and SSH formats, conversion from
tpm2-tools based command line strings and loading tpm2-tools context files.
}

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files %{_name}


%check
%pyproject_check_import
# The test test_tools_decode_tpml_tagged_tpm_property checks TPM2 revision which is not stable
# In upstream this test as well as the tools are removed so I do not have any good way to fix it
%ifarch s390x
# this test does not work for some reason on the s390x as it times out
%global testargs -k "not test_spi_helper_good and not test_tools_decode_tpml_tagged_tpm_property"
%else
%global testargs -k "not test_tools_decode_tpml_tagged_tpm_property"
%endif
%pytest --import-mode=append %{?!rhel:-n 1} %{?testargs}


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.0-10
- Import
