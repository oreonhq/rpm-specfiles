%global source0_hash e8add7980a7574b5114185ff3fdea9b3ad6aa766f6c8253f8e77f59641fc2612

%global         commit          8c47cc9e665b3b1744cccfaa7a650de5f3c575dd
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})
%global         commitdate      20200323
%global         srcname         jstyleson
%global         forgeurl        https://github.com/linjackson78/jstyleson
Version:        0.0.2^%{commitdate}.%{shortcommit}
%global         tag             %{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        A python library to parse JSON with js-style comments

License:        MIT
URL:            %{forgeurl}
Source:         %{forgeurl}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

BuildArch: noarch

%global _description %{expand:
jstyleson is a python library to parse JSON with js-style comments.
Trailing comma is also supported.

JSON by standard does not allow comments and trailing comma, and the
python standard json module does not offer options to parse such informal
JSON.

jstyleson try to make it happy with your js-style commented JSON, by first
removing all elements inside (comments and trailing comma), then hand it
to the standard json module.

jstyleson supports parsing JSON with:

- single-line comment
- multi-line comment
- inline comment
- trailing comma
}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{commit}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check 
%pytest tests

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE
 
%changelog
%autochangelog
