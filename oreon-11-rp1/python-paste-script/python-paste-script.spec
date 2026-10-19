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
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD AND (LicenseRef-Callaway-MIT OR LicenseRef-Callaway-Python)
Summary:        A pluggable command-line frontend
URL:            https://github.com/cdent/pastescript
Source0:        https://pypi.python.org/packages/source/P/PasteScript/PasteScript-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-paste-script = %{version}-%{release}
# /oreon:deps
%description
%{desc}

%package -n python3-paste-script
Summary:        %{sum}
%description -n python3-paste-script
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir PasteScript-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
mv %{buildroot}%{_bindir}/paster %{buildroot}%{_bindir}/paster-%{python3_version}
ln -s ./paster-%{python3_version} %{buildroot}%{_bindir}/paster-3
%oreon_autofiles python3-paste-script usr/lib/python3*/site-packages/paste_script* usr/lib64/python3*/site-packages/paste_script* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/paste_script* usr/lib64/python3*/site-packages/paste_script* usr/bin/*

%files
%files -n python3-paste-script -f %{oreon_filedir}/python3-paste-script.list

%changelog

%autochangelog
