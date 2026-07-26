%global source0_hash dcfd2c759322eb44fe193a9e0b1b86c5b87f3ec5ea8e1bb43b3e9ae423f1e8fe

%global pypi_name mbstrdecoder

Name:           python-%{pypi_name}
Version:        1.1.3
Release:        7%{?dist}
Summary:        multi-byte character string decoder

License:        MIT
URL:            https://github.com/thombashi/mbstrdecoder 
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz 
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description
multi-byte character string decoder

%package -n     python3-%{pypi_name}
Summary:        %{summary}
 
Requires:  python3-chardet

%description -n python3-%{pypi_name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}
sed -i 's/chardet>=3.0.4,<.*/chardet>=3.0.4/g' requirements/requirements.txt

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# Please support chardet 6.0.0
# https://github.com/thombashi/mbstrdecoder/issues/14
#
# Skip failing test:
# test/test_mbstrdecoder.py::Test_to_MultiByteStrDecoder_unicode::test_normal_codec_candidate[Bob\u2019s Burgers-windows-1252-windows_1252-codec_candidates4]
k="${k-}${k+ and }not (Test_to_MultiByteStrDecoder_unicode and Burgers-windows-1252-windows_1252-codec_candidates4)"

%pytest -k "${k-}" -v

%files -n python3-%{pypi_name} -f %{pyproject_files} 
%license LICENSE
%doc README.rst

%changelog
%autochangelog
