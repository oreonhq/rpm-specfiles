%global source0_hash 88abb1f60a4b01e0e941714e12fbab36c7f63513da66a8f70c83b84f994a882c

Name:           python-aiostream
Version:        0.7.0
Release:        3%{?dist}
Summary:        Generator-based operators for asynchronous iteration

License:        GPL-3.0-only
URL:            https://github.com/vxgmichel/aiostream
Source:         %{url}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

Patch0:         require-lower-setuptools-version.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio

%global _description %{expand:
aiostream provides a collection of stream operators that can be combined to
create asynchronous pipelines of operations.

It can be seen as an asynchronous version of itertools, although some aspects
are slightly different. Essentially, all the provided operators return a
unified interface called a stream.}

%description %_description

%package -n python3-aiostream
Summary:        %{summary}

%description -n python3-aiostream %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n aiostream-%{version}

# Don't run coverage as part of tests
sed -r \
    -e 's/ --cov aiostream//' \
    -i pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files aiostream

%check
# Use --import-mode to solve file mismatch error
%pytest -v --import-mode importlib

%files -n python3-aiostream -f %{pyproject_files}
%doc README.*

%changelog
%autochangelog
