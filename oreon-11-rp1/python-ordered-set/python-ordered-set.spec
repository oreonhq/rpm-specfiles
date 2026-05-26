%global srcname ordered-set
%global dir_name ordered_set

Name:           python-%{srcname}
Version:        4.1.0
Release:        %autorelease
Summary:        Custom MutableSet that remembers its order

License:        MIT
URL:            https://github.com/rspeer/ordered-set
Source0:        https://files.pythonhosted.org/packages/source/o/ordered-set/ordered-set-4.1.0.tar.gz
# oreon url source checksums begin
%global source0_sha256 694a8e44c87657c59292ede72891eb91d34131f6531463aab3009191c77364a8
%global source0_file ordered-set-4.1.0.tar.gz
# oreon url source checksums end

BuildArch:      noarch
BuildRequires:  python3-devel
#tests
BuildRequires:  python3-pytest

%global _description\
An OrderedSet is a custom MutableSet that remembers its order, so that every\
entry has an index that can be looked up.

%description %_description

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python3-%{srcname} %{_description}

Python 3 version.

%generate_buildrequires
%pyproject_buildrequires

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/ordered-set-4.1.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "694a8e44c87657c59292ede72891eb91d34131f6531463aab3009191c77364a8" || { echo "oreon: Source0 SHA256 mismatch for ordered-set-4.1.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n %{srcname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest

%files -n python3-%{srcname}
%license MIT-LICENSE
%doc README.md
%dir %{python3_sitelib}/%{dir_name}
%{python3_sitelib}/%{dir_name}/*.py
%{python3_sitelib}/%{dir_name}/__pycache__
%{python3_sitelib}/%{dir_name}/py.typed
%{python3_sitelib}/*.dist-info

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.1.0-1
- Prepare for Oreon 11 (RP1)
