%global source0_hash abb64768d25bf563da8e2165d477a491cba18bc22c4ec8db7acbdae94e59ebc4

%global desc %{expand:
Python bindings for the AWS Common Runtime}


Name:           python-awscrt
Version:        0.31.1
Release:        %autorelease

Summary:        Python bindings for the AWS Common Runtime
# All files are licensed under Apache-2.0, except:
# - crt/aws-c-common/include/aws/common/external/cJSON.h is MIT
# - crt/aws-c-common/source/external/cJSON.c is MIT
# - crt/s2n/pq-crypto/kyber_r3/KeccakP-brg_endian_avx2.h is BSD-3-Clause
License:        Apache-2.0 AND MIT AND BSD-3-Clause
URL:            https://github.com/awslabs/aws-crt-python

Source0:        https://files.pythonhosted.org/packages/source/a/awscrt/awscrt-0.31.1.tar.gz

# two tests require internet connection, skip them
Patch0:         skip-tests-requiring-network.patch
# skip SHA1 in test_crypto
Patch1:         skip-SHA1-in-test_crypto.patch
# websockets test fail fix
Patch2:         websockets.patch

BuildRequires:  python%{python3_pkgversion}-devel

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  openssl-devel

BuildRequires:  python%{python3_pkgversion}-websockets

ExcludeArch:    %{ix86}


%description
%{desc}


%package -n python%{python3_pkgversion}-awscrt
Summary:        %{summary}


%description -n python%{python3_pkgversion}-awscrt
%{desc}


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n awscrt-%{version}

# relax version requirements
sed -i -e 's/setuptools>=75\.3\.1/setuptools/' -e 's/wheel>=0\.45\.1/wheel/' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires


%build
export AWS_CRT_BUILD_USE_SYSTEM_LIBCRYPTO=1
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files _awscrt awscrt


%check
%{py3_test_envvars} %{python3} -m unittest


%files -n python%{python3_pkgversion}-awscrt -f %{pyproject_files}
%doc README.md


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.31.1-1
- Prepare for Oreon 11 (RP1)
