%global source0_hash a11bf7d5b4d13d809d2ed7ed3a20b71994447ad203fb5f20f1fd073948e95086

%global srcname bitstring

Name:           python-%{srcname}
Version:        4.1.4
Release:        11%{?dist}
Summary:        Simple construction, analysis and modification of binary data

License:        MIT
URL:            https://github.com/scott-griffiths/bitstring
Source0:        https://github.com/scott-griffiths/bitstring/archive/%{srcname}-%{version}/%{srcname}-%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
bitstring is a pure Python module designed to help make the creation and
analysis of binary data as simple and natural as possible.

Bitstrings can be constructed from integers (big and little endian), hex,
octal, binary, strings or files. They can be sliced, joined, reversed,
inserted into, overwritten, etc. with simple functions or slice notation.
They can also be read from, searched and replaced, and navigated in, similar
to a file or stream.}

%description %_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel

%generate_buildrequires
%pyproject_buildrequires

%description -n python%{python3_pkgversion}-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{srcname}-%{version}

sed -i '1{s|^#!\(/usr\)\?/bin/\(env \)\?python\d\?$||}' %{srcname}/__init__.py

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files bitstring

%check
%{__python3} -m unittest

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.md release_notes.txt

%changelog
%autochangelog
