%global source0_hash f8a16081043e1af20705e211bda41b64c3f08a45785755daec539ae41281c5d1

%{?python_enable_dependency_generator}
%global srcname fontname

Name:           python-fontname
Version:        1.0.0
Release:        14%{?dist}
Summary:        A lib for guessing font name

License:        MIT
URL:            https://github.com/Asvel/fontname
Source0:        https://files.pythonhosted.org/packages/00/3b/0d282acce368434b16a2e956ebfa18f59317854a5949fadb00edbeff0a8b/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description\
fontname is a lib for guessing font name, in other words, reading and decoding\
quirk encoded raw font name.\
\
It current supports SFNT format fonts, and is adept at dealing with CJK fonts.

%description %_description

%package -n python3-%{srcname}
Summary:        A lib for guessing font name
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
fontname is a lib for guessing font name, in other words, reading and decoding
quirk encoded raw font name.

It current supports SFNT format fonts, and is adept at dealing with CJK fonts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files fontname

%check
# add below to make sure initial build will catch runtime import errors
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc PKG-INFO README.rst
%license LICENSE.txt

%changelog
%autochangelog
