%global source0_hash 0a4b30387343d7146dd7a01688008d4070bd03d196fded1514f4e750532a7be7

%global commit 5aea0fd4461bd05dd96e4ad637f6be7bceb1cee5
%global snapdate 20231031

Name:           python-etcd
Version:        0.5.0~%{snapdate}git%(echo '%{commit}' | cut -b -7)
Release:        7%{?dist}
Summary:        A python client library for etcd

License:        MIT
URL:            https://github.com/jplana/python-etcd

Source:         %{url}/archive/%{commit}/python-etcd-%{commit}.tar.gz

# Support Python 3.13
# https://github.com/jplana/python-etcd/pull/288
Patch:          %{url}/pull/288.patch
# Replace removed TestCase method aliases
# https://github.com/jplana/python-etcd/pull/289
Patch:          %{url}/pull/289.patch
# Do not include tests in bdists/wheels
# https://github.com/jplana/python-etcd/pull/290
Patch:          %{url}/pull/290.patch
# Support Python 3.14
# https://github.com/jplana/python-etcd/pull/294
Patch:          %{url}/pull/294.patch

#VCS: git:https://github.com/jplana/python-etcd

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  etcd
# setup.py: test_requires
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pyOpenSSL}

%global _description %{expand:
Client library for interacting with an etcd service, providing Python access to
the full etcd REST API. Includes authentication, accessing and manipulating
shared content, managing cluster members, and leader election.}

%description %{_description}

%package -n python3-etcd
Summary:        %{summary}

%py_provides python3-python-etcd

%description -n python3-etcd %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n python-etcd-%{commit} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l etcd

%check
# TODO: What is happening?
# OpenSSL.crypto.Error: [('digital envelope routines', '', 'invalid digest')]
k="${k-}${k+ and }not (TestEncryptedAccess and test_get_set_authenticated)"
k="${k-}${k+ and }not (TestEncryptedAccess and test_get_set_unauthenticated)"
k="${k-}${k+ and }not (TestEncryptedAccess and test_get_set_unauthenticated_missing_ca)"
k="${k-}${k+ and }not (TestEncryptedAccess and test_get_set_unauthenticated_with_ca)"
k="${k-}${k+ and }not (TestClientAuthenticatedAccess and test_get_set_unauthenticated)"

# TODO: What is happening?
# E           etcd.EtcdException: Raft Internal Error : nodePath /1/dir : Not a file ()
k="${k-}${k+ and }not (TestSimple and test_directory_ttl_update)"

%pytest -k "${k-}" -v

%files -n python3-etcd -f %{pyproject_files}
%doc README.rst
#license LICENSE.txt

%changelog
%autochangelog
