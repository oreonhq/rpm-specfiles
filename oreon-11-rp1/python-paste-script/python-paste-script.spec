%global source0_hash ddec801a13ac667e094edde28f90212cdea7bdc9a18d4371b08f5a6ef7d2eba2

%global desc Paster is pluggable command-line frontend, including commands to setup package\
file layouts\
\
Built-in features:\
\
 * Creating file layouts for packages.\
   For instance a setuptools-ready file layout.\
 * Serving up web applications, with configuration based on paste.deploy\
%global sum A pluggable command-line frontend

Name:           python-paste-script
Version:        3.3.0
Release:        12%{?dist}
BuildArch:      noarch

# paste/script/wsgiserver/ is BSD licensed from CherryPy
# paste/script/util/subprocess24.py is MIT or Python
# string24.py may also be MIT or Python (looks to have come from the python-2.4 release)
# The rest of the code is MIT.
# Automatically converted from old format: MIT and BSD and (MIT or Python) - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD AND (LicenseRef-Callaway-MIT OR LicenseRef-Callaway-Python)
Summary:        %{sum}
URL:            https://github.com/cdent/pastescript
Source0:        https://pypi.python.org/packages/source/P/PasteScript/PasteScript-%{version}.tar.gz

BuildRequires:  python3-devel

%description
%{desc}

%package -n python3-paste-script
Summary:        %{sum}

%description -n python3-paste-script
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n PasteScript-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

find docs -type f -exec chmod 0644 \{\} \;

%build
%pyproject_wheel

%install
%pyproject_install

mv %{buildroot}%{_bindir}/paster %{buildroot}%{_bindir}/paster-%{python3_version}
ln -s ./paster-%{python3_version} %{buildroot}%{_bindir}/paster-3

%pyproject_save_files paste

# TODO: enable tests in the future.  dependency mess right now for python 3.11+
#%%check
#%%tox

%files -n python3-paste-script -f %{pyproject_files}
%license docs/license.txt
%doc docs/*
%{python3_sitelib}/PasteScript-%{version}-py%{python3_version}-nspkg.pth
%{_bindir}/paster-3
%{_bindir}/paster-%{python3_version}

%changelog
%autochangelog
