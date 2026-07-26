%global source0_hash e588fdcbd03e58287ffb5495d8f38f36ebacc5ddeb615146f0d00e009a830587

%global _description %{expand:
Pygments lexers for Git output and files.}

Name:           python-pygments-git
Version:        1.6.0
Release:        %{autorelease}
Summary:        Pygments lexers for Git output and files

License:        MIT
URL:            https://github.com/adamchainz/pygments-git
Source0:        %{url}/archive/%{version}/pygments-git-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-pygments-git
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-pygments-git %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pygments-git-%{version}

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

# we use the template because we don't want the strict versioning
sed -i "s|-r requirements/{envname}.txt|-r requirements/requirements.in|" tox.ini

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pygments_git

%check
%pyproject_check_import
%tox

%files -n python3-pygments-git -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
