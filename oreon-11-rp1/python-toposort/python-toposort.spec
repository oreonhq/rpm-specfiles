%global source0_hash bfbb479c53d0a696ea7402601f4e693c97b0367837c8898bc6471adfca37a6bd

Name:           python-toposort
Version:        1.10
Release:        1%{?dist}
Summary:        Topological sort implementation
License:        Apache-2.0
URL:            https://pypi.org/project/toposort/
Source0:        https://files.pythonhosted.org/packages/69/19/8e955d90985ecbd3b9adb2a759753a6840da2dff3c569d412b2c9217678b/toposort-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%description
A topological sort for python.

%package -n python3-toposort
Summary:        %{summary}

%description -n python3-toposort
A topological sort for python.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n toposort-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files toposort

%files -n python3-toposort -f %{pyproject_files}
