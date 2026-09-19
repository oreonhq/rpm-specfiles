%global source0_hash 3a1581f611d9dace7dee35f288e5f3891066a9dd1f5f0881532289fc37f89ea5

%bcond_with bootstrap

Name:           python-cobalt
Version:        9.0.1
Release:        %autorelease
Summary:        A lightweight library for working with Akoma Ntoso Act documents

License:        LGPL-3.0-or-later
URL:            https://github.com/laws-africa/cobalt
Source:         %{pypi_source cobalt}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
# Documentation requirements
%if %{without bootstrap}
BuildRequires:  python3dist(cobalt)
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx_rtd_theme
# Generate DocBook for internal documentation
BuildRequires:  python3-sphinx-design
BuildRequires:  texinfo
%endif

%global _description %{expand:
Cobalt is a lightweight Python library for working with Akoma Ntoso documents.
It makes it easy to work with Akoma Ntoso documents, metadata and FRBR URIs.

It is lightweight because most operations are done on the XML document directly
without intermediate objects. You still need to understand how Akoma Ntoso
works.}

%description %_description

%package -n     python3-cobalt
Summary:        %{summary}

%description -n python3-cobalt %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n cobalt-%{version}
%if %{without bootstrap}
sed -i '/with open("..\/VERSION") as f:/d' docs/conf.py
sed -i '/release = f.read/d' docs/conf.py
SHORTVERSION="$(echo %{version} | cut --delimiter '.'  --complement -f3)"
echo $SHORTVERSION
sed -i "s/version = '.'.join(release.split('.')\[:2\])/version = '${SHORTVERSION}'/g" docs/conf.py
cat docs/conf.py
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
%if %{without bootstrap}
# Build documentation
sphinx-build docs texinfo -b texinfo
pushd texinfo
makeinfo --docbook cobalt.texi
popd
%endif

%install
%pyproject_install
%pyproject_save_files -l cobalt
%if %{without bootstrap}
mkdir -p %{buildroot}%{_datadir}/help/en/python-cobalt/
install -m 644 texinfo/cobalt.xml %{buildroot}%{_datadir}/help/en/python-cobalt/
%endif

%check
%pyproject_check_import
%pytest

%files -n python3-cobalt -f %{pyproject_files}
%if %{without bootstrap}
%dir  %{_datadir}/help/en
%lang(en) %{_datadir}/help/en/python-cobalt/
%endif

%changelog
%autochangelog
