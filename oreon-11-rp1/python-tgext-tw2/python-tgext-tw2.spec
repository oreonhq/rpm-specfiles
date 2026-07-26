%global source0_hash ebe86df9bc64d4ab8fdcbde3781d6605b81aff2daacb77696ead81cabd7b8a64

%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname tgext-tw2

Name:           python-tgext-tw2
Version:        0.1
Release:        %autorelease
Summary:        Support ToscaWidgets2 forms and validation in TurboGears
License:        MIT
URL:            https://github.com/TurboGears/tgext.tw2
# Unable to use pypi_source, missing tests/kajiki_form.xhtml file
#Source0:        pypi_source tgext.tw2
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(webtest)

%description
Support ToscaWidgets2 forms and validation in TurboGears 2.5+

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
Support ToscaWidgets2 forms and validation in TurboGears 2.5+

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n tgext.tw2-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l tgext

%check
%pytest

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
