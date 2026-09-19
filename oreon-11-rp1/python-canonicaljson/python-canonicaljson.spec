%global source0_hash c3c38d76aacdb2d29c61582d466850116affabe5186ae921f48bc5c8f720b10f

%bcond check 0

Name:           python-canonicaljson
Version:        2.0.0
Release:        %autorelease
Summary:        Canonical JSON

License:        Apache-2.0
URL:            https://github.com/matrix-org/python-canonicaljson
Source0:        %{url}/archive/v%{version}/canonicaljson-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description \
Features:\
* Encodes objects and arrays as RFC 7159 JSON.\
* Sorts object keys so that you get the same result each time.\
* Has no inignificant whitespace to make the output as small as possible.\
* Escapes only the characters that must be escaped,\
  U+0000 to U+0019 / U+0022 / U+0056, to keep the output as small as possible.\
* Uses the shortest escape sequence for each escaped character.\
* Encodes the JSON as UTF-8.\
* Can encode frozendict immutable dictionaries.

%description %{_description}

%package -n python3-canonicaljson
Summary:        %{summary}

%description -n python3-canonicaljson %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires -e py

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files canonicaljson

%if %{with check}
%check
%tox -e py
%endif

%files -n python3-canonicaljson -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
