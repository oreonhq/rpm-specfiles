%global source0_hash c7c0bf85af0f70ca2ef4b6ea9a74ef372f73392aa17bea0d885dcba7356d0867

Name:           python-wheezy-template
Version:        3.2.5
Release:        1%{?dist}
Summary:        Python template library
License:        MIT
URL:            https://pypi.org/project/wheezy.template/
Source0:        https://files.pythonhosted.org/packages/43/1d/b4fb6ee3f6a0af54ac26e0425b7947bd7d9ed786a75ca173a40640c25bc6/wheezy_template-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%description
A lightweight template library.

%package -n python3-wheezy-template
Summary:        %{summary}
Provides:       python3dist(wheezy.template) = %{version}

%description -n python3-wheezy-template
A lightweight template library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n wheezy_template-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files wheezy

%files -n python3-wheezy-template -f %{pyproject_files}
