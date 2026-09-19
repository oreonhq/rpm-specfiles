%global source0_hash b1ac1515e84fa4c31dc10ad1a7800c0f305a1a3887b4b4e6e1980ceda4f50173

Name:           python-sphinxygen
Version:        1.0.12
Release:        2%{?dist}
Summary:        A script to read Doxygen XML output and emit ReST for Sphinx

# All files under ISC, though some tests and
# unpackaged files are under 0BSD
License:        ISC
URL:            https://gitlab.com/drobilla/sphinxygen
# Source from Pypi does not include all test files
Source:        %{url}/-/archive/v%{version}/sphinxygen-v%{version}.tar.gz

# Fix tests with doxygen version 1.14
# https://gitlab.com/drobilla/sphinxygen/-/merge_requests/2
Patch:          0001-Fix-tests-with-doxygen-1.14.patch

BuildRequires:  sed
BuildRequires:  python3-devel
# Needed for tests
# html5lib is not currently available on EPEL10
%if 0%{?fedora}
BuildRequires:  doxygen
BuildRequires:  python3dist(html5lib)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)
%endif

BuildArch: noarch

%global _description %{expand:
Sphinxygen is a Python module/script that generates Sphinx markup to describe
a C API, from an XML description extracted by Doxygen.}

%description %_description

%package -n python3-sphinxygen
Summary:        %{summary}

%description -n python3-sphinxygen %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n sphinxygen-v%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinxygen
# fix permissions
chmod 644 %{buildroot}%{python3_sitelib}/sphinxygen/sphinxygen.py
# remove shebang line
sed -i '/^#!\/usr\/bin/d' %{buildroot}%{python3_sitelib}/sphinxygen/sphinxygen.py

# install manpage
mkdir -p %{buildroot}%{_mandir}/man1
install -Dpm 0644 doc/sphinxygen.1 -t %{buildroot}%{_mandir}/man1/

%check
%if 0%{?fedora}
%pytest test
%else
%pyproject_check_import
%endif

%files -n python3-sphinxygen -f %{pyproject_files}
%doc README.md NEWS
%{_bindir}/sphinxygen
%{_mandir}/man1/sphinxygen.1*
 
%changelog
%autochangelog
