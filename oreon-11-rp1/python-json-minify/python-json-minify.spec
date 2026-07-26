%global source0_hash 499717626144a533d64ed4a1513976cf2212958b6806a66e07dd8e22207df559

%global srcname json-minify
%global srcname_ json_minify
%global Srcname_ JSON_minify

Name:           python-%{srcname}
Version:        0.3.0
Release:        29%{?dist}
Summary:        Python port of the JSON-minify utility

License:        MIT
URL:            https://github.com/getify/JSON.minify/tree/python
Source:         %pypi_source %{Srcname_}
# Fix invalid escape sequences in regex strings.
Patch:          https://github.com/getify/JSON.minify/pull/74.patch

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%description
JSON-minify minifies blocks of JSON-like content into valid JSON by removing
all whitespace *and* JS-style comments. With JSON-minify, you can maintain
developer-friendly JSON documents, but minify them before parsing or
transmitting them over-the-wire.

%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{srcname}
JSON-minify minifies blocks of JSON-like content into valid JSON by removing
all whitespace *and* JS-style comments. With JSON-minify, you can maintain
developer-friendly JSON documents, but minify them before parsing or
transmitting them over-the-wire.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{Srcname_}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L %{srcname_}

%check
%{python3} -m unittest discover

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
