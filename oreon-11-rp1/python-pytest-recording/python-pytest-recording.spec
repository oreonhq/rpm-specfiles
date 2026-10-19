%global source0_hash 568d64b2a85992eec4ae0a419c855d5fd96782c5fb016784d86f18053792768c
Name:           python-pytest-recording
Version:        0.13.4
Release:        1%{?dist}
Summary:        A pytest plugin powered by VCR.py to record and replay HTTP traffic
License:        MIT
URL:            https://github.com/kiwicom/pytest-recording
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_recording/pytest_recording-%{version}.tar.gz
BuildArch:      noarch
Patch0:         werkzeug.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pytest-recording = %{version}-%{release}
# /oreon:deps
%package -n       python3-pytest-recording+tests
Summary:        Metapackage for python3-pytest-recording tests extras
Requires:       python3-pytest-recording = %{version}-%{release}
Requires:       python3dist(werkzeug) == 3.1.3
Provides:       python3dist(pytest-recording[tests]) = %{version}-%{release}

%description -n python3-pytest-recording+tests
Metapackage for python3-pytest-recording tests extras.

%package -n       python3-pytest-recording+dev
Summary:        Metapackage for python3-pytest-recording dev extras
Requires:       python3-pytest-recording = %{version}-%{release}
Provides:       python3dist(pytest-recording[dev]) = %{version}-%{release}

%description -n python3-pytest-recording+dev
Metapackage for python3-pytest-recording dev extras.

%description

%package -n     python3-pytest-recording
Summary:        A pytest plugin powered by VCR.py to record and replay HTTP traffic
# oreon:reqs
Requires:       python3dist(pytest) >= 3.5.0
Requires:       python3dist(vcrpy) >= 2.0.1
# /oreon:reqs
%description -n python3-pytest-recording

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pytest_recording-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-recording usr/lib/python3*/site-packages/pytest_recording* usr/lib64/python3*/site-packages/pytest_recording* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_recording* usr/lib64/python3*/site-packages/pytest_recording* usr/bin/*

%check

%pyproject_check_import
k="${k-}${k+ and }not (test_block_network_with_allowed_hosts[block_marker])"
k="${k-}${k+ and }not (test_block_network_with_allowed_hosts[block_cmd])"
k="${k-}${k+ and }not (test_block_network_with_allowed_hosts[vcr_cfg])"
%pytest -k "${k-}"
%files
%files -n python3-pytest-recording -f %{oreon_filedir}/python3-pytest-recording.list

%changelog

%autochangelog
