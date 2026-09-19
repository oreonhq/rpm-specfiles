%global source0_hash e769819ff0b0c043d020246ce1defcaadd65b9c21d244468a45a7f06cb88af5d

Name:           python-oauth
Version:        1.0.1
Release:        44%{?dist}
Summary:        Library for OAuth version 1.0a

License:        MIT
URL:            http://code.google.com/p/oauth/
Source0:        http://pypi.python.org/packages/source/o/oauth/oauth-%{version}.tar.gz

# In Python 3 urlparse is urllib.parse
Patch0:         oauth-python3.patch

BuildArch:      noarch
BuildRequires:  python3-devel
# Needed for %%check
BuildRequires:  python3-cgi

%global _description\
Library for OAuth version 1.0a.\

%description %_description

%package -n python3-oauth
Summary: %summary

%description -n python3-oauth %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n oauth-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

%install
%{pyproject_install}
%pyproject_save_files '*'
 

%check
%pyproject_check_import

%files -n python3-oauth -f %{pyproject_files}
%doc LICENSE.txt

%changelog
%autochangelog
